# Job Digest, 24 August 2026 (Cowork Scheduled Run)

## Run type and render toolchain

Scheduled Agent A (Cowork Drafting Agent) run. Render toolchain installed
clean: `weasyprint 69.0`, `python-docx`, `pypdf` all imported successfully
at Step 0. No fallback to Markdown-only output was needed.

## Backlog gate result

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **9**
rows in Status = 'drafted' at run start. This is authoritative per the
14 July 2026 rule (no Notion error, so no CSV fallback needed). 9 falls in
the **8 to 10 tier** under the 28 July 2026 yield reset gate, which caps
this run at the **top 3** newly scored roles. Ran steps 3 through 6 as
normal (not the 11+ hard pause).

## UPDATE (after this run): merge conflict revealed 4 of 9 were real, not orphaned

At the time this run started, the local checkout was cloned from a stale
`main` — a same-day run (23 Aug) had drafted 4 real roles and pushed to
`main` after this session's clone but before this session finished. A
merge conflict surfaced when reconciling this run's branch with `main`
after the fact, which corrected the finding below: **ADAC, Rosenberger
Hochfrequenztechnik, DELO Industrie Klebstoffe, and nerou GmbH DO have
real rendered deliverables** (confirmed via `role_configs_23aug.py` and
their 8 files each on `main`), and are genuinely applied-ready, not
orphaned. Merging `main` into this branch pulled that content in; CSV was
merged to keep both this run's 3 rows and the 23 Aug run's 9 rows.

**The remaining finding below still holds for 5 companies only**:
Boellhoff Gruppe, Anstalt fuer Kommunale Datenverarbeitung in Bayern
(AKDB), NewTec GmbH, Schaeffler Technologies, and logen.ai. These 5 still
have no draft folder anywhere in git history (checked again after the
merge with `main`) despite Notion showing them 'drafted' since 22 Aug.

## CRITICAL FINDING (corrected): 5 orphaned Notion "drafted" rows with no git content

Before drafting anything new, reconciliation surfaced a serious integrity
issue that Rah should investigate:

**5 pre-run Notion rows in Status = 'drafted' point to Draft Path
folders that do not exist anywhere in this git repository or its commit
history, even after merging in the 23 Aug run from `main`.** Companies
affected: Boellhoff Gruppe, Anstalt fuer Kommunale Datenverarbeitung in
Bayern (AKDB), NewTec GmbH, Schaeffler Technologies, logen.ai. All dated
22 August 2026 in Notion's Date Drafted field (the 23 Aug dated rows,
ADAC/Rosenberger/DELO/nerou, are confirmed real per the update above).

I verified these are real, currently live job postings (confirmed via
fresh StepStone/LinkedIn search results today), so this does not look like
fabricated data. The likely explanation is a prior Cowork run (22 Aug)
that created the Notion rows and then crashed, lost its worktree, or
failed to commit and push before completing steps 5 through 8 — leaving
Notion claiming "drafted" for roles that were never actually rendered or
committed anywhere.

Per invariant 2 (git is the source of truth for content) and invariant 3
(halting beats a false success), I did **NOT** mirror these 5 rows into
`applied-log.csv` — there is no real deliverable in this repo to point an
audit trail at, and doing so would fabricate evidence of drafts that don't
exist. I also did **NOT** modify or delete the Notion rows themselves;
Cowork's charter is to create new drafted rows, not alter existing ones,
and deleting data outside that scope risked destroying a legitimate record
if I'm wrong about the cause. **All 9 rows (the 5 still orphaned plus the
4 later confirmed real) counted toward the backlog gate's authoritative
Notion count** at run start (9, landing in the 8-10 cap tier), per the
standing rule that the Notion count is authoritative regardless of
anomalies underneath it.

**Recommended action for Rah:** decide whether to (a) re-run the drafting
pipeline for these 5 roles for real, or (b) manually flip their Notion
Status to something other than 'drafted' (e.g. a new "needs redraft" note)
so they stop inflating the backlog gate count on every future run.

## Reconciliation result

CSV vs Notion reconciliation (full 154-row CSV against all Notion rows,
company + role matched case-insensitively) found:

