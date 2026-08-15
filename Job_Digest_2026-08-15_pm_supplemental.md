# Job Digest Supplemental — 15 August 2026 (Scheduled Afternoon Run)

**Run type:** Scheduled task run, third invocation of the day. Cowork MCP context, Notion and Tavily reachable, Gmail draft created.
**Status:** RAN NORMAL top 3 cut. 3 new roles drafted.

---

## Backlog gate result

Per the 14 July 2026 status source of truth override and the 28 July 2026 yield based reset rule:

- Notion data source fd974369-40b2-48c5-b660-d15256c88f52 queried directly at run start.
- Drafted count in Notion at run start: **5** rows (Retorio, AssetMetrix GmbH, Phoenix Contact, BSH Home Appliances Group, viadee Unternehmensberatung AG — all from the earlier 15 August run).
- Rah manually flipped 7 rows from the morning supplemental's 12 drafted to applied since then, dropping the backlog to 5.
- 5 is below the 8 row soft cap and the 11 row hard pause. Normal top 3 to 5 cut applies.
- Cut set to 3 this run to preserve a controlled backlog while Rah works through the current 5 drafted and the 3 newly drafted after this run (total 8, still under the soft cap).
- Fallback path: CSV drafted count also confirmed at 5 pre-append, in sync with Notion.

## Reconciliation step

Per the 11 July 2026 rule.

- Read applied-log.csv in full (137 rows before append).
- Queried Notion data source for every row and compared statuses.
- Drift found and fixed: **HDI AG Werkstudent Data Engineering und Analytics im Aktuariat** showed `Not listed Anymore` in the CSV but `applied` in Notion. Notion is the source of truth per the 14 July 2026 rule, so the CSV row was updated to `applied`.
- No other CSV to Notion drift on statuses this run.
- No CSV rows missing a Notion counterpart.

---

## Top Cut — 3 Roles Drafted

Ordering per 12 July 2026 priority rule (freshness first, then role type, then Best for overlap) inside the single Germany geographic tier.

### 1. BMW Group — Werkstudent Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse
**Location:** Muenchen, hybrid, Teilzeit
**Source:** BMW Career Page (bmwgroup.jobs)
**Posting freshness date used:** 13 August 2026 (posted ~2 days ago as of run time)
**German level required:** Not stated, posting body in German
**Language track:** German (posting body in German, per 20 July 2026 language match hard rule)
**Apply method:** Company portal (bmwgroup.jobs) — Rah applies manually per the 13 August 2026 auto-apply rule
**Apply link:** https://www.bmwgroup.jobs/de/de/jobfinder.html?query=Werkstudent+Data+Science+KI+Tool+Qualitaetsanalyse
**Draft path:** drafts/BMW Muenchen Werkstudent Data Science KI Tool Qualitaetsanalyse/
**Deliverables:** CV_Rahul_Rawat.md, CV_Rahul_Rawat.docx, CV_Rahul_Rawat.html, CV_Rahul_Rawat.pdf, CoverLetter_Rahul_Rawat.md, CoverLetter_Rahul_Rawat.docx, CoverLetter_Rahul_Rawat.pdf — all seven rendered ok, PDF fit 3 pages after auto trim to 1 Personal Projects entry
**Fit rationale:** BMW is running an AI tool development role squarely inside a quality analysis workflow. My Multi Agent RAG project shows evaluation harness discipline for LLM tooling, and CreditIQ demonstrates SHAP driven analysis. eRay GmbH forecasting work adds honest quantitative evaluation credibility.
**Projects selected:** #1 Multi-Agent RAG (primary), #2 CreditIQ (trimmed to 1 by overflow ladder)
**Certifications:** NVIDIA LLM (lead), AWS Cloud Foundations, Google Data Analytics
**Timing:** message today (15 August), apply 17 August per 28 July 2026 warm outreach rule
**LinkedIn outreach:** no clear contact this run (BMW quality team names not surfaced via Tavily in the automated run without a browser session; adding a contact requires interactive LinkedIn access)

