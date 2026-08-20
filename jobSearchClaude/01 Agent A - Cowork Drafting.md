# Agent A, the Cowork Drafting Agent

## At a glance

| Field | Value |
|---|---|
| Trigger | Scheduled task in Cowork, cron in the cloud sandbox |
| Repo path at run time | `/tmp/JobSearch` (cloned fresh each run) |
| Owns writes to | `applied-log.csv`, files under `drafts/*`, `Job_Digest_YYYY-MM-DD.md`, `role_configs_YYYYMMDD.py`, `run_YYYYMMDD.py`, new Notion rows in status `drafted`, Gmail drafts of the daily digest, git commits and pushes to `main` |
| Never touches | Notion status flips out of `drafted`, `Date Applied`, `Outreach Status`, LinkedIn or Xing compose windows, any file under `/Users/rahulrawat/Desktop/jobSearchClaude` (that is Agent B's checkout) |
| Reads at run start | [[CV Rules]], [[19 August 2026 Rules]], `master-projects.md` |

## STEP 0 — Environment preflight

`git clone` the repo with the PAT, `cd` into the checkout, install:

```
pip install weasyprint python-docx --break-system-packages
python3 -c "import weasyprint, docx"
```

If the toolchain does not install → HALT and email a "render toolchain failed" digest. Never fall back to markdown-only output. See [[Playbook - Render Toolchain Failed]].

## STEP 1 — Read the rule books

Read [[CV Rules]] and `master-projects.md` in full. All paths in this run are rooted at `/tmp/JobSearch`.

## STEP 2 — Backlog gate, Notion first

Query [[Notion Schema]] data source for rows where `Status = 'drafted'`. This count is authoritative. Only if Notion errors after one 30 second retry, fall back to counting `applied-log.csv` and note the fallback plainly in the digest.

Apply the 28 July 2026 gate (see [[CV Rules]]):

- Under 8 drafted → normal top 3 to 5
- 8 to 10 drafted → cap at top 3
- 11 or more drafted → HARD PAUSE, skip STEP 3 through STEP 6

## STEP 3 — Reconciliation

For each CSV row, match on `company` + `role` case insensitive. If Notion has a different Status, update the CSV to match Notion. If a CSV row is missing from Notion, create the Notion row with the CSV status. See [[Playbook - Notion CSV Drift]]. Reconciliation runs even on paused runs.

## STEP 4 — Search, filter, score, tailor

Sources in order of preference: LinkedIn, career pages, StepStone, Xing, Indeed. Indeed is capped at 1 per run under the 28 July yield weighting.

Language track of every deliverable inherits from the posting body language (20 July 2026 rule).

Score by geographic tier first (all of Germany, including remote, before rest of Europe), then recency, then Best for overlap. Distance is not a scoring factor.

## STEP 5 — Render eight deliverables per role

For every drafted role, render into `/tmp/JobSearch/drafts/[folder]/`:

1. `CV_Rahul_Rawat.md`
2. `CoverLetter_Rahul_Rawat.md`
3. `CV_Rahul_Rawat.docx`
4. `CV_Rahul_Rawat.html`
5. `CV_Rahul_Rawat.pdf`
6. `CoverLetter_Rahul_Rawat.docx`
7. `CoverLetter_Rahul_Rawat.html`
8. `CoverLetter_Rahul_Rawat.pdf`

Use `build_html.py` (see [[build_html.py Overview]]) plus a fresh `role_configs_YYYYMMDD.py` and `run_YYYYMMDD.py` you author for today. Pattern after `role_configs_13aug.py` and `run_13aug.py`.

If any deliverable fails to render → HALT that role and flag it in the digest. Never ship `.md` only.

## STEP 6 — Dual write

Append every newly drafted role to `applied-log.csv` with status `drafted`. Create the matching Notion row using [[Notion Schema]].

## STEP 7 — Digest and Gmail

Write `Job_Digest_YYYY-MM-DD.md` with top cut, watchlist, dropped roles, transparency block, backlog gate result, platform breakdown, language track decisions, and apply method per role. Create a Gmail draft to `rahulrawat2r@gmail.com`. Never send.

## STEP 8 — Commit and push

`git add -A`, commit with a message naming the date and count, push to `main`. If push fails, retry once, then flag in the digest. Do not force push. See [[Playbook - Push from Cowork Blocked]] for the bundle workaround.

## STEP 9 — Verify

Confirm every drafted folder has all eight deliverables. Confirm CSV and Notion `drafted` counts match after the run. Confirm the push landed with `git log -1 origin/main`. End the final chat message with: `N new roles drafted, backlog now M drafted in Notion, git commit hash, Gmail draft status`.

## Failure philosophy

Optimising for HONESTY over throughput. A run that drafts zero roles and reports "render toolchain failed to install" is a SUCCESSFUL run. A run that ships `.md`-only files and buries the failure in a Notes field is a FAILED run. Historical audit is not optional; every drafted row must be traceable to a specific search source and a specific run.
