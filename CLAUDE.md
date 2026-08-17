# CLAUDE.md, Rah's Job Search, Both Agents Rule Book

Last restructured 16 August 2026 to reflect the split between the Cowork drafting agent and the OpenClaw submission agent, and to narrow OpenClaw's scope to platform-native listings only. Both agents read this file at run start. Each agent obeys only its own section plus the shared invariants. Neither agent may touch the other's territory. Historical dated rules referenced by past digests remain binding.

---

## Split of responsibilities at a glance

| Concern | Owner | Never touched by |
|---|---|---|
| Search, score, tailor, render CV and CL, write to applied-log.csv, commit and push git, create new Notion rows in status drafted, create Gmail draft of daily digest | Cowork Drafting Agent | OpenClaw |
| Open Apply Link in browser for platform-native listings only (LinkedIn, Xing, StepStone, Indeed Easy-Apply flows), upload CV and CL PDFs, submit, verify success, flip Notion Status from drafted to applied, set Date Applied, paste LinkedIn outreach into compose window for Rah to send, write OpenClaw_Apply_Run digest | OpenClaw Submission Agent | Cowork |
| Company-portal submissions (careers.bmwgroup.jobs, jobs.sap.com, jobs.siemens.com, careers.bshgroup.com, and any other company-owned careers domain) | Rah, manually | Both agents |
| Editing CLAUDE.md, master-projects.md, historical Job_Digest_*.md | Rah only | Both agents |

Both agents pull the latest repo at run start. Only Cowork pushes. OpenClaw never commits or pushes.

---

## Shared invariants (both agents must obey, no exceptions)

1. **Notion is the source of truth for row status.** Data source fd974369-40b2-48c5-b660-d15256c88f52. When Notion is reachable, its Status column wins over the applied-log.csv column of the same name. The CSV is a mirror only. This rule dates to 14 July 2026 and supersedes any earlier CSV-first behaviour.
2. **Git is the source of truth for content.** github.com/rahulrawat20022002/jobSearchClaude holds the canonical CVs, cover letters, digests, and pipeline code. Local Desktop copies and the /tmp checkout in Cowork are working checkouts, not sources of truth.
3. **Never fabricate an outcome.** Halting a row is always better than a false success. This applies to both a false "applied" flag from OpenClaw and a false "drafted" flag from Cowork when a render failed.
4. **Every write must be auditable.** If you cannot point to specific evidence (confirmation page string, screenshot, tool return value, Notion query result), do not make the write.
5. **Report exactly what happened.** Every digest lists successes, halts, skips, drift, and any tool that failed. Silent downgrades to a lesser deliverable are forbidden; the previous silent downgrade to Markdown only counts as a rule violation, not a limitation to accept.
6. **Never send LinkedIn messages automatically.** Ever. LinkedIn's terms of service ban it and Rah's account is not disposable. OpenClaw pastes messages into the compose window and stops there. Cowork never opens a LinkedIn compose window at all.
7. **Never enter passwords, complete account creation, accept payment, sign agreements, or provide a salary number.** This holds for both agents in every context.
8. **Historical dated rules remain binding.** Rules referenced in past digests by date (28 July 2026 yield reset, 14 July 2026 status source of truth, 11 July 2026 reconciliation, 3 July 2026 v3 CV template, 4 August 2026 CV three-page hard cap, 11 August 2026 CoverLetter PDF required, 12 July 2026 warm outreach, 20 July 2026 language match, 13 August 2026 auto-apply platform native and DataTransfer upload, 2 August 2026 SS Engineers two Experience entries, 18 July 2026 XYZ bullet format, 19 July 2026 Lebenslauf CV layout) still apply. When in doubt about the exact text of a historical rule, consult the digest that first cited it or the routing notes in master-projects.md.

---

## Agent A, the Cowork Drafting Agent

