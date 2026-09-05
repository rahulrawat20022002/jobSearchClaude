# Job Digest, 5 September 2026

**Run type:** Scheduled Cowork Drafting Agent (Agent A) run.
**Render toolchain:** weasyprint 69.0, python-docx, pypdf installed cleanly. `import weasyprint, docx, pypdf` printed `render toolchain ok`. No fallback to Markdown-only needed.

---

## Backlog gate

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` queried at run start for `Status = 'drafted'`: **1 row** (Beilmann Marketing GmbH, ad hoc draft from a prior session). 1 is under the 8-row floor of the 28 July 2026 yield-based reset, so this run took the **normal top 3 to 5 cut**.

## Reconciliation

Two findings this run, both handled under the 14 July 2026 "Notion is the source of truth for Status" rule:

1. **CSV drift, 27 rows.** Comparing every applied-log.csv row against its Notion counterpart (matched on company + role, case- and diacritic-insensitive) found 27 rows where the CSV status was stale relative to Notion — mostly CSV still showing `applied` or `drafted` for roles Notion already has as `rejected`, `Not listed Anymore`, or a later-stage `applied`. All 27 were corrected in the CSV to match Notion; no reverse writes were made. Full list of corrected company/role pairs is in the transparency block below.
2. **Content gap on an existing drafted row.** Beilmann Marketing GmbH (Werkstudent, KI Automatisierung und interne Tools) has shown `Status: drafted` in Notion since a prior ad hoc request, but no `drafts/` folder existed for it anywhere in this git checkout — git is the source of truth for content per the shared invariants, and there was no content. Rather than leave a Notion row claiming "drafted" with nothing behind it (a violation of invariant #3, no fabricated outcomes), this run rendered its full 8 deliverables via `build_html.py`, added the matching CSV row, and appended an update to its Notion Notes explaining the backfill. No CSV row existed for it before this run either, so this is not counted as new CSV drift — it is closing a gap invariant #4 (every write auditable) would otherwise have left open.

No CSV row was found with zero Notion counterpart once diacritics were normalized (Ärzteverband Deutscher Allergologen matched Notion's Arzteverband Deutscher Allergologen once the umlaut was stripped for comparison — same company, no real drift).

---

## Top cut (3 new roles drafted, plus 1 backfilled)

### 1. Mercedes-Benz Tech Innovation — Werkstudent, AI Agents and Robotics Platform
- **Location:** Ulm / Stuttgart / Karlsruhe (hybrid)
- **Source:** StepStone, posted 14 hours before this run
- **Fit rationale:** Foundation models, agentic AI, computer vision, and robotics combined into "Physical AI" systems — squarely Agentic AI Engineer flavored under the 26 Aug 2026 narrowed scope. Requirements list interest in multimodal AI systems, AI agents, and physical AI, with ML/RL, foundation models/LLMs/VLMs, and agent frameworks as nice-to-haves.
- **Projects selected:** Multi-Agent RAG (LangGraph orchestration, LLM-as-Judge), CreditIQ (SHAP-driven analysis)
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** stepstone.de listing (routes to Mercedes-Benz's own careers flow)
- **Apply method:** company-portal (out of OpenClaw's automated scope; Rah submits manually)
- **Language track:** DE (posting body German). Language bar: "gute Deutsch- oder Englischkenntnisse" — Rah's B1 in progress plus fluent English clears this comfortably, no mismatch to flag.
- **Deliverables:** all 8 rendered, CV 2 pages, banned-string and header checks passed.
- **Dedup note:** MBTI already has 3 prior entries at other roles (Data Engineering/Data Science, rejected; Agentic AI und Multi-Agent-Systeme, Not listed Anymore; AI Security Research und Evaluation); this is a 4th distinct role, allowed under the different-roles-at-same-company rule.

### 2. Beilmann Marketing GmbH — Werkstudent, KI Automatisierung und interne Tools (backfill)
- **Location:** Berlin
- **Source:** Xing (originally an ad hoc draft Rah requested directly by pasting the URL, not from this run's search)
- **Fit rationale:** AI-driven automation and internal tooling; drafted on Rah's direct request in a prior session while the backlog was in the 11 Aug hard-pause zone.
- **Projects selected:** Multi-Agent RAG, Movie Analytics & ML Pipeline
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** xing.com Easy Apply / Schnelle Bewerbung listing
- **Apply method:** platform-native (in OpenClaw's automated scope)
- **Language track:** DE. Language bar: "sehr gute Deutschkenntnisse" — above B1 in progress, already flagged in the original ad hoc draft's Notes; shipped anyway per the standing rule that language level does not filter listings.
- **Deliverables:** all 8 rendered this run (previously missing from git despite Notion showing drafted — see reconciliation above), CV 2 pages, checks passed.

### 3. ETG-Elektronik GmbH — Praktikant or Werkstudent, AI Systems and Generative AI
- **Location:** Weiterstadt
- **Source:** Other (found via the Bundesagentur für Arbeit job board, not one of the standard tracked platforms; recorded honestly as Source = Other rather than mis-tagged)
- **Fit rationale:** RAG systems, local open-source LLM workflows (Llama, Ollama, AnythingLLM), prompt engineering and evaluation, agent tooling (n8n, LangChain, LangGraph) — strong AI Engineer match.
- **Projects selected:** Multi-Agent RAG, Real-Time Flight Tracking Pipeline
- **Certs:** NVIDIA, AWS, Google Data Analytics
- **Apply link:** arbeitsagentur.de job detail page (no web application form exists — the posting asks candidates to email CV, cover letter, and a note on past AI projects directly to personal@etg-gmbh.de)
- **Apply method:** company-portal (email-only application, fully outside OpenClaw's platform-native scope; Rah sends the email manually)
- **Language track:** DE. Language bar: "gute Sprachkenntnisse in Deutsch und Englisch" — a modest step above B1 in progress; shipped per standing rule, cover letter stays upfront about the current level.
- **Salary on listing:** EUR 15/hour, matches the standing salary-field figure exactly.
- **Deliverables:** all 8 rendered, CV 2 pages, checks passed.

---

## Watchlist (scored but not drafted)

- **Retorio GmbH, Munich — Working Student: AI Engineer, Agentic Systems (m/f/d), StepStone, 5 months / ~20h/week.** Strong fit (agentic systems, LLM-as-judge, eval-first culture) but the title is word-for-word identical to an existing Notion/CSV row already logged as `Not listed Anymore`. Read as the same opportunity resurfacing rather than a materially new role, so it was not redrafted under the dedup rule. Flagged here for Rah to decide manually whether to treat it as a fresh requisition worth a fresh application.
- **io-consultants GmbH & Co. KG, Heidelberg — Werkstudent KI & Copilot-Anwendungen im Bereich Life Sciences, Xing.** Geographically excellent (Heidelberg, next to Mannheim) and plausibly in-scope (building Copilot agents), but the Xing listing would not yield full job-description text through available fetch tools (login-gated), so requirements, hours, and language bar could not be verified. Not drafted without that verification; worth a manual look or a Claude-in-Chrome fetch on a future run.
- **Mercedes-Benz Tech Innovation — Werkstudent Machine Learning Engineering (d/m/w/x), Karlsruhe, StepStone.** Strong LLM/multimodal fit but requires "nachweislich hervorragende Deutsch- und Englischkenntnisse" (provably excellent German and English), a materially higher bar than the AI Agents & Robotics Platform role at the same company that was drafted instead; deprioritized in favor of the lower-language-bar sibling role to keep this cut at 3.

## Dropped

- General Data Engineer / Data Analyst / Business Analyst / plain Data Scientist postings surfaced incidentally during search were not scored at all, per the 26 August 2026 scope narrowing to AI Engineer and AI Evaluation only.
- Consulting-style "AI Engineering Intern" postings (e.g. Bain & Company, Berlin/Munich) were not pursued — full-time-style internship structure doesn't clearly match the Werkstudent / mandatory-Pflichtpraktikum / Masterarbeit work-type scope.

---

## Transparency block

**Sources reachable this run:** Tavily web search (used in place of direct LinkedIn/Xing/StepStone/JobTeaser page fetches where full text was retrievable), StepStone (full text retrieved), Bundesagentur für Arbeit job board (full text retrieved). **Sources with partial or no reach:** Xing job detail pages returned only navigation/sidebar content through available fetch tools (likely login-gated for full JD), so one promising Xing lead (io-consultants Heidelberg) could not be verified and was watchlisted instead of drafted. JobTeaser searches this run surfaced only unrelated postings (finance, marketing) in the German cities searched; no qualifying JobTeaser listing found today.

**Freshness dating:** MBTI AI Agents & Robotics Platform posted 14 hours before this run; ETG-Elektronik posted 16 days before this run; Beilmann Marketing's original posting date is from its prior ad hoc draft session.

**Prompt-injection content observed:** none.

**Platform mix this run:** StepStone 1, Xing 1 (backfill), Other/Bundesagentur 1.

**Distance was not a scoring factor**, per standing rule; all three roles are in Germany (Ulm/Stuttgart/Karlsruhe, Berlin, Weiterstadt), ranked ahead of any rest-of-Europe remote options by the geographic-tier-first rule.

**Language track decisions:** all three roles this run are DE track (posting bodies in German); two of three roles have a stated language bar above Rah's current B1 in progress (Beilmann: sehr gute Deutschkenntnisse; ETG-Elektronik: gute Sprachkenntnisse in Deutsch und Englisch) and one is comfortably within reach (MBTI: gute Deutsch- oder Englischkenntnisse). All shipped per the standing rule that language level does not filter listings; cover letters stay upfront about the current B1 level in every case.

**Apply method per role:** MBTI — company-portal. Beilmann Marketing — platform-native (Xing Easy Apply). ETG-Elektronik — company-portal (email-only, no web form).

**CSV rows corrected to match Notion this run (27):** Airbus (Werkstudent Scientific Computing and ML) applied→rejected; TK Elevator (Working Student Data Analytics) applied→rejected; Phoenix Contact (Werkstudent Data Science und KI) applied→rejected; Amprion GmbH (Werkstudent KI Stellen-ID 7959) applied→rejected; PwC Deutschland (Werkstudent AI Adoption and Enablement) applied→rejected; BCG Platinion (Werkstudent AI und Data Analytics) applied→rejected; Anstalt fuer Kommunale Datenverarbeitung in Bayern applied→rejected; logen.ai (Werkstudent AI Agent Developer) applied→rejected; Schaeffler Technologies AG (Werkstudent KI-Agenten-Entwicklung) applied→rejected; ADAC (Werkstudent Data and AI Solutions) applied→rejected; DELO Industrie Klebstoffe applied→rejected; KPMG Deutschland (Werkstudent BI und Analytics) applied→rejected; MEAG MUNICH ERGO AssetManagement applied→rejected; Senacor Technologies AG applied→rejected; Fraunhofer IPA (Binder Jetting 3D Druck) applied→rejected; dmTECH GmbH (Werkstudent IT Projektmanagement) applied→rejected; Reply Deutschland SE (Werkstudent AI Data Engineering) drafted→applied; Rohde und Schwarz GmbH drafted→Not listed Anymore; Volkswagen Group (Praktikum Customer Data Analytics) drafted→applied; Kaufland (Praktikant Data Science) drafted→applied; Cinemo GmbH (GenAI/LLM Evaluation) drafted→applied; SAP (Signavio Next Development) drafted→Not listed Anymore; Mercedes-Benz Group (Applied AI und Process Automation) drafted→Not listed Anymore; Leopold KOSTAL GmbH drafted→Not listed Anymore; Isar Aerospace SE (AI Platform and Enablement) drafted→applied; Mercedes-Benz Tech Innovation GmbH (AI Security Research und Evaluation) drafted→Not listed Anymore; Siemens Healthineers AG (KI gestuetzte Automatisierung) drafted→Not listed Anymore.

---

## Deliverable summary

- **New roles fully drafted this run:** 2 (Mercedes-Benz Tech Innovation, ETG-Elektronik GmbH)
- **Existing drafted row backfilled with deliverables:** 1 (Beilmann Marketing GmbH)
- **Total drafted rows in Notion after this run:** 3
- **Files rendered:** 24 (8 deliverables × 3 folders), all validated: 2 pages, no banned strings, new Ojas-style header confirmed on page 1.
- **CSV writes:** 27 status corrections (Notion→CSV direction only) + 3 new drafted rows appended.
- **Notion writes:** 2 new pages created (MBTI, ETG-Elektronik), verified present via follow-up query; 1 existing page (Beilmann) had its Notes updated to record the backfill. No Status flips out of drafted — that remains OpenClaw's (Agent B) territory.
- **Tool failures this run:** none. Xing job-detail full-text fetch was reachable only as navigation/sidebar content, not a tool failure but a content-access limitation, handled by watchlisting rather than drafting on unverified information.