- **6 real drift rows**, all CSV showing `drafted` while Notion showed
  `applied` — confirmed genuine because all 6 have complete rendered
  deliverables on disk (CV + CL in md/html/pdf/docx). CSV updated to match
  Notion (Notion is the status source of truth):
  - Amprion GmbH, Werkstudent KI Stellen-ID 7959 -> applied
  - BCG Platinion, Werkstudent AI und Data Analytics Energy Knowledge Management -> applied
  - Arthrex GmbH, Working Student Business Analytics and Process Optimization -> applied
  - Sana HR Solutions GmbH, Werkstudent Data Engineer -> applied
  - Robert Bosch GmbH, Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank -> applied
  - FLEX Capital Management GmbH, Werkstudent Data Science and AI -> applied

  (All 6 were evidently submitted by OpenClaw since the 21 August run.)

- **9 Notion-only rows found at run start, later resolved to 5 truly
  orphaned + 4 confirmed real**: see Update and Critical Finding above.
  The 5 still-orphaned rows were not mirrored to CSV; the 4 confirmed
  real rows (ADAC, Rosenberger, DELO, nerou) arrived via the post-run
  merge with `main`, which already had their CSV rows and deliverables.

- No CSV rows were found missing a Notion counterpart (the one apparent
  mismatch, Ärzteverband Deutscher Allergologen, was a Unicode normalization
  artifact in my matching script, not a real drift).

CSV drafted count after reconciliation and before this run's new drafts:
**0**. After this run's 3 new drafts: **3** (matching this run's Notion
adds).

## Top cut, 3 new roles drafted

### 1. KPMG Deutschland — Werkstudent Business Intelligence und Analytics
- **Location:** Berlin. Start October 2026, 6 months.
- **Source:** LinkedIn, posted 3 days before this run.
- **Apply link:** https://de.linkedin.com/jobs/view/werkstudent-business-intelligence-analytics-m-w-d-at-kpmg-deutschland-4456001674
- **Apply method:** unconfirmed — LinkedIn posting, could be Easy Apply or
  redirect to KPMG's own careers portal; OpenClaw to classify at run time.
- **Language track:** DE (posting written in German). Requires "sehr gute
  Deutsch- und Englischkenntnisse" — above Rah's current B1 in progress,
  flagged transparently in the cover letter's closing paragraph.
- **Fit rationale:** internal Analytics team building SQL/Power BI
  dashboards and translating analyses into stakeholder insights — strong
  match for the Business Analyst / Data Analyst track.
- **Projects selected:** Fast Food Nutritional Analyzer and Meal Simulator
  (Tableau dashboards), Economic Impact Analysis of Global Climate Events
  (stakeholder-facing analytics pipeline).
- **Certs:** SAS Viya, Google Data Analytics, AWS Academy (BI-first order).
- **Deliverables:** all 8 rendered, CV 2 pages, validated clean.

### 2. MEAG MUNICH ERGO AssetManagement GmbH — Werkstudent Data Enablement
- **Location:** München, on-site presence required.
- **Source:** StepStone, posted 1 week before this run.
- **Apply link:** https://www.stepstone.de/stellenangebote--Werkstudent-Data-Enablement-mwd-Muenchen-MEAG-MUNICH-ERGO-AssetManagement-GmbH--14395291-inline.html
- **Apply method:** unconfirmed — page showed a disabled "Nicht verfügbar"
  apply control in the scraped snapshot; OpenClaw to classify at run time
  (may route to careers.munichre.com).
- **Language track:** DE (posting written in German). Requires German and
  English at minimum B2 — above Rah's current B1 in progress, flagged
  transparently in the cover letter.
- **Fit rationale:** Python/SQL data pipeline work, data governance tool
  evaluation, data policy documentation — strong Data Engineer /
  Data Analyst overlap.
- **Projects selected:** Real Time Flight Tracking Data Pipeline, Movie
  Analytics and ML Pipeline (schema enforcement, data governance angle).
- **Certs:** AWS Academy, SAS Viya, Google Data Analytics.
- **Deliverables:** all 8 rendered, CV 2 pages, validated clean.

### 3. Senacor Technologies AG — Masterarbeit, Datenstrategie und Kuenstliche Intelligenz
- **Location:** Berlin, Bonn, Frankfurt, Hamburg, München, Nürnberg, Wien
  (hybrid/DACH-wide, homeoffice possible, no relocation required).
- **Source:** StepStone, posted 3 days before this run.
- **Apply link:** https://www.stepstone.de/stellenangebote--Abschlussarbeit-im-Bereich-Datenstrategie-und-Kuenstliche-Intelligenz-Berlin-Bonn-Frankfurt-Hamburg-Muenchen-Nuernberg-Wien-Senacor-Technologies-AG--12683570-inline.html
- **Apply method:** unconfirmed — StepStone "Ich bin interessiert" quick
  apply control shown, but not confirmed platform-native vs redirect;
  OpenClaw to classify at run time.
