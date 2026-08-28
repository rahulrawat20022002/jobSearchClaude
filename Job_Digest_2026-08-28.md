# Job Digest, 28 August 2026 (Scheduled Cowork Run)

## Run type and render toolchain

Scheduled Cowork Agent A run. Render toolchain installed clean:
`pip install weasyprint python-docx pypdf` succeeded, `import weasyprint,
docx, pypdf` printed `render toolchain ok 69.0`. No fallback to Markdown
only was needed.

## Backlog gate result

Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` returned **8**
rows with Status = `drafted` at run start. Under the 28 July 2026 yield
reset gate, 8 to 10 drafted caps the run at the **top 3** newly scored
roles (not the normal top 3 to 5). Backlog after this run: **11** drafted
in Notion (8 + 3 new).

## Reconciliation result: drift found and fixed

Reconciliation surfaced a real gap, not just a status mismatch. Four rows
that already showed `drafted` in Notion (Cinemo GmbH, Leopold KOSTAL,
SAP Signavio, Mercedes-Benz Group Applied AI und Process Automation) had
**no corresponding files anywhere in this checkout's git history on
`main`** — the applied-log.csv rows, the digest, and all 32 rendered
deliverable files for those 4 roles existed only on an unmerged branch,
`claude/adoring-dijkstra-lnbu2v`, from a run on 27 August 2026 that never
got merged (commit `a44cf20`, "Scheduled run 2026-08-27, 4 new drafts").

Per invariant #2 (git is the source of truth for content) and invariant
#3 (never fabricate an outcome, halting beats a false success), this was
treated as a real, previously-completed run whose output simply never
reached `main`, not as work to redo. The commit was a clean fast-forward
from this branch's prior head, so it was merged in directly (no conflict,
no rewritten history) before any of today's new work began. After the
merge, a full CSV-vs-Notion diff across all 180 CSV rows and 181 Notion
rows at that point found **zero further Status drift**; the only
remaining non-match was a harmless umlaut normalisation artefact
(`Ärzteverband` vs `Arzteverband`) where both sides already agreed on
`applied`.

**Action for Rah:** the 27 August run's PR/branch merge step appears to
have silently not completed that day. Worth checking whether the
auto-merge step in CLAUDE.md step 8 is firing reliably on every run.

## Top cut (3 new drafts, capped run)

### 1. Isar Aerospace SE — Working Student, AI Platform and Enablement
- **Location:** Parsdorf, Bavaria (hybrid)
- **Source:** Company Page (Greenhouse job board, found via general web
  search), posted 6 days before this run
- **Fit rationale:** operates and evaluates a self managed open source
  model inference stack, agentic tooling, and MCP server integration —
  a strong AI Engineer match under the 26 August 2026 scope narrowing.
- **Projects selected:** Multi Agent RAG (LLM as Judge, local Ollama
  inference), Movie Analytics and ML Pipeline (fully automated Cloud Run
  batch pipeline)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Language track:** EN (posting body in English, no German requirement)
- **Apply link:** https://job-boards.eu.greenhouse.io/isaraerospace/jobs/4958455101
- **Apply method:** company-portal (Greenhouse on isaraerospace.com) —
  out of OpenClaw's platform-native scope, Rah submits manually
- **Deliverables:** all 8 rendered, CV 2 pages

### 2. Mercedes-Benz Tech Innovation GmbH — Werkstudent AI Security, Research und Evaluation
- **Location:** Ulm, Karlsruhe, Stuttgart, Berlin (hybrid, 4 locations)
- **Source:** LinkedIn, posted about 1 week before this run
- **Fit rationale:** explicitly evaluation flavored — "Analyse und
  Bewertung moderner KI-Modelle", automated evaluation methods for AI
  system security. Directly maps to the RAG project's LLM as Judge
  harness and CreditIQ's SHAP based vulnerability analysis. Strong AI
  Evaluation match.
- **Projects selected:** Multi Agent RAG (LLM as Judge evaluation),
  CreditIQ (SHAP subgroup vulnerability analysis)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Language track:** DE (posting body in German)
- **Language level flag:** posting demands "nachweislich hervorragende
  Deutsch- und Englischkenntnisse" (provably excellent German AND
  English) — materially above Rah's current B1 in progress level. The
  cover letter is upfront about this gap rather than papering over it.
- **Apply link:** https://de.linkedin.com/jobs/view/werkstudent-ai-security-research-evaluation-d-m-w-x-at-mercedes-benz-tech-innovation-4446792270
- **Apply method:** company-portal (application flow believed to route
  to MBTI's own Workday portal, req R0006827) — out of OpenClaw scope,
  Rah submits manually
- **Deliverables:** all 8 rendered, CV 2 pages

### 3. Siemens Healthineers AG — Werkstudent KI gestuetzte Automatisierung bei Research und Development
- **Location:** Kemnath (hybrid, up to 60% mobile within Germany)
- **Source:** LinkedIn (full JD text confirmed via jobs.siemens.com
  mirror), posted 23 August 2026, 5 days before this run
- **Fit rationale:** evaluating AI tools (Microsoft 365 Copilot, GitHub
  Copilot, Claude Code) in real development workflows, scripting
  automation into toolchains. Fits AI Engineer scope; requires critical
  evaluation of AI generated output.
- **Projects selected:** Multi Agent RAG (agentic system, critical
  evaluation habits), Movie Analytics and ML Pipeline (Python automation
  wired into a toolchain)
- **Certs:** NVIDIA, AWS Academy, Google Data Analytics
- **Language track:** DE (posting body in German)
- **Language level note:** posting only requires "sehr gute
  Englischkenntnisse, Deutsch ist von Vorteil" (German is a plus, not
  required) — no mismatch despite the DE track.
- **Apply link:** https://jobs.siemens.com/en_US/externaljobs/JobDetail/518932
- **Apply method:** company-portal (jobs.siemens.com) — out of
  OpenClaw scope, Rah submits manually
- **Deliverables:** all 8 rendered, CV 2 pages

## Watchlist (scored but not drafted under the top 3 cap)

- **Mercedes-Benz Group, Student\*in fuer Masterarbeit, Agentic AI in
  der CarIT Security** (Sindelfingen). Real posting (Stellennummer
  MER00046QC, deadline 2 Oct 2026), Master Thesis work type, agentic AI
  for automotive cybersecurity knowledge work. Passed over in favor of
  the more explicitly evaluation-flavored MBTI AI Security role above,
  and because the pulled JD text (via jobs.help and BeBee mirrors) never
  yielded the actual "Aufgaben" and "Qualifikationen" body text — only
  the department and scope summary. Worth a second pass next run if the
  full JD becomes fetchable, since a Masterarbeit is a more durable
  engagement than another Werkstudent role.
- **Siemens AG, Werkstudent AI Strategy & Program Steering** (Stuttgart,
  Mercedes-Benz Tech Innovation adjacent listing surfaced in the same
  search). Not pulled in detail this run; strategy/steering framing
  reads more PM than AI Engineer, likely out of the 26 August scope
  narrowing on closer read.

## Dropped this run

- None dropped outright; all candidates surfaced this run either made
  the top 3 or are noted on the watchlist above pending a fuller JD pull.

## Transparency block

- **Sources reachable this run:** Tavily general web search (used for
  LinkedIn, Xing, StepStone, JobTeaser, and company career page
  discovery, per the standing search source list), Tavily extract for
  full JD text on several candidate postings.
- **Sources not directly queried this run:** Indeed MCP is not present
  in this environment's tool set; Indeed was not used this run (0 of 3,
  well under the 1-per-run cap, no yield impact).
- **Freshness dating:** all three postings dated from source metadata
  (Isar Aerospace "Posted 6 days ago" on LinuxCareers mirror, MBTI
  "Vor 1 Woche" on LinkedIn, Siemens Healthineers "Posted since
  23-Aug-2026" on jobs.siemens.com).
- **Prompt injection content observed but not acted on:** none observed
  in any fetched job posting content this run.
- **Platform mix this run:** Company Page 1 (Isar Aerospace via
  Greenhouse), LinkedIn 2 (MBTI, Siemens Healthineers).
- **Distance was not a scoring factor**, per standing rule; all three
  roles are within Germany (Bavaria and Baden-Wuerttemberg), the single
  top geographic tier.
- **Target role scope:** all three roles scored and drafted fall inside
  the 26 August 2026 narrowing to AI Engineer and AI Evaluation only.

## Deliverable summary

- 3 new roles drafted, 24 new files rendered (8 deliverables x 3 roles),
  all validated: 2 pages, banned strings absent, retired PERSONAL DETAILS
  strings absent.
- CSV: 3 rows appended (184 total lines including header).
- Notion: 3 new pages created under data source
  `fd974369-40b2-48c5-b660-d15256c88f52`, verified by follow-up query
  showing 11 drafted rows (was 8).
- Reconciliation recovered 4 previously-drafted roles from an unmerged
  branch (see Reconciliation section above) — no new deliverables
  rendered for those 4, their files already existed complete on that
  branch and are now on `main`.
