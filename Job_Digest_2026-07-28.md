# Job Search Digest, 28 July 2026

## Run status: HARD PAUSE

Notion Job Applications database currently shows 15 rows with status drafted. The 28 July 2026 backlog gate says 11 or more drafted rows triggers a hard pause. The search step, the draft step, the CSV append step, the Notion create step, and the Gmail digest with new roles are all skipped this run. Only this pause digest and the CSV to Notion reconciliation step ran.

Rah needs to work through the drafted backlog before the next scheduled run drafts anything new. Once the drafted count in Notion drops below 11, the normal top 3 to 5 cut resumes.

## Outstanding drafts to apply to, 15 rows

These are the drafted rows in Notion as of this run. Each row has a CV and cover letter ready in the drafts folder, and each Notion row has the LinkedIn outreach contact and message stored where applicable. Warm outreach first, then application 48 hours later per the 28 July 2026 rule. Older drafts here have already crossed that window, so apply promptly on those.

From the 26 July 2026 run:
1. Freudenberg Technology Innovation, Masterarbeit, Data Science and Machine Learning im Spritzguss, Weinheim, StepStone
2. Airbus, Master Thesis, AI Suitability Evaluation for Modelica Physical Models, Hamburg, Xing
3. TK Elevator, Working Student, Data Analytics, Duesseldorf, StepStone
4. ROSEN Group, Masterarbeit, Process Mining, Lingen, Xing
5. Siemens Healthineers, Working Student, Data Science and AI for X-Ray Technology, Forchheim, LinkedIn
6. Avelios Medical, Working Student, Machine Learning, Muenchen, LinkedIn
7. SAP, Working Student, AI Engineering for Business Applications, Garching bei Muenchen, LinkedIn
8. 1&1 Mobilfunk, Werkstudent, AI und Data Automation Mobilfunk Rollout, Duesseldorf, StepStone
9. PMMG Group, Werkstudent, Process und Data Science, Muenchen, Indeed
10. GEA Hilge, Werkstudent, Data Analytics und AI, Bodenheim, Indeed

From the 27 July 2026 run:
11. Mercedes-Benz Tech Innovation, Werkstudent, Agentic AI und Multi-Agent-Systeme, Berlin, StepStone
12. Fraunhofer-Institut fuer Integrierte Schaltungen IIS, Praktikant Abschlussarbeit, Simulation und Machine Learning in der Robotik, Dresden, Xing
13. ANDREAS STIHL AG und Co. KG, Praktikum, Data Analytics und Machine Learning fuer Produktnutzungsdaten, Waiblingen, LinkedIn
14. YOONA Ventures GmbH, Werkstudent, AI Working Student Project-Based, Berlin, Indeed
15. Deutsche Telekom MMS GmbH, Werkstudent, AI Product Builder und KI gestuetzte Produktentwicklung, Dresden, Indeed

## Backlog gate math

The 28 July 2026 rule redefines the gate as follows. Under 8 drafted rows, the normal top 3 to 5 cut runs. At 8 to 10 drafted rows, the run caps at top 3. At 11 or more drafted rows, the run hard pauses. Notion says 15 drafted rows this morning, so the run pauses. Notion is the source of truth per the 14 July 2026 rule; the CSV read below confirms the same count of 15 as a cross check.

## Reconciliation notes

CSV rows counted, 112. Notion rows counted, 112. The one status drift found was Deutsche Bank, TDI Internship Frankfurt, where Notion carries "shortlisted but no interview" and the CSV still read "shortlisted". Per the 14 July 2026 rule Notion is authoritative for status, so the CSV was synced in place to carry the Notion value verbatim. No other drift rows were found. No Notion creates were needed this run since every CSV row already has a matching Notion row.

## Transparency block

Sources reachable this run, Notion query API returned 200 on the first call, CSV read locally. Tavily, Indeed, StepStone, Xing, LinkedIn Jobs, and company career pages were not queried because the hard pause skips the search step per the 28 July 2026 rule. Gmail draft created for this pause digest and addressed to rahulrawat2r@gmail.com.

No new CV, cover letter, or LinkedIn outreach was produced this run. No new rows were appended to applied-log.csv. No new Notion rows were created. The 15 drafted rows above stay untouched and continue to be Rah's backlog to work through.

## Next scheduled run

The next scheduled run will re-check the Notion drafted count first thing. If Rah has moved rows from drafted to applied on 5 or more entries by then, the backlog drops to 10 or below and the run will draft the top 3 under the soft cap. If Rah moves 8 or more entries out of drafted, the run resumes the normal top 3 to 5 cut. Until then every scheduled run will keep pausing to protect Rah from a compounding backlog.