### 2. KfW Bankengruppe — Werkstudent im Bereich IT, Data Science und KI
**Location:** Frankfurt am Main, hybrid, Teilzeit
**Source:** Xing
**Posting freshness date used:** 13 August 2026 (posted 2 days ago as of run time)
**German level required:** Not stated explicitly, posting body in German, KfW is a German public bank
**Language track:** German (posting body in German)
**Apply method:** Platform-native (Xing Schnelle Bewerbung) — Auto-submit pending, tooling not wired yet
**Apply link:** https://www.xing.com/jobs/frankfurt-main-werkstudent-it-data-science-ki
**Draft path:** drafts/KfW Bankengruppe Frankfurt Werkstudent IT Data Science KI/
**Deliverables:** all seven rendered ok, PDF fit 3 pages after auto trim to 1 Personal Projects entry
**Fit rationale:** KfW is a regulated financial services environment where CreditIQ's fairness by design pattern lands directly. Multi Agent RAG shows evaluation harness discipline for LLM tooling under regulator scrutiny. eRay GmbH gives production ML credibility.
**Projects selected:** #2 CreditIQ (primary), #1 Multi-Agent RAG (trimmed to 1 by overflow ladder)
**Certifications:** NVIDIA LLM (lead), AWS Cloud Foundations, Google Data Analytics
**Timing:** message today (15 August), apply 17 August
**LinkedIn outreach:** no clear contact this run

### 3. Allianz Insurance — Working Student, Data Science
**Location:** Munich, hybrid, Teilzeit
**Source:** Xing
**Posting freshness date used:** 12 August 2026 (posted 3 days ago as of run time)
**German level required:** Not stated (posting listed as m/f/d with English title)
**Language track:** English (posting body in English, per 20 July 2026 language match hard rule; Allianz Insurance uses English for cross-border DS teams)
**Apply method:** Platform-native (Xing) — Auto-submit pending, tooling not wired yet
**Apply link:** https://www.xing.com/jobs/muenchen-working-student-data-science
**Draft path:** drafts/Allianz Insurance Muenchen Working Student Data Science/
**Deliverables:** all seven rendered ok, PDF fit 3 pages after auto trim to 1 Personal Projects entry
**Fit rationale:** Insurance risk modelling is downstream of the same fairness by design credit scoring pattern I built in CreditIQ. Multi Agent RAG shows evaluation harness discipline. eRay GmbH forecasting adds production ML credibility.
**Projects selected:** #2 CreditIQ (primary), #1 Multi-Agent RAG (trimmed to 1 by overflow ladder)
**Certifications:** NVIDIA LLM (lead), AWS Cloud Foundations, Google Data Analytics
**Timing:** message today (15 August), apply 17 August
**LinkedIn outreach:** no clear contact this run
**Dedup note:** Distinct from the existing Allianz Versicherungs-AG "Werkstudent Data Analyst" applied row per the "different roles at the same company" rule; sister entity, different team, different role.

---

## Watchlist (not drafted this run, considered)

- **Fraunhofer IIS Erlangen — Werkstudent Data Science und Natural Language Processing.** Attractive NLP fit, but Fraunhofer IIS has two prior rejected rows in the log for adjacent roles (audio compression, simulation/robotics). Left off the top cut this run to avoid piling more rejections on the same institute; will reconsider on a run where alternatives are thinner.
- **Meierhofer Berlin — Werkstudent Data Science / Business Intelligence.** StepStone, posted 3 days ago, healthcare BI focus. Left off because the top 3 cut was full; will consider on the next run to lift the StepStone share.
- **statworx Frankfurt — Werkstudent AI Education.** Xing, posted 3 days ago. Non-core fit (education rather than build), left off.
- **BMW AG — Werkstudent Data, Analytics AI im Einkauf (Muenchen).** BMW career page, fresh. Left off because a stronger BMW role (Data Science und KI Tool Qualitaetsanalyse) was already picked in the top 3 and stacking two BMW roles in one run is not the mix pattern.

## Dropped (filter rejects, not scored)

- Multiple Duales Studium / dual study listings (dropped per master-projects.md filter).
- Senior Data Scientist, Head of Analytics, Principal roles (dropped per work type filter: not Werkstudent / Praktikum / Master Thesis).
- Consulting Manager / Account Executive roles (dropped for work type).

