# Pipeline Overview

The job-search pipeline splits work across three actors. Each has a well defined lane and is forbidden from touching the other lanes. This is the single most important thing to keep straight when reading any digest.

![[pipeline_diagram.png]]

## The three actors

| Actor | Where it runs | What it owns | Never touches |
|---|---|---|---|
| [[01 Agent A - Cowork Drafting]] | Cloud sandbox, on a schedule | Search, score, tailor, render, `applied-log.csv` writes, new Notion rows in status `drafted`, git commits and pushes | Notion status flips out of `drafted`, `Date Applied`, LinkedIn compose windows, the local Mac checkout |
| [[02 Agent B - OpenClaw Submission]] | Rah's Mac, on demand | Open Apply Link, upload CV+CL, submit, verify, flip Notion `drafted → applied`, set `Date Applied`, paste LinkedIn outreach | CLAUDE.md, master-projects.md, `applied-log.csv`, files under `drafts/`, `git commit`, `git push` |
| [[03 Rah Manual - Company Portals]] | Rah's browser, by hand | Every submission to a company-owned careers domain (SAP, BMW, Siemens, BSH, and any other) | Nothing scoped in for the agents; this lane exists precisely because the agents will not go here |

## The one-way flow

1. Agent A picks new roles from LinkedIn, career pages, StepStone, Xing, Indeed. Scores them. Tailors CV and cover letter per role. Renders eight deliverables per role into `drafts/[folder]/`. Writes the row to Notion in status `drafted`. Appends it to `applied-log.csv`. Commits and pushes.
2. Rah reads the daily Gmail digest, decides which roles to actually submit.
3. For platform native listings (LinkedIn Easy Apply, Xing Schnelle Bewerbung, StepStone Schnelle Bewerbung, Indeed Easy Apply) → Rah fires OpenClaw and Agent B submits them.
4. For company portal listings (careers.bmwgroup.jobs, jobs.sap.com, jobs.siemens.com, careers.bshgroup.com, any other company-owned careers domain) → Rah submits manually. OpenClaw explicitly skips these with the note `company-portal, Rah to submit manually`.

## The four shared invariants (unbreakable)

1. **Notion is the source of truth for row status.** CSV mirrors Notion, never the reverse.
2. **Git is the source of truth for content.** Local Desktop and `/tmp` checkouts are working copies.
3. **Never fabricate an outcome.** Halting is always better than a false `applied` or `drafted` flag.
4. **Every write must be auditable.** No confirmation string → no write.

Two more that behave like invariants: never send a LinkedIn message automatically ([[02 Agent B - OpenClaw Submission]] pastes and stops), and never enter passwords or salary numbers ([[02 Agent B - OpenClaw Submission]] uses 15 EUR/hour when required).

## When each agent decides "not my job"

- Agent A never submits, never opens portals, never touches Notion Status past `drafted`.
- Agent B never commits or pushes; if it accidentally touches a tracked file, it halts.
- Both agents skip company portal listings entirely and leave them for Rah.

## See also

- [[19 August 2026 Rules]] for the current CV shape
- [[Notion Schema]] for column names both agents must respect
- [[Daily Workflow]] for how a normal day flows through this