- **Language track:** DE (posting written in German). Requires "sehr gute
  Deutschkenntnisse" (no English requirement stated) — above Rah's current
  B1 in progress, flagged transparently in the cover letter.
- **Fit rationale:** Masterarbeit researching data strategy and data
  integration as a precondition for KI adoption — direct match for the
  Master Thesis target category, and for the RAG/CreditIQ regulatory data
  strategy angle.
- **Projects selected:** Multi Agent RAG with LLM as Judge, CreditIQ
  Fairness by Design Credit Scoring (EU AI Act / GDPR regulatory data
  strategy angle).
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics.
- **Deliverables:** all 8 rendered, CV 2 pages, validated clean.

## Watchlist (scored but not drafted under the top-3 cap)

- ARAG, Werkstudent Data Engineering & Data Science, München (LinkedIn) —
  full job description could not be retrieved (LinkedIn login wall on
  this posting), held back pending a source that yields the full text.
- SAP, Working Student Data Analyst / Data Science, Walldorf (LinkedIn) —
  same LinkedIn login-wall issue; the scraped page also returned a
  mismatched location ("North Charleston, SC"), suggesting a scraping
  artifact worth re-checking on a future run rather than trusting blind.
- Forvis Mazars, Werkstudent Data Analytics / Python — full description
  not retrieved this run, held back.
- ZEISS, Internship Machine Learning, München — internship type
  (Pflichtpraktikum vs voluntary) not confirmed, held back pending
  verification.

## Dropped

None excluded under the Step 3 filters this run (no dual-study, Quereinsteiger,
or voluntary-internship listings surfaced in this run's search set).

## Transparency block

- **Sources reachable:** Tavily search (general web, StepStone-indexed,
  Xing-indexed, LinkedIn-indexed results all returned). Tavily extract
  (advanced depth) successfully pulled full StepStone job page content for
  MEAG and Senacor.
- **Sources unreachable:** Direct WebFetch to `linkedin.com` / any
  `*.linkedin.com` subdomain is blocked by this environment's network
  egress proxy (`EGRESS_BLOCKED`). Tavily extract on LinkedIn URLs mostly
  returned the anonymous login wall rather than the job description (KPMG's
  posting was the one exception where enough content rendered before the
  wall). This constrained today's candidate pool toward StepStone and the
  one LinkedIn listing where content was retrievable, and is why the
  ARAG and SAP LinkedIn leads landed on the watchlist instead of the top
  cut. No dedicated Indeed MCP tool was available in this session
  (deferred-tool search returned none); Indeed was not used this run
  (0 of the 1-per-run cap), consistent with the platform mix below.
- **Freshness dating notes:** all 3 drafted postings were dated by their
  source listing ("posted X days/week ago") at query time, 24 Aug 2026.
- **Prompt injection content observed:** none. Notion comment threads and
  job posting text were treated as data throughout; no instructions
  embedded in scraped content were followed.
- **Platform mix this run:** LinkedIn 1 (KPMG), StepStone 2 (MEAG,
  Senacor), Xing 0, Indeed 0, Company Page 0.
- **Distance was not a scoring factor**, per the standing rule; all 3
  roles are within Germany (geographic tier 1).

## Deliverable summary

- 3 new roles drafted, all 8 deliverables rendered and validated for each
  (24 files total): CV_Rahul_Rawat.{md,html,pdf,docx},
  CoverLetter_Rahul_Rawat.{md,html,pdf,docx}.
- All 3 CVs passed the 19 August 2026 validation gate: 2 pages, no banned
  strings (toward B2 / Databricks / Delta Lake / LangChain / PyTorch), no
  retired PERSONAL DETAILS-era strings on page 1, Ojas-style header
  confirmed (name, positioning tag, contact line 1 with email, contact
  line 2, italic status line).
- CSV: 6 rows reconciled from drafted to applied, 3 new drafted rows
  appended by this run. After merging in the 23 Aug run from `main`
  (see Update above), final CSV status counts on this branch: 76
  rejected, 59 applied, 18 Not listed Anymore, 1 shortlisted but no
  interview, 12 drafted (9 from the 22-23 Aug run, of which 4 are
  confirmed real and 5 remain orphaned per the corrected Critical
  Finding, plus this run's 3).
- Notion: 6 rows already correct (no action needed there, CSV was the lagging
  side), 3 new drafted rows created and verified present via follow-up
  query. Notion drafted total after this run: 12 (9 pre-existing — 4
  confirmed real, 5 still orphaned per the corrected finding above —
  plus this run's 3).
