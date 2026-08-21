# Job Digest, 21 August 2026

Run type: Scheduled Cowork Agent A run (normal backlog gate).
Render toolchain: installed clean this run (weasyprint 69.0, python-docx 1.2.0, pypdf 6.16.1). `import weasyprint, docx, pypdf` printed `render toolchain ok`.

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **4** rows in Status = `drafted` at run start:
- Sana HR Solutions GmbH, Werkstudent Data Engineer (Taetigkeits-ID 7016)
- Robert Bosch GmbH, Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank (REF293881R)
- FLEX Capital Management GmbH, Werkstudent Data Science and AI
- Amprion GmbH, Werkstudent KI (Stellen-ID 7959)

4 drafted is under 8, so the 28 July 2026 gate applied normally: top 3 to 5 cut. Backlog after this run: **6** drafted in Notion (4 at start, minus 0 resolved, plus 2 new).

### Flag: possible concurrent or interrupted duplicate run

Three of the four starting rows (Sana HR Solutions, Robert Bosch Masterarbeit, FLEX Capital Management) have a Notion `createdTime` of `2026-08-21 11:48:15Z`, about 16 minutes before this session started, and one of them (Amprion Werkstudent KI) carries a Notes field reading *"Reconciled 2026-08-21: CSV had row with no Notion counterpart, created with CSV status per CLAUDE.md Step 3"* -- language that matches this very reconciliation process. None of the three new-looking rows have a matching `applied-log.csv` row, a `drafts/` folder in this checkout, or a same-day git commit (`git log` shows the latest commit is 20 Aug 2026, and the Sana HR Solutions posting on StepStone confirms it is a real, currently live listing, so this is not a hallucinated row).

This is strong evidence that another Cowork session ran very recently, wrote three Notion rows, and then stopped before reaching the CSV write, commit, or push steps -- possibly a duplicate scheduled firing, or a session that crashed mid-run. Per CLAUDE.md invariant #2 (git is the source of truth for content) this run did **not** invent draft folders or CSV rows for those three roles to "fill the gap." They are left exactly as Notion has them. **Rah: please check for another Cowork session that may be stuck or duplicated, and decide whether to re-run those three roles from scratch (their Draft Path folders do not exist in the repo) or leave them as an orphaned Notion-only record.**

## Reconciliation

Full sweep of all 149 `applied-log.csv` rows against Notion (not just the newest rows): **32 rows updated** from a stale CSV status to the true Notion status. Notably:
- 27 older rows had moved from `applied` to `rejected` in Notion without the CSV mirror catching up (normal drift from OpenClaw/manual outcome tracking over time).
- Of the 6 rows drafted on 20 Aug: Amprion Werkstudent KI matched Notion already (no change); Ed. Zueblin AG, PwC Deutschland, Bosch Rexroth AG, and Amprion Masterarbeit had all moved to `applied` in Notion; Ardex GmbH had moved to `Not listed Anymore`. All five updated in the CSV to match.
- No CSV row was genuinely missing a Notion counterpart (an apparent one-row mismatch on "Aerzteverband Deutscher Allergologen" turned out to be a Unicode normalisation artifact in the diff script, not real drift -- the row is present in both under its proper spelling).

CSV and Notion are now aligned. This is a heavier-than-usual reconciliation pass; the drift had clearly been accumulating over several runs.

## Top cut (2 roles drafted)

Search covered LinkedIn, StepStone, Xing, and company career pages via web search/extract this run. The Indeed MCP tool was not present in this session's available tools, so Indeed sourcing was skipped rather than substituted with an unverified fallback -- noted as a source gap below.

### 1. BCG Platinion, Muenchen
**Werkstudent AI und Data Analytics, Energy Knowledge Management**
- Source: StepStone, posted about 17 hours before this run. Homeoffice moeglich, Teilzeit.
- Apply link: https://www.stepstone.de/stellenangebote--Werkstudent-in-AI-Data-Analytics-Energy-Knowledge-Management-all-genders-Muenchen-BCG-Platinion--14369735-inline.html
- Apply method: platform-native (StepStone Schnelle Bewerbung)
- Language track: DE (posting body entirely in German)
- German level required: not explicitly stated ("gute Kommunikationsfaehigkeiten in Deutsch und Englisch"), recorded as `none` in Notion rather than guessing a tier
- Fit rationale: role is feasibility studies and agentic development of AI/Analytics applications (AI agents, chatbots, full stack apps) for BCG's Energy Practice, plus market/tech trend research and training material upkeep -- a strong match for the Multi Agent RAG project's LangGraph orchestration and evaluation harness
- Projects selected: Multi Agent RAG with LLM as Judge (DE), Movie Analytics and ML Pipeline on GCP (DE)
- Certifications: NVIDIA (led, per AI/RAG routing rule), AWS Academy, Google Data Analytics
- Deliverables: all 8 rendered, CV 2 pages, no banned strings, Ojas header confirmed

