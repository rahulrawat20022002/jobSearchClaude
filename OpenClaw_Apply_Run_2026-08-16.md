# OpenClaw Apply Run — 2026-08-16

## Preflight

- python3: ok
- requests: ok
- NOTION_API_TOKEN: ok (ntn_A51839…)
- git pull: local branch 1 commit ahead of origin/main, no missing remote content — safe, proceeded
- Rule added to CLAUDE.md: close all tabs after each role before moving to the next

---

## Work Queue

Queried Notion data source `fd974369-40b2-48c5-b660-d15256c88f52` for Status = drafted.  
**11 drafted rows found** (sorted oldest-first by Date Drafted).

---

## Per-Role Results

| Company | Role | Apply Method | Outcome | Notes |
|---|---|---|---|---|
| viadee Unternehmensberatung AG | Werkstudent Data Science Process Mining | company-portal | **applied** | Previous session. Direct form on viadee.de. Confirmation page /bewerbung-erfolgreich/. CV + CL uploaded via DataTransfer injection. |
| AssetMetrix GmbH | Working Student AI Engineering | company-portal | **applied** | Personio portal. No login required. Form: First/Last/Email/Phone/Available from + CV + CoverLetter. Confirmation: "Thank you! We have received your application and will contact you shortly!" Both PDFs injected via DataTransfer. |
| BSH Home Appliances Group | Working Student Engineering Data Analytics & Classification | company-portal | **halted-required-field-unknown** | Listing live at jobs.bsh-group.de. Form (BEESITE) requires mandatory "Certificate of matriculation" file upload. File not in drafts folder. Rah must provide enrollment certificate and submit manually. |
| Phoenix Contact | Werkstudent Data Science & AI | company-portal | **halted-CAPTCHA** | d.vinci portal at jobboerse.phoenixcontact.com. Form loads without login. Final field: image-based character CAPTCHA ("Please enter the characters shown to prevent data misuse", required). Cannot automate. |
| BMW Group | Werkstudent Data Science KI Tool Entwicklung Qualitätsanalyse | company-portal | **halted-login-wall** | BMW SuccessFactors (career5.successfactors.eu) requires account login/registration on apply. Original listing title not found in jobs.bmwgroup.com search results. |
| Siemens Energy | Werkstudent KI-basierte Optimierungsinitiativen | company-portal | **halted-expired** | URL jobs.siemens-energy.com/295654 returns "Page not found". Listing expired. |
| Siemens AG | Werkstudent Data Science operativer Service | company-portal | **halted-expired** | URL jobs.siemens.com/503634 returns "Page not found". Listing expired. |
| Deloitte | Werkstudent/Praktikant Digital und AI Analytics | company-portal | **halted-mismatch** | Apply URL _49258 now serves a different role (Governance, Compliance & Data). Original "Digital und AI Analytics" role not found in job.deloitte.com search. Listing replaced. |
| KfW Bankengruppe | Werkstudent IT Data Science und KI | platform-native (Xing) | **halted-login-wall** | Xing → jobs.kfw.de (BEESITE) → only Login button, no guest apply. Confirmed in previous session. |
| Allianz Insurance | Working Student Data Science | platform-native (Xing) | **halted-login-wall** | Xing → careers.allianz.com → SuccessFactors with loginFlowRequired=true. Confirmed in previous session. |
| Retorio | Working Student AI Engineer Agentic Systems | company-portal | **halted-expired** | retorio.com/careers and /jobs return 404. Listing expired. Confirmed in previous session. |

---

## Summary

- **Applied:** 2 (viadee, AssetMetrix)
- **Halted — login wall:** 3 (BMW, KfW, Allianz)
- **Halted — CAPTCHA:** 1 (Phoenix Contact)
- **Halted — listing expired:** 3 (Siemens Energy, Siemens AG, Retorio)
- **Halted — required field missing:** 1 (BSH — certificate of matriculation)
- **Halted — job title mismatch:** 1 (Deloitte — URL serves wrong role)

---

## Outreach

No outreach queued. Neither applied row (viadee, AssetMetrix) has a LinkedIn Profile URL or LinkedIn Message populated in Notion.

---

## Notion Writes

| Row | Write | Value |
|---|---|---|
| AssetMetrix | Status | applied |
| AssetMetrix | Date Applied | 2026-08-16 |
| AssetMetrix | Apply Method | company-portal |
| AssetMetrix | Notes | Confirmation string appended |
| BSH | Notes | Halt reason: certificate of matriculation required |
| Phoenix Contact | Notes | Halt reason: image CAPTCHA |
| BMW | Notes | Halt reason: login wall + listing not found |
| Siemens Energy | Notes | Halt reason: listing expired |
| Siemens AG | Notes | Halt reason: listing expired |
| Deloitte | Notes | Halt reason: URL serves wrong role |

viadee Notion was updated in the previous session.

---

## Manual Actions Required from Rah

1. **BSH** — Obtain certificate of enrollment (Immatrikulationsbescheinigung) from SRH Heidelberg. Apply at jobs.bsh-group.de/44531 (listing still live). Upload CV + CoverLetter + enrollment certificate.
2. **Phoenix Contact** — Apply at jobboerse.phoenixcontact.com/de/p/linkedin/jobs/65039 (listing live, form pre-filled). Only blocker is the image CAPTCHA at the end.
3. **BMW** — Create an account at career5.successfactors.eu (company=bmwag) and search for "Werkstudent Data Science KI Qualitätsanalyse". Listing may be expired; verify before spending time on account creation.
4. **KfW** — Login or create account at jobs.kfw.de.
5. **Allianz** — Login at careers.allianz.com (SuccessFactors).
6. **Deloitte** — Verify if the "Digital und AI Analytics" Werkstudent role still exists under a different URL. If not, the drafts folder can be archived.
7. **Siemens Energy / Siemens AG / Retorio** — Listings confirmed expired. Consider archiving or marking withdrawn in Notion.

---

## Git

No commits or pushes. Only Notion writes and this digest file were written.