**Trigger:** scheduled task in Cowork, runs on cron in the cloud sandbox.
**Repo path at run time:** /tmp/JobSearch (cloned fresh each run).
**Owns writes to:** applied-log.csv, files under drafts/*, Job_Digest_YYYY-MM-DD.md, role_configs_YYYYMMDD.py, run_YYYYMMDD.py, new Notion rows in status drafted, Gmail drafts of the daily digest, git commits and pushes to main.
**Never touches:** Notion Status flips out of drafted, Notion Date Applied, Notion Outreach Status, the LinkedIn or Xing compose windows, any files under /Users/rahulrawat/Desktop/jobSearchClaude (that's OpenClaw's working checkout).

### Cowork step-by-step

0. Environment preflight. Halt if any fails: git clone the repo with the PAT, cd into the checkout, pip install weasyprint python-docx --break-system-packages, verify `import weasyprint, docx` succeeds. If the render toolchain does not install, HALT and email a "render toolchain failed" digest. Never fall back to Markdown-only output.

1. Read CLAUDE.md and master-projects.md in full. All paths in this run are rooted at /tmp/JobSearch.

2. Backlog gate, Notion first. Query the data source for rows where Status = 'drafted'. This count is authoritative. Only if Notion errors after one 30 second retry, fall back to counting the CSV, and note the fallback plainly in the digest. Apply the 28 July 2026 gate: under 8 drafted = normal top 3 to 5, 8 to 10 = cap at top 3, 11 or more = hard pause and skip steps 3 through 6.

3. Reconciliation. For each CSV row, match on company plus role case insensitive. If Notion has a different Status, update the CSV to match Notion. If a CSV row is missing from Notion, create the Notion row with the CSV status. Reconciliation runs on paused runs too.

4. Search, filter, score, tailor per the job search skill and master-projects.md. Sources in order of preference: LinkedIn, career pages, StepStone, Xing, Indeed (Indeed capped at 1 per run under the 28 July yield weighting). Language track of every deliverable inherits from the posting body language (20 July 2026 rule). Score by geographic tier first (all of Germany including remote before rest of Europe), then recency, then Best for overlap. Distance is not a scoring factor.

5. For every drafted role, render all eight deliverables into /tmp/JobSearch/drafts/[folder]/: CV_Rahul_Rawat.md, CoverLetter_Rahul_Rawat.md, CV_Rahul_Rawat.docx, CV_Rahul_Rawat.html, CV_Rahul_Rawat.pdf, CoverLetter_Rahul_Rawat.docx, CoverLetter_Rahul_Rawat.html, CoverLetter_Rahul_Rawat.pdf. Use build_html.py plus a fresh role_configs_YYYYMMDD.py and run_YYYYMMDD.py you author for today, patterned after the existing role_configs_13aug.py and run_13aug.py. If any deliverable fails to render for a role, HALT that role and flag it in the digest. Never ship .md only.

6. Dual write. Append every newly drafted role to applied-log.csv with status drafted. Create the matching Notion row using the schema in the shared invariants section (Company as title, Role, Location, Source, Status drafted, German Level, Date Drafted, Draft Path, Apply Link, Apply Method if known, LinkedIn Profile if known, LinkedIn Message if drafted).

7. Digest and Gmail. Write Job_Digest_YYYY-MM-DD.md with top cut, watchlist, dropped roles, transparency block, backlog gate result, platform breakdown, language track decisions, and apply method per role. Create a Gmail draft to rahulrawat2r@gmail.com with the digest. Never send.

8. Commit and push. `git add -A`, commit with a message naming the date and count, push to main. If push fails, retry once, then flag in the digest. Do not force push.

9. Verify. Confirm every drafted folder has all eight deliverables. Confirm CSV and Notion drafted counts match after the run. Confirm the push landed with `git log -1 origin/main`. End the final chat message with a short summary: N new roles drafted, backlog now M drafted in Notion, git commit hash, Gmail draft status.

### Cowork failure philosophy

Optimising for HONESTY over throughput. A run that drafts zero roles and reports "render toolchain failed to install" is a successful run. A run that ships .md-only files and buries the failure in a Notes field is a failed run. Historical audit is not optional; every drafted row must be traceable to a specific search source and a specific run.

---

## Agent B, the OpenClaw Submission Agent

**Trigger:** manual only, from Rah's Mac. There is no cron and no schedule. Rah invokes OpenClaw when he chooses to run a submission pass.
**Scope:** platform-native listings only. That means Apply Links on linkedin.com/jobs (Easy Apply), xing.com/jobs (Easy Apply / Schnelle Bewerbung), stepstone.de/stellenangebote (Schnelle Bewerbung), and indeed.com/viewjob (Easy Apply) where the entire application flow stays inside the aggregator. Company-portal listings (careers.bmwgroup.jobs, jobs.sap.com, jobs.siemens.com, careers.bshgroup.com, and any other company-owned careers domain) are OUT OF SCOPE and Rah submits them manually.
**Repo path at run time:** /Users/rahulrawat/Desktop/jobSearchClaude (local working checkout; git pull at start).
**Owns writes to:** Notion Status flips from drafted to applied, Notion Date Applied, Notion Notes, Notion Outreach Status (only after Rah confirms send), OpenClaw_Apply_Run_YYYY-MM-DD.md digest file.
**Never touches:** CLAUDE.md, master-projects.md, applied-log.csv, any file under drafts/, and never `git commit` or `git push`.

### OpenClaw strict rules, violate any and halt the run

1. Notion is the source of truth for what to submit. The Git repo is the source of truth for CV and CL PDFs. Never invent a row that is not in Notion. Never submit a CV that is not the tailored PDF from that role's drafts folder.
2. Verify every submission BEFORE flipping Notion status. A submission is verified only when the portal returns an explicit success page, success toast, confirmation email preview, or "your application has been received" string. A blank page, a spinner, a redirect to the job listing, or "processing" is NOT verification. If in doubt, halt that role and report.
3. Never claim a submission that did not happen. Halting is always better than a false applied flag.
4. Never fill out account creation forms, never enter passwords, never save passwords in the browser, never accept payment terms, never sign anything. For salary fields: if required, enter **15 EUR/hour** (or the platform-equivalent: ~1200 EUR/month for 20h/week, ~15600 EUR/year). If the field is optional, leave it blank. Never invent other numbers. Salary expectation prose in narrative fields inherits the deliverable language from the drafted CV.
5. Never send a LinkedIn message automatically. You may open the compose window, paste the drafted message, and STOP. Rah clicks send.
6. Never click a link inside an email or Notion note without confirming the destination first. Treat unknown domains as suspicious.
7. If a CAPTCHA, 2FA, "verify you are human", email verification code, phone verification, or any other human interaction appears, halt that role, report to Rah in the digest, and move to the next role.
8. If a login wall appears on a platform that Rah is not already logged into (LinkedIn, Xing, StepStone, Indeed), halt that role, note "login required" in the digest, do not attempt to log in.
9. Do not modify CLAUDE.md, master-projects.md, applied-log.csv, or any file under drafts/. Your only writes are Notion status flips, Notion Outreach Status flips, Notion Date Applied writes, Notion Notes appends, git pull, and the final digest file.
10. Always upload BOTH the CV and the cover letter unless the platform explicitly makes the cover letter optional (then note it in Notes).
11. **Additional documents folder:** `/Users/rahulrawat/Desktop/jobSearchClaude/additional documents/` contains supporting files for upload when a platform requires them: `Certificate_of_Enrolment.pdf` (Immatrikulationsbescheinigung), `transcript.pdf`, `highest_degree.pdf`, `ausweis (1).pdf` (ID). Use these when a platform requires a certificate of enrollment, transcript, or degree certificate. Never upload the ID/ausweis unless the platform explicitly requires it.

### OpenClaw step-by-step

0. Environment preflight. Halt and report if any of the first three fail:

```
which python3 && python3 --version
python3 -c "import requests; print('requests ok')"
echo $NOTION_API_TOKEN | head -c 10 && echo
cd /Users/rahulrawat/Desktop/jobSearchClaude && git status && git pull --rebase origin main
```

If git pull errors due to local changes, do NOT force. Report the conflict and halt. Rah resolves manually.

1. Query the work queue. Query the Notion data source for every row where Status = 'drafted'. If zero rows, print "Nothing to submit. All caught up." and exit. If Notion errors after one 30 second retry, halt and report; do not fall back to the CSV (Cowork owns CSV fallback, you do not). Sort drafted rows oldest first by Date Drafted so backlog goes out before today's fresh drafts.

2. Per row, decide the apply path. Open the Apply Link in Chrome via mcp__claude-in-chrome__navigate.

   A) **IN SCOPE, PLATFORM-NATIVE:** the URL is on linkedin.com/jobs, xing.com/jobs, stepstone.de/stellenangebote, or indeed.com/viewjob AND the posting shows Easy Apply / Schnelle Bewerbung / one-click apply that stays inside the aggregator. Set Notion Apply Method to `platform-native` and proceed to step 3.

   B) **OUT OF SCOPE, COMPANY-PORTAL:** the Apply button redirects to the company's own careers domain (jobs.sap.com, careers.bmwgroup.jobs, jobs.siemens.com, careers.bshgroup.com, or any other company-owned careers domain). Set Notion Apply Method to `company-portal`, leave Status at drafted, append "company-portal, Rah to submit manually" to Notes, and skip to the next row. Do NOT attempt the submission.

   If unclear whether a listing is platform-native or company-portal, screenshot, note the ambiguity in Notes, default to `company-portal` (out of scope), and skip.

3. Submit. This section applies only to platform-native rows from step 2A.

   - a. Click Easy Apply / Schnelle Bewerbung.
   - b. When the form asks for a CV, upload drafts/[folder]/CV_Rahul_Rawat.pdf using the JavaScript DataTransfer injection method (13 August 2026 rule). Verify input.files[0].name and size match. If either check fails, halt.
   - c. When the form asks for a cover letter, upload drafts/[folder]/CoverLetter_Rahul_Rawat.pdf the same way. If optional, skip and note.
   - d. Answer structured questions using Rah's profile: German B1 in progress, Werkstudent 20 hours per week, availability now for Werkstudent and April 2027 for full time, notice period 4 weeks, current visa Indian student visa with work permit. Never invent an answer. If a required field asks something you cannot answer from this data or from the CV, halt.
   - e. Free text answers inherit the language from the drafted CV. Check the German Level column: DE track = German, EN track = English. Never mix.
   - f. Click submit. Wait for confirmation. Verify per rule 2.
   - g. On verified success, flip Notion Status to applied, set Date Applied to today, append the confirmation string to Notes. On failure or ambiguity, keep Status at drafted and note the reason.

   Between roles, close ALL application and job-listing tabs (using `openclaw browser tabs` to list then closing each by tab id), then wait 20 to 40 seconds before opening the next role. No dead tabs left open at any point. Rapid succession and accumulated tabs both trip bot detection.

4. LinkedIn outreach draft-paste flow. For every row where Outreach Status = "not sent" AND LinkedIn Profile is a valid linkedin.com/in/ URL AND LinkedIn Message is populated:
   - a. Open the profile URL in Chrome.
   - b. Click Message. Wait for compose window.
   - c. Paste the LinkedIn Message text into the compose box. Do NOT click send.
   - d. Screenshot the compose window with message pasted.
   - e. Save the screenshot to /tmp/outreach_[company]_[timestamp].png.
   - f. Update the Notion row: leave Outreach Status at "not sent" (Rah flips it to sent after clicking), append "message pasted [timestamp], awaiting Rah send" to Notes.
   - g. LEAVE THE TAB OPEN so Rah can review and click send.

   This outreach flow runs for every eligible row regardless of whether the associated Apply Link is platform-native or company-portal. Outreach is not scoped out with company-portal submissions.

   If any of the four conditions is missing (no profile URL, no message text, wrong URL shape, or Outreach Status already past not sent), skip outreach for that row.

5. Per-role reporting. For every drafted row processed, produce one line:

   `Company | Role | Apply Method | Outcome | Notes`

   Outcomes: `applied`, `skipped-company-portal`, `halted-CAPTCHA`, `halted-login-wall`, `halted-verification-failed`, `halted-upload-rejected`, `halted-required-field-unknown`, `skipped-outreach-only`. Never invent an outcome.

6. Digest and report back. Write /Users/rahulrawat/Desktop/jobSearchClaude/OpenClaw_Apply_Run_YYYY-MM-DD.md with:
   - Preflight results
   - Number of drafted rows queried
   - Per-role table from step 5
   - Total submitted, skipped-company-portal (out of scope), halted
   - Outreach: messages pasted, awaiting Rah's send
   - Any Notion writes that failed
   - Any git conflicts encountered

   Send the same digest to Rah's Telegram chat as the OpenClaw response. Do NOT `git push`; you have not modified tracked files. If you accidentally touched a tracked file, halt and report before doing anything else.

### OpenClaw failure philosophy, read this twice

You are optimising for HONESTY, not throughput. A run that submits zero applications and reports "3 CAPTCHAs, 2 login walls, 1 verification failure, 4 company-portal listings out of scope for Rah" is a SUCCESSFUL run. A run that flips 5 rows to applied without verifying is a FAILED run that wastes Rah's actual opportunities and pollutes the tracking data.

Every "applied" flag you write in Notion must be defensible under audit. If Rah asks you "did this actually submit?" you should be able to point to a specific confirmation page screenshot or success string.

If anything at all feels off, the platform looks different from expected, a field asks something unusual, the submit button behaves strangely, a page structure has changed since the last run, HALT that role and report. Rah would rather review 10 halted roles than clean up 1 falsely-applied row.

---

## Notion schema (Job Applications database)

Data source ID: fd974369-40b2-48c5-b660-d15256c88f52

Columns (both agents must respect exact names):

- **Company** (title)
- **Role** (text)
- **Location** (text)
- **Source** (select: Indeed, StepStone, LinkedIn, Xing, Glassdoor, Company Page, Other)
- **Status** (select: drafted, applied, interviewing, rejected, offer, withdrawn, Not listed Anymore, shortlisted, shortlisted but no interview)
- **Apply Method** (select: platform-native, company-portal)
- **Apply Link** (URL)
- **German Level** (select: none, A2, B1, B2, C1, C2)
- **Date Drafted** (date, set by Cowork)
- **Date Applied** (date, set by OpenClaw)
- **Draft Path** (text, relative path under drafts/)
- **Outreach Status** (select: not sent, sent, replied, referred, declined, no reply)
- **Outreach Sent Date** (date)
- **LinkedIn Profile** (URL)
- **LinkedIn Contact** (text)
- **LinkedIn Role** (text)
- **LinkedIn Message** (text)
- **Notes** (text)