### 2. Arthrex GmbH, Muenchen
**Working Student, Business Analytics and Process Optimization**
- Source: StepStone, posted about 2 days before this run. Homeoffice moeglich, Teilzeit.
- Apply link: https://www.stepstone.de/stellenangebote--Working-Student-Business-Analytics-Process-Optimization-Muenchen-Arthrex-GmbH--14411716-inline.html
- Apply method: platform-native (StepStone)
- Language track: EN (posting body entirely in English, "Your Tasks" / "Your Qualifications")
- German level required: "business-fluent German proficiency" stated explicitly, no CEFR level given; recorded as `B2` in Notion as a conservative estimate. **This is above Rah's current B1** -- disclosed openly in the cover letter's closing paragraph, following the same honesty pattern used for the CHECK24 and BMW drafts on 13 Aug.
- Fit rationale: logistics/transportation process optimization, data analysis and dashboard reporting, Power BI/Power Automate exposure valued -- strong match for the Fast Food Tableau dashboard project and the Climate Economics analytics pipeline
- Projects selected: Fast Food Nutritional Analyzer and Meal Simulator (EN), Economic Impact Analysis of Global Climate Events (EN)
- Certifications: SAS Viya (led, per BI/Analyst routing rule), Google Data Analytics, AWS Academy
- Deliverables: all 8 rendered, CV 2 pages, no banned strings, Ojas header confirmed

## Watchlist (scored but not drafted, real language or freshness blockers)

- **AKDB, Werkstudent AI and Machine Learning NLP and Semantic Search, Muenchen** -- strong RAG/embeddings fit, but requires verhandlungssichere Deutschkenntnisse mindestens C1. Large gap versus current B1.
- **statworx, Werkstudent Automation und AI, Frankfurt** -- still live on the company's own Personio page, but requires sehr gute Deutsch- und Englischkenntnisse mindestens C1.
- **50Hertz Transmission, Werkstudentin Data Analytics und Konzepte im EU-Strommarkt, Berlin** -- good Python/data-analysis fit, requires gute Deutschkenntnisse B2.

## Dropped this run (verified dead or unverifiable, not silently skipped)

- **Delivery Hero, Working Student Data Engineering (Vendor), Berlin** -- excellent dbt/BigQuery/Airflow fit, but the company careers page states "This vacancy has expired."
- **MEAG MUNICH ERGO, Werkstudent Data Enablement, Muenchen** -- StepStone shows the apply button as "Nicht verfuegbar" (closed-listing signal); also requires German and English at least B2.
- **Vecrion AI, Werkstudent Generative AI Agentic Systems** -- LinkedIn lists the company location as Indiana, United States, outside the Germany/remote-EU scope.
- **Novo AI, Data Engineer Intern (Pflichtpraktikum), Hannover/Frankfurt** -- LinkedIn required login to read the job description; could not verify content, so not drafted rather than guessing.
- **XING frankfurt-main-werkstudent-data-scientist-152990082 (aviation/facility services Data Scientist)** -- XING itself returns "This job ad isn't available."
- **PIMCO Prime Real Estate / Allianz, Intern Software and Data Engineering, Muenchen** -- page rendered with empty task/requirement sections (JS-gated content), could not verify.

## Transparency block

- **Sources reachable this run:** LinkedIn (search snippets only, most full postings login-walled), StepStone (fully readable, both drafted roles sourced here), Xing (mostly expired or unavailable postings this run), company career pages (statworx Personio page reachable, Delivery Hero and Arthrex/careers.arthrex.com reachable).
- **Sources not used:** Indeed -- the Indeed MCP tool was not present in this session's tool set. Web-fetch fallback was deliberately not substituted, per CLAUDE.md's preference for the dedicated Indeed tool; this is a real source gap this run, not a policy choice.
- **Platform mix:** StepStone 2, all other sources 0. Narrower than the usual 28 July yield target because every promising LinkedIn/Xing lead this run turned out expired, login-walled, or otherwise unverifiable. Flagged honestly rather than padded with a weaker pick to hit a platform quota.
- **Freshness:** BCG Platinion posted ~17 hours before this run; Arthrex posted ~2 days before this run. Both current dates confirmed against StepStone's own "Erschienen: vor X" timestamps.
- **Prompt-injection content observed but not acted on:** none this run.
- **Distance was not a scoring factor**, per master-projects.md.
- **Language track decisions:** BCG Platinion DE (posting body in German), Arthrex EN (posting body in English despite the company being Munich-based).
- **Notion query quota:** the post-write verification SQL query (`SELECT ... WHERE Status = 'drafted'`) hit the workspace's Notion query rate limit after the two `create-pages` calls. The `create-pages` tool call itself returned both new page IDs with all properties echoed back correctly, which stands as the audit evidence for this run; a follow-up count could not be independently confirmed via SQL due to the quota.

## Tool failure this run

`mcp__Gmail__create_draft` returned "The service is currently unavailable" on two consecutive attempts. No Gmail draft was created this run. This digest file and the git push are the authoritative record; Rah should check the repo directly rather than expect a Gmail draft for 21 Aug 2026.

## Deliverable summary

- 2 new roles drafted, 16 new files rendered (8 deliverables x 2 roles), all present on disk.
- 2 new `applied-log.csv` rows appended (status `drafted`).
- 2 new Notion rows created via `create-pages` (confirmed via tool return value; SQL re-query blocked by quota, see above).
- 32 existing CSV rows corrected to match Notion during reconciliation.
- CSV drafted-row count: 1 (Amprion Werkstudent KI, unchanged) + 2 new = 3. Notion drafted-row count: 4 at start + 2 new = 6 (the 3-row discrepancy versus CSV's 3 is exactly the 3 orphaned rows flagged above, which have no CSV mirror).
