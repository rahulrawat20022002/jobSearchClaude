# Rah Manual, Company Portal Submissions

Everything the two agents will not touch. This lane exists precisely because company portals cannot be automated reliably: they use custom form flows, ATS-vendor account creation gates, and per-company anti-bot detection that would trip [[02 Agent B - OpenClaw Submission]] in unpredictable ways. Rather than build custom flow handlers for every company, the pipeline draws a hard line: platform native = Agent B, company portal = Rah.

## What counts as a company portal

Any Apply Link that redirects to (or is hosted on) a company-owned careers domain. Current list observed in Rah's queue:

- `careers.bmwgroup.jobs` — BMW Group careers
- `jobs.sap.com` — SAP careers (SuccessFactors ATS)
- `jobs.siemens.com` — Siemens careers
- `careers.bshgroup.com` — BSH Home Appliances careers
- `careers.telekom.com` — Deutsche Telekom careers
- `careers.allianz.com` — Allianz careers
- `jobs.kfw.de` — KfW careers

Plus any other domain that behaves the same way: the Apply button leaves the aggregator, lands you on a company-branded careers site with its own login flow, its own uploads, its own confirmation email.

## Why they are out of scope for the agents

- **Account creation:** most portals require registering an account before the first submission, with email verification. Invariant #7 (never enter passwords, never accept account creation) rules this out for Agent B.
- **CAPTCHA and 2FA:** company portals routinely add these to reduce spam. Agent B halts on any of these per its strict rule #7.
- **Custom question sets:** each ATS asks different structured questions (visa status wording, availability, salary expectation). Some fields have no analogue in Rah's profile block and would force Agent B to invent an answer, which violates invariant #3 (never fabricate an outcome).
- **Uploads:** many portals reject the JavaScript DataTransfer method (13 August 2026 rule) that Agent B relies on for platform native uploads. That leaves screenshots, which OpenClaw cannot verify without human judgment.

Together, the amount of custom handling per portal to make submission reliable outweighs the throughput gain. Manual submission is faster than debugging OpenClaw against a fifth different portal.

## Rah's workflow for company portal roles

When Agent A drafts a company portal role, the row shows up in Notion in status `drafted` like any other. Agent B, when Rah later fires OpenClaw, hits the row, sees the URL redirects to a company domain, sets `Apply Method = company-portal`, appends `company-portal, Rah to submit manually` to Notes, and skips. The row stays in `drafted`.

Rah's routine:

1. Open Notion, filter to `Status = drafted AND Apply Method = company-portal`. That is the queue.
2. Sort by `Date Drafted` ascending, oldest first.
3. For each row, open the Apply Link in a fresh browser window.
4. Attach `CV_Rahul_Rawat.pdf` and `CoverLetter_Rahul_Rawat.pdf` from the draft folder shown in the `Draft Path` column.
5. Attach `Certificate_of_Enrolment.pdf`, `transcript.pdf`, `highest_degree.pdf` from `additional documents/` when the portal asks. Never upload the ID (`ausweis (1).pdf`) unless the portal explicitly requires it.
6. Salary expectation: if the field is optional, leave it blank. If required, use `15 EUR/hour` for Werkstudent framing (~1200 EUR/month for 20h/week, ~15600 EUR/year). Never invent another number.
7. Submit. Wait for a confirmation page or email.
8. Manually flip the Notion row: `Status = applied`, `Date Applied = today`, paste the confirmation string into Notes. If verification failed, keep at `drafted` and note the reason (same honesty rule as Agent B).

## Reference lists to have open

- Rah's profile block (visa, availability, notice period, German level) — memorised or in a sticky note. Do not deviate for a specific portal without noting the deviation.
- The 15 EUR/hour framing for salary fields.
- The additional documents folder location: `~/Desktop/jobSearchClaude/additional documents/`.
- The drafted role's `Draft Path` in Notion, so the right tailored CV+CL go up.

## Why this stays a manual lane

Two engineering answers considered and rejected:

- **Build per-portal adapters.** Would work but requires maintenance every time a portal updates its form. The pipeline is already stretched between search, tailoring, submission, and reconciliation; adding N portal adapters is not the highest leverage next step.
- **Use a headless browser with human intervention hooks.** Would need Rah watching the run anyway to handle CAPTCHAs and unusual fields. Faster to just submit manually.

Revisit this decision if the ratio of company portal to platform native listings in Rah's queue shifts significantly.

## See also

- [[02 Agent B - OpenClaw Submission]] for the platform native flow that these portals fall outside of
- [[Notion Schema]] for the `Apply Method` column
- [[Daily Workflow]] for how manual portal submissions fit into Rah's day
