# Agent B, the OpenClaw Submission Agent

## At a glance

| Field | Value |
|---|---|
| Trigger | Manual only, from Rah's Mac. No cron, no schedule. Rah invokes OpenClaw when he chooses a submission pass. |
| Repo path at run time | `/Users/rahulrawat/Desktop/jobSearchClaude` (local working checkout; `git pull` at start) |
| Owns writes to | Notion Status flips from `drafted → applied`, Notion `Date Applied`, Notion `Notes`, Notion `Outreach Status` (only after Rah confirms send), `OpenClaw_Apply_Run_YYYY-MM-DD.md` digest file |
| Never touches | `CLAUDE.md`, `master-projects.md`, `applied-log.csv`, any file under `drafts/`, and never `git commit` or `git push` |
| Scope | Platform native listings ONLY — see below |

## Platform native scope

Agent B submits **only** listings where the Apply Link is on:

- `linkedin.com/jobs` — Easy Apply
- `xing.com/jobs` — Easy Apply / Schnelle Bewerbung
- `stepstone.de/stellenangebote` — Schnelle Bewerbung
- `indeed.com/viewjob` — Easy Apply

...AND the entire application flow stays inside the aggregator.

Company portal listings (`careers.bmwgroup.jobs`, `jobs.sap.com`, `jobs.siemens.com`, `careers.bshgroup.com`, or any other company-owned careers domain) are OUT OF SCOPE. See [[03 Rah Manual - Company Portals]].

Ambiguous listing? Screenshot, note the ambiguity, default to `company-portal` (out of scope), skip.

## STEP 0 — Environment preflight

```
which python3 && python3 --version
python3 -c "import requests; print('requests ok')"
echo $NOTION_API_TOKEN | head -c 10 && echo
cd /Users/rahulrawat/Desktop/jobSearchClaude && git status && git pull --rebase origin main
```

Halt and report if any of the first three fail. If `git pull` errors due to local changes, do NOT force. Report the conflict and halt; Rah resolves manually.

## STEP 1 — Query the work queue

Query Notion for every row where `Status = 'drafted'`. If zero rows → print `Nothing to submit. All caught up.` and exit. Sort drafted rows oldest first by `Date Drafted` so backlog goes out before today's fresh drafts.

If Notion errors after one 30 second retry → halt and report. Do NOT fall back to the CSV; that is Agent A's fallback path, not yours.

## STEP 2 — Per row, decide the apply path

Open the Apply Link in Chrome via `mcp__claude-in-chrome__navigate`.

**Path A — IN SCOPE, platform native:** URL is on one of the four aggregators AND the posting shows Easy Apply / Schnelle Bewerbung / one-click apply that stays inside the aggregator. Set Notion `Apply Method` to `platform-native` and proceed to STEP 3.

**Path B — OUT OF SCOPE, company portal:** the Apply button redirects to a company-owned careers domain. Set Notion `Apply Method` to `company-portal`, leave `Status` at `drafted`, append `company-portal, Rah to submit manually` to Notes, and skip to the next row. Do NOT attempt the submission.

## STEP 3 — Submit (platform native only)

1. Click Easy Apply / Schnelle Bewerbung.
2. When the form asks for a CV → upload `drafts/[folder]/CV_Rahul_Rawat.pdf` via the JavaScript DataTransfer injection method (13 August 2026 rule). Verify `input.files[0].name` and size. If either check fails → HALT.
3. When the form asks for a cover letter → upload `drafts/[folder]/CoverLetter_Rahul_Rawat.pdf` the same way. If optional, skip and note.
4. Answer structured questions using Rah's profile: German B1 in progress, Werkstudent 20h/week, availability now for Werkstudent and April 2027 for full time, notice period 4 weeks, current visa Indian student visa with work permit. Never invent an answer. Required field you cannot answer → HALT.
5. Free text answers inherit the CV language. Check `German Level`: DE track = German, EN track = English. Never mix.
6. Click submit. Wait for confirmation. Verify per the strict rule below.
7. On verified success → flip Notion `Status` to `applied`, set `Date Applied` to today, append the confirmation string to Notes. On failure or ambiguity → keep `Status = drafted`, note the reason.

**Between roles:** close ALL application and job listing tabs (use `openclaw browser tabs` to list, close by tab id), then wait 20 to 40 seconds before opening the next role. No dead tabs left open. Rapid succession and accumulated tabs both trip bot detection.

