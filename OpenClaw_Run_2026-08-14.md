# OpenClaw Auto-Apply Run — 14 August 2026

## Summary

| # | Company | Role | Portal | Status | Notes |
|---|---------|------|--------|--------|-------|
| 1 | Mercedes-Benz | Masterarbeit Learning Dexterous Robot Manipulation, Sindelfingen | Oracle Taleo (tas-daimler.taleo.net) | ✅ Submitted | Completed step 6/6; CV + cover letter uploaded |
| 2 | BMW Group | Werkstudent Data Analytics Qualitätsmanagement Digitale Dienste, München | SAP SuccessFactors | ✅ Submitted | Profile-based form; accepted existing CV (02.08.26) |
| 3 | BMW Group | Abschlussarbeit KI-Agenten Produktionsplanung Hochvoltspeicher, München | SAP SuccessFactors | ✅ Submitted | Profile-based form |
| 4 | SCHOTT AG | (role via StepStone) | StepStone Quick Apply | ✅ Submitted | "I'm interested" quick-apply; confirmed via /application/confirmation/success URL |
| 5 | HDI AG | Werkstudent Data Engineering & Analytics Aktuariat, Hannover | StepStone Quick Apply | ✅ Submitted | "I'm interested" quick-apply |
| 6 | Commerzbank | Praktikant Big Data & Advanced Analytics / Projektcontrolling AI, Frankfurt | Jobylon (jobs.commerzbank.com) | ⛔ Blocked | Portal requires Immatrikulationsbescheinigung (university enrollment certificate). CV + cover letter already uploaded. Rah must manually upload the certificate and click "Review & submit". |
| 7 | CHECK24 | Werkstudent AI-Produkte – Kreditvergleich, München | CHECK24 Career Portal (jobs.check24.de) | ✅ Submitted | Found via Xing listing; full form filled (personal info, German B2, non-EU temp permit, 20h/week, 14 EUR/h); CV + cover letter uploaded; success URL confirmed |

## Totals
- **Submitted:** 6
- **Blocked:** 1 (Commerzbank — missing enrollment certificate)
- **Pending manual action:** Commerzbank — Rah to upload Immatrikulationsbescheinigung then click "Review & submit"

## Commerzbank Portal URL (for manual completion)
`https://jobs.commerzbank.com//index.php?ac=application&application_token=2fcd627ffefa591123e3c2f2e770dd9b71b1e7d7&jobad_id=62213`

## Platform Automation Notes
- **StepStone Quick Apply**: Works fully automated — "I'm interested" single click, no CV upload needed.
- **Oracle Taleo**: Fully automatable — multi-step form, file upload via JS DataTransfer pattern.
- **SAP SuccessFactors**: Fully automatable — profile-based, existing profile CV used.
- **CHECK24 Career Portal**: Automatable but location field requires autocomplete selection (not raw text value); React form state must be updated via native input events.
- **Xing Easy Apply**: Not available for CHECK24 — redirects to employer website only.
- **LinkedIn Easy Apply**: Not available for Commerzbank — redirects to company portal.