---

## Transparency block

- **Backlog gate:** 5 drafted rows in Notion at run start (source of truth per 14 July 2026 rule), CSV in agreement. Under 8 = normal cut. Cut set to 3 rather than 5 to keep post-run backlog at 8 exactly, still at the soft cap boundary.
- **Reconciliation:** 1 CSV drift fixed (HDI AG status flipped from `Not listed Anymore` to `applied` to match Notion).
- **Source reachability this run:**
  - Notion: reachable, dual write successful for all 3 rows.
  - Tavily: reachable, used for StepStone, Xing, and career page sweeps.
  - LinkedIn: not sourced this run (already covered by earlier 15 August run with 4 LinkedIn drafts; login-walled for contact sourcing in automated context).
  - Indeed: not sourced this run (background weight per 28 July 2026 yield reset).
  - Gmail: reachable, digest draft created.
- **Platform breakdown for top 3 this run:** BMW Career Page 1, Xing 2, StepStone 0, LinkedIn 0, Indeed 0. Combined with the earlier 15 August run: LinkedIn 4, Xing 3, BMW Career Page 1, StepStone 0, Indeed 0. Total for the day: 8 drafts across 3 platforms. StepStone shortfall carries to the next run per the redistribution rule.
- **Language track decisions:** BMW = DE (posting body in German), KfW = DE (German bank, posting body in German), Allianz Insurance = EN (posting body in English, m/f/d title). All three verified via posting body language per the 20 July 2026 language match hard rule.
- **Render toolchain:** WeasyPrint 69.0 installed cleanly, all 3 CVs fit within the 3 A4 page hard cap after the overflow ladder trimmed each to 1 Personal Projects entry with 3 bullets. All 3 cover letters fit 1 A4 page on the default CL CSS without needing the tight variant.
- **Notion schema note:** The 13 August 2026 rule prescribes an `Apply Method` column with values `platform-native` and `company-portal`. That column does not yet exist on the Notion data source (attempted write returned validation_error). Recorded the Apply Method inside the Notes field on each new row as a fallback. Suggest Rah adds an `Apply Method` select column to the Notion database with those two options.
- **Auto-submit pending:** 2 of the 3 rows drafted this run are platform-native (KfW on Xing, Allianz on Xing). Per the 13 August 2026 auto-apply rule, both should ideally auto-submit, but the tooling is not yet wired for Xing in the pipeline. Both listed here so Rah can batch-submit later. BMW is company-portal, Rah applies manually as usual.

---

## Backlog after this run

Notion drafted rows expected after this run: 5 existing + 3 new = **8 drafted**. This lands exactly at the soft cap boundary. If Rah does not clear at least 1 drafted row before the next scheduled run, the next run caps at top 3 again per the 28 July 2026 gate. If backlog reaches 11 the next run hard-pauses.

Existing 5 drafted rows Rah still needs to apply to from the earlier 15 August run:

| Company | Role | Location | Source | Draft folder |
|---|---|---|---|---|
| Retorio | Working Student, AI Engineer Agentic Systems | Munich | LinkedIn | drafts/Retorio Munich Working Student AI Engineer Agentic Systems/ |
| AssetMetrix GmbH | Working Student, AI Engineering | Munich | LinkedIn | drafts/AssetMetrix GmbH Munich Working Student AI Engineering/ |
| Phoenix Contact | Werkstudent, Data Science und KI | Blomberg | LinkedIn | drafts/Phoenix Contact Blomberg Werkstudent Data Science AI/ |
| BSH Home Appliances Group | Working Student, Engineering Data Analytics and Classification | Munich | LinkedIn | drafts/BSH Home Appliances Munich Working Student Data Analytics Classification/ |
| viadee Unternehmensberatung AG | Werkstudent, Data Science und Process Mining | Koeln | Xing | drafts/viadee Unternehmensberatung Koeln Werkstudent Data Science Process Mining/ |

New 3 drafted rows from this run (per top cut above): BMW Group, KfW Bankengruppe, Allianz Insurance.
