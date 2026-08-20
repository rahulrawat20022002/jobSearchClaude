# Notion Schema, Job Applications Database

Data source ID: `fd974369-40b2-48c5-b660-d15256c88f52`

Both agents must respect these exact column names. Shared invariant #1 (see [[Pipeline Overview]]) makes Notion the source of truth for row status, so a typo in a column name is not a small bug; it means the write silently misses and the row diverges from CSV. See [[Playbook - Notion CSV Drift]] for what happens when this occurs.

## Columns

### Identity

| Column | Type | Notes |
|---|---|---|
| **Company** | title | Also the row title in Notion's UI. |
| **Role** | text | Free-form. Match on `Company + Role` case insensitive during CSV reconciliation. |
| **Location** | text | City or "Remote (Germany)" etc. Distance is not a scoring factor per the 28 July 2026 rule. |
| **Source** | select | `Indeed`, `StepStone`, `LinkedIn`, `Xing`, `Glassdoor`, `Company Page`, `Other`. Indeed capped at 1 per run per the 28 July yield weighting. |

### State machine

| Column | Type | Notes |
|---|---|---|
| **Status** | select | `drafted`, `applied`, `interviewing`, `rejected`, `offer`, `withdrawn`, `Not listed Anymore`, `shortlisted`, `shortlisted but no interview`. Only [[02 Agent B - OpenClaw Submission]] flips out of `drafted`. [[01 Agent A - Cowork Drafting]] only creates new rows in `drafted`. |
| **Apply Method** | select | `platform-native`, `company-portal`. Written by [[02 Agent B - OpenClaw Submission]] STEP 2 after inspecting the Apply Link. |
| **Date Drafted** | date | Set by [[01 Agent A - Cowork Drafting]] STEP 6 when the row is created. |
| **Date Applied** | date | Set by [[02 Agent B - OpenClaw Submission]] STEP 3g on verified success. Never set by Agent A. |

### Apply payload

| Column | Type | Notes |
|---|---|---|
| **Apply Link** | URL | The URL Agent A sourced. Agent B navigates to this. |
| **German Level** | select | `none`, `A2`, `B1`, `B2`, `C1`, `C2`. Determines the deliverable language track per the 20 July 2026 rule. See [[CV Rules]]. |
| **Draft Path** | text | Relative path under `drafts/` for this role's folder. Contains all 8 deliverables. |

### Outreach

| Column | Type | Notes |
|---|---|---|
| **Outreach Status** | select | `not sent`, `sent`, `replied`, `referred`, `declined`, `no reply`. Rah flips from `not sent` to `sent` after clicking send in LinkedIn. |
| **Outreach Sent Date** | date | Set when Rah flips `Outreach Status` to `sent`. |
| **LinkedIn Profile** | URL | `linkedin.com/in/...` for the target contact. Populated by Agent A under the 12 July 2026 warm outreach rule. |
| **LinkedIn Contact** | text | Human readable name of the contact. |
| **LinkedIn Role** | text | Their role at the company (recruiter, hiring manager, team lead). |
| **LinkedIn Message** | text | The drafted message. Agent B pastes and stops. |

### Freeform

| Column | Type | Notes |
|---|---|---|
| **Notes** | text | Both agents append. Common notes: `company-portal, Rah to submit manually`, `login required`, `verification failed: <string>`, `CAPTCHA halted`, confirmation string on successful submission. |

## Who writes what

| Writer | Columns it may write |
|---|---|
| [[01 Agent A - Cowork Drafting]] | Company, Role, Location, Source, Status (only on new row creation, always `drafted`), Apply Link, German Level, Date Drafted, Draft Path, LinkedIn Profile, LinkedIn Contact, LinkedIn Role, LinkedIn Message |
| [[02 Agent B - OpenClaw Submission]] | Status (only `drafted → applied`), Apply Method, Date Applied, Notes (append), Outreach Status (only Rah flips to `sent`, but Agent B never flips out of `not sent`) |
| Rah, manually | Everything, including corrections and status flips beyond `applied` (interviewing, rejected, offer, etc.) |

## Reconciliation semantics

See [[Playbook - Notion CSV Drift]] for the runbook. Short version: Notion always wins. When [[01 Agent A - Cowork Drafting]] STEP 3 reconciles, if Notion's `Status` differs from `applied-log.csv`'s `Status` for the same `Company + Role`, the CSV is updated. If a CSV row is missing from Notion, Agent A creates the Notion row with the CSV status (this is the ONLY case where CSV informs a Notion write on reconciliation; the row is by definition missing so Notion has nothing to defend).

## See also

- [[Pipeline Overview]] for the four invariants
- [[01 Agent A - Cowork Drafting]] STEP 6 for how new rows are created
- [[02 Agent B - OpenClaw Submission]] STEP 3g for the `drafted → applied` flip
