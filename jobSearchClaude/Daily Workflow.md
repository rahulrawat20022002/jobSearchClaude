# Daily Workflow

How Rah's day flows through the pipeline. This is descriptive, not prescriptive — the schedule shifts around interviews and travel — but it captures the normal cadence and what to check when.

## Morning (Rah)

1. **Pull the repo on the Mac.** `cd ~/Desktop/jobSearchClaude && git pull --rebase origin main`. If a rebase conflict appears, do NOT let [[02 Agent B - OpenClaw Submission]] run until resolved; per its STEP 0, it will halt on a dirty checkout anyway.
2. **Read today's Gmail digest.** [[01 Agent A - Cowork Drafting]] STEP 7 leaves a draft to `rahulrawat2r@gmail.com` with the day's cut. Read it in Gmail Drafts folder, do not send it (the digest is for Rah, not outbound).
3. **Skim the digest.** Sections in order: top cut (roles Rah should actually consider), watchlist (drafted but marginal), dropped (with reasons), transparency block (search sources hit, dedup counts), backlog gate result, platform breakdown (LinkedIn vs Xing vs StepStone vs Indeed vs Career Page counts), language track decisions (which roles are DE vs EN and why), apply method per role.
4. **Open Notion.** Filter to `Status = drafted`, sort by `Date Drafted` descending. Newest at the top are today's roles. Verify [[Notion Schema]] columns look right — Company, Role, Apply Method (if already set from a prior OpenClaw pass), German Level.
5. **Decide today's submissions.** For each new drafted row, decide: submit today, save for later, or reject. Reject → flip Status to `withdrawn` in Notion with a Notes reason.

## Mid morning (Rah)

Company portal submissions ([[03 Rah Manual - Company Portals]]):

1. Filter Notion to `Status = drafted AND Apply Method = company-portal`. Also filter to blank `Apply Method` on rows drafted before OpenClaw last ran, since those have not been classified yet — OpenClaw will set them on its next pass.
2. For each row, open the Apply Link. Attach the tailored `CV_Rahul_Rawat.pdf` and `CoverLetter_Rahul_Rawat.pdf` from the folder in `Draft Path`. Attach `Certificate_of_Enrolment.pdf`, `transcript.pdf`, `highest_degree.pdf` as required.
3. Submit. Manually flip Notion: `Status = applied`, `Date Applied = today`, paste confirmation string into Notes.

## Late morning (Rah, optional)

Fire OpenClaw if there is a queue of platform-native drafts:

1. In Cowork on Mac, launch OpenClaw.
2. It runs [[02 Agent B - OpenClaw Submission]] STEP 0 through STEP 6.
3. Read the `OpenClaw_Apply_Run_YYYY-MM-DD.md` digest that lands in `~/Desktop/jobSearchClaude/`.
4. Review any halted rows — CAPTCHA, login walls, verification failures. Decide per row whether to retry manually or drop.
5. Review the LinkedIn outreach tabs OpenClaw left open — read the pasted messages, click send in the ones Rah wants to send. After clicking send, flip Notion `Outreach Status` to `sent` and set `Outreach Sent Date`.

## Afternoon (background)

- [[01 Agent A - Cowork Drafting]]'s next scheduled run may fire (there is often an early-afternoon PM run when the morning yielded few roles). The digest lands in Gmail Drafts the same way. Rah can either combine it with the morning cut for a single OpenClaw pass, or fire OpenClaw again for the fresh batch.
- Rah reviews `master-projects.md` when a project or certification changes. Never edit the CV directly; edit `master-projects.md` and let the render pipeline pick it up. See [[Skills Buckets]] for the "must be evidenced in a bullet" rule.

## Weekly (Rah)

- **Reconciliation audit.** Spot check 5 random `applied` rows and verify each has a confirmation string in Notes. This is the audit trail invariant #4 relies on.
- **Master projects hygiene.** Prune projects that are no longer relevant. Add anything new Rah shipped that week.
- **CV rules review.** Skim [[CV Rules]] and [[19 August 2026 Rules]]. If Rah made any tactical override during the week ("dropped the second cert for this one BMW role"), decide whether it should become a rule or stays as a one off.

## When something breaks

- Push failed from Cowork → [[Playbook - Push from Cowork Blocked]]
- Two page cap exceeded → [[Playbook - 2 Page Cap Exceeded]]
- Notion / CSV drift surfaced → [[Playbook - Notion CSV Drift]]
- Render toolchain failed at STEP 0 → [[Playbook - Render Toolchain Failed]]

## What NOT to do (order of operations traps)

- Do not manually flip a Notion row from `drafted` to `applied` for a platform native role and then run OpenClaw on the same day. OpenClaw will find the row already at `applied`, skip it, and no verification will happen. If you must submit manually, either flip after OpenClaw has run, or delete the row from OpenClaw's queue by flipping Apply Method to `company-portal` first.
- Do not commit to `main` from the Mac while a Cowork run is mid-flight. Cowork pushes at STEP 8; a concurrent local push causes an ugly rebase. If the Cowork run is scheduled, wait for its digest before pushing.
- Do not edit `applied-log.csv` by hand. Notion is the source of truth. If the CSV is wrong, fix it in Notion and let the next reconciliation sync it.

## See also

- [[Pipeline Overview]] for the actor map
- [[01 Agent A - Cowork Drafting]] for the drafting agent's steps
- [[02 Agent B - OpenClaw Submission]] for the submission agent's steps