## STEP 4 — LinkedIn outreach draft-paste flow

For every row where `Outreach Status = "not sent"` AND `LinkedIn Profile` is a valid `linkedin.com/in/` URL AND `LinkedIn Message` is populated:

1. Open the profile URL in Chrome.
2. Click Message. Wait for compose window.
3. Paste the message text into the compose box. Do NOT click send.
4. Screenshot the compose window with message pasted.
5. Save the screenshot to `/tmp/outreach_[company]_[timestamp].png`.
6. Update the Notion row: leave `Outreach Status` at `not sent` (Rah flips it after clicking send), append `message pasted [timestamp], awaiting Rah send` to Notes.
7. LEAVE THE TAB OPEN so Rah can review and click send.

This flow runs for every eligible row regardless of whether the Apply Link is platform-native or company portal. Outreach is not scoped out with company portal submissions.

## STEP 5 — Per role reporting

For every drafted row processed, produce one line:

`Company | Role | Apply Method | Outcome | Notes`

Outcomes (never invent one): `applied`, `skipped-company-portal`, `halted-CAPTCHA`, `halted-login-wall`, `halted-verification-failed`, `halted-upload-rejected`, `halted-required-field-unknown`, `skipped-outreach-only`.

## STEP 6 — Digest and report back

Write `/Users/rahulrawat/Desktop/jobSearchClaude/OpenClaw_Apply_Run_YYYY-MM-DD.md` with preflight results, drafted rows queried, per-role table, totals, outreach status, any Notion write failures, any git conflicts. Send the same digest to Rah's Telegram chat as the OpenClaw response.

Do NOT `git push`; you have not modified tracked files. If you accidentally touched one, HALT and report before doing anything else.

## Strict rules, violate any and halt

1. Notion is the source of truth for what to submit. Git is the source of truth for CV and CL PDFs.
2. **Verify every submission BEFORE flipping Notion status.** Verification means an explicit success page, success toast, confirmation email preview, or "your application has been received" string. Blank page, spinner, redirect back to the listing, or "processing" is NOT verification.
3. Never claim a submission that did not happen.
4. Never fill account creation forms, enter passwords, save passwords in the browser, accept payment, sign anything. **Salary field: if required, enter 15 EUR/hour** (~1200 EUR/month for 20h/week, ~15600 EUR/year). If optional, leave blank.
5. Never send a LinkedIn message automatically. Paste and stop. Rah clicks send.
6. Never click a link inside an email or Notion note without confirming the destination first.
7. CAPTCHA / 2FA / verify-you-are-human / email or phone verification appears → HALT that role, next.
8. Login wall on a platform Rah is not already logged into → HALT that role, note `login required`, do not attempt to log in.
9. Do not modify `CLAUDE.md`, `master-projects.md`, `applied-log.csv`, or any file under `drafts/`.
10. Always upload BOTH CV and cover letter unless the platform explicitly makes the CL optional (note it).
11. `additional documents/` holds `Certificate_of_Enrolment.pdf`, `transcript.pdf`, `highest_degree.pdf`, `ausweis (1).pdf`. Use as required. Never upload the ID unless explicitly required.

## Why B never pushes

Agent B's writes are entirely in Notion and in its own digest file. Nothing under `drafts/`, nothing in tracked source. If it commits or pushes anything, it has violated its lane — see invariants #2 and #4 in [[Pipeline Overview]]. This is why the rule reads "never commit or push", not "usually don't push".

## Failure philosophy (read twice)

Optimising for HONESTY, not throughput. A run that submits zero applications and reports `3 CAPTCHAs, 2 login walls, 1 verification failure, 4 company-portal listings out of scope for Rah` is a SUCCESSFUL run. A run that flips 5 rows to `applied` without verifying is a FAILED run that wastes Rah's actual opportunities and pollutes tracking data.

Every `applied` flag written to Notion must be defensible under audit. If Rah asks "did this actually submit?" you should point to a specific confirmation page screenshot or success string.

If anything at all feels off — the platform looks different from expected, a field asks something unusual, the submit button behaves strangely, a page structure changed since last run — HALT that role and report. Rah would rather review 10 halted roles than clean up 1 falsely applied row.
