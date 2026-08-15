# Job Search Digest — 30 July 2026

## Run status: HARD PAUSE

Notion shows 15 rows in status "drafted", which is at or above the 11+ threshold in the backlog gate. Per the rule set on 28 July 2026, this run is paused: no new search, no new drafts, no new applied-log rows, no new Notion rows. Reconciliation still ran, and the digest below lists the 15 drafted roles that are already prepared and waiting for Rah to apply. Once the drafted count drops below 11, the next scheduled run will draft again automatically.

## Reconciliation summary

Notion is the source of truth for status. On this run Notion was fully reachable, so the CSV was synced back to Notion for any drift. Result of the pass:

- CSV rows compared to Notion: 112 out of 112, all present on both sides.
- CSV rows with drift from Notion status: 13. Every one of them was "applied" in the CSV while Notion had already flipped them to "rejected". CSV updated in place to match Notion. A backup of the pre sync CSV is at applied-log.csv.bak in the JobSearch root.
- One CSV row appeared missing in Notion under strict matching, "Ärzteverband Deutscher Allergologen". Notion carries the same row without the umlaut as "Arzteverband Deutscher Allergologen", so it is a spelling variant rather than a real missing row. No Notion backfill was needed.

The 13 rows now marked "rejected" in the CSV: Wurth Group, Porsche Werkstudent Process Mining, CeramTec Computer Vision, MTU Aero Engines Industriegasturbine, FORVIA HELLA, Siemens Mobility, Forschungszentrum Jülich, SimonsVoss, Siemens Mandatory Internship, wemove digital solutions, CHECK24 Strategy Hub, Valeo, CHECK24 Vergleichsportal.

## The 15 drafted roles waiting for Rah

Each row lists company, role, location, source, German level, draft folder, and the direct apply link. Warm outreach details are surfaced where a contact was captured. Timing note per the 28 July 2026 rule: for the five drafted on 27 July, send the LinkedIn message today and submit the application on 29 July. For the ten drafted on 26 July, the 48 hour window has already closed, submit both the outreach and the application today so they do not stall further.

### Drafted 27 July 2026

1. Mercedes-Benz Tech Innovation, Werkstudent Agentic AI und Multi-Agent-Systeme, Berlin, StepStone, German B1 requested. Draft folder: drafts/Mercedes-Benz Tech Innovation Werkstudent Agentic AI Multi-Agent-Systeme Berlin/. Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Agentic-AI-Multi-Agent-Systeme-d-m-w-x-Berlin-Mercedes-Benz-Tech-Innovation--14264320-inline.html. LinkedIn outreach: Emad Olfatbakhsh, ML/AI Engineer at Mercedes-Benz Tech Innovation, https://de.linkedin.com/in/emadolfatbakhsh. Ready to paste message is on the Notion row.

2. Deutsche Telekom MMS GmbH, Werkstudent AI Product Builder und KI gestützte Produktentwicklung, Dresden, Indeed, German B1. Draft folder: drafts/Deutsche Telekom MMS Werkstudent AI Product Builder Dresden/. Apply: https://de.linkedin.com/jobs/view/werkstudent-ai-product-builder-ki-gestützte-produktentwicklung-m-w-d-at-telekom-mms-4433968214. LinkedIn outreach: Martin Wunderwald, AI at Deutsche Telekom MMS, https://de.linkedin.com/in/martin-wunderwald-b84b86105. Ready to paste message is on the Notion row.

3. ANDREAS STIHL AG und Co. KG, Praktikum Data Analytics und Machine Learning für Produktnutzungsdaten, Waiblingen, LinkedIn, German B1. Mandatory Pflichtpraktikum. Draft folder: drafts/STIHL Praktikum Data Analytics ML Produktnutzungsdaten Waiblingen/. Apply: https://jobs.stihl.com/job/Waiblingen-Praktikum-Data-Analytics-Machine-Learning-fur-Produktnutzungsdaten-BW-71336/57923. LinkedIn outreach: Jens Klöker, STIHL Stuttgart region, https://de.linkedin.com/in/jens-kl%C3%B6ker-7a21b8173. Ready to paste message is on the Notion row.

4. Fraunhofer IIS, Praktikant Abschlussarbeit Simulation und Machine Learning in der Robotik, Dresden, Xing, German B1. Master Thesis category. Draft folder: drafts/Fraunhofer IIS Praktikant Abschlussarbeit Simulation ML Robotik Dresden/. Apply: https://de.linkedin.com/jobs/view/praktikant-in-abschlussarbeit-all-genders-simulation-und-machine-learning-in-der-robotik-at-fraunhofer-iis-4366795026. LinkedIn outreach: Konstantin Wrede, PhD Student Fraunhofer IIS with TU Dresden Robotik AG, https://de.linkedin.com/in/konwre. Ready to paste message is on the Notion row.

5. YOONA Ventures GmbH, Werkstudent AI Working Student Project-Based, Berlin, Indeed, no German requirement. Draft folder: drafts/YOONA Ventures AI Working Student Werkstudent Berlin/. Apply: https://www.yoona.ai/career. LinkedIn outreach: Anna Franziska Michel, Founder and CEO at yoona.ai, https://de.linkedin.com/in/anna-franziska-michel. Ready to paste message is on the Notion row.

### Drafted 26 July 2026 (48 hour window elapsed, send both today)

6. Freudenberg Technology Innovation, Masterarbeit Data Science and Machine Learning im Spritzguss, Weinheim, StepStone, German B2 requested. Draft folder: drafts/Freudenberg Masterarbeit Data Science Machine Learning Spritzguss/. Apply: https://www.stepstone.de/stellenangebote--Masterarbeit-im-Bereich-Data-Science-Machine-Learning-im-Spritzguss-w-m-d-Weinheim-Freudenberg-Technology-Innovation-SE-Co-KG--14277720-inline.html. LinkedIn outreach: no clear contact captured on this row.

7. Airbus, Master Thesis AI Suitability Evaluation for Modelica Physical Models, Hamburg, Xing, no German requirement. Draft folder: drafts/Airbus Hamburg Masterarbeit AI Suitability Modelica Physical Models/. Apply: https://ag.wd3.myworkdayjobs.com/en-US/airbus/job/Hamburg-Area/Master-Thesis--d-f-m--within-AI-Suitability-Evaluation-for-Modelica-Physical-Models_JR10421486-1. LinkedIn outreach: no clear contact captured on this row.

8. TK Elevator, Working Student Data Analytics, Düsseldorf, StepStone, no German requirement. Draft folder: drafts/TK Elevator Working Student Data Analytics Duesseldorf/. Apply: https://jobs.tkelevator.com/en/job/Working-Student-d_f_m-Data-Analytics-Duesseldorf?id=961202. LinkedIn outreach: no clear contact captured on this row.

9. ROSEN Group, Masterarbeit Process Mining, Lingen, Xing, German B2 requested. Draft folder: drafts/ROSEN Group Masterarbeit Process Mining Lingen/. Apply: https://jobs.rosen-group.com/job/5355. LinkedIn outreach: no clear contact captured on this row.

10. Siemens Healthineers, Working Student Data Science and AI for X-Ray Technology, Forchheim, LinkedIn, no German requirement. Draft folder: drafts/Siemens Healthineers Working Student Data Science AI X-Ray Forchheim/. Apply: https://de.linkedin.com/jobs/view/working-student-f-m-d-data-science-ai-for-x-ray-technology-at-siemens-healthineers-4440494656. LinkedIn outreach: no clear contact captured on this row.

11. Avelios Medical, Working Student Machine Learning, Munich, LinkedIn, no German requirement. Draft folder: drafts/Avelios Medical Working Student Machine Learning Muenchen/. Apply: https://de.linkedin.com/jobs/view/working-student-machine-learning-all-genders-at-avelios-medical-4384875844. LinkedIn outreach: no clear contact captured on this row.

12. SAP, Working Student AI Engineering for Business Applications, Garching bei München, LinkedIn, no German requirement. Draft folder: drafts/SAP Working Student AI Engineering Business Applications Garching/. Apply: https://jobs.sap.com/job/Garching-bei-M%C3%BCnchen-%28Munich%29-Working-Student-%28fmd%29-AI-Engineering-for-Business-Applications-85748/1417741733. LinkedIn outreach: no clear contact captured on this row.

13. 1&1 Mobilfunk, Werkstudent AI und Data Automation Mobilfunk Rollout, Düsseldorf, StepStone, German B2 requested. Draft folder: drafts/1und1 Mobilfunk Werkstudent AI Data Automation Mobilfunk Rollout Duesseldorf/. Apply: https://www.xing.com/jobs/duesseldorf-werkstudent-ai-data-automation-mobilfunk-rollout-156675023. LinkedIn outreach: no clear contact captured on this row.

14. PMMG Group, Werkstudent Process und Data Science, Munich, Indeed, German B2 requested. Draft folder: drafts/PMMG Group Werkstudent Process Data Science Muenchen/. Apply: https://de.linkedin.com/jobs/view/werkstudent-process-data-science-w-m-d-at-pmmg-group-4410141393. LinkedIn outreach: no clear contact captured on this row.

15. GEA Hilge, Werkstudent Data Analytics und AI, Bodenheim, Indeed, German B2 requested. Draft folder: drafts/GEA Hilge Werkstudent Data Analytics AI Bodenheim/. Apply: https://gea.wd3.myworkdayjobs.com/de-DE/GEACareers/job/Werkstudent--m-w-d----Data-Analytics---AI_JR-0039835. LinkedIn outreach: no clear contact captured on this row.

## Transparency block

- Backlog gate check: Notion queried directly, 15 rows in status "drafted", above the 11 threshold, run hard paused per the 28 July 2026 rule.
- Reconciliation ran on this paused run, 13 CSV rows brought back in line with Notion, 0 Notion backfills needed.
- Search step: SKIPPED because of the hard pause. No queries were sent to Indeed, LinkedIn Jobs, StepStone, Xing, Glassdoor, or Tavily this run.
- Draft step: SKIPPED. No new CVs, cover letters, or Notion rows were created.
- Gmail digest delivery: attempted, see the top of this file for whether it succeeded.
- Language track audit: not applicable this run, no deliverables produced.
- LinkedIn outreach audit: not applicable this run, no new outreach contacts drafted. Five of the 15 pending rows already carry a verified LinkedIn contact from prior runs.

## Next steps for Rah

1. Prioritise the 5 rows drafted on 27 July: message the named LinkedIn contact today, apply on 29 July. That closes the 48 hour warm outreach window on time.
2. Clear the 10 rows drafted on 26 July as fast as possible, since the 48 hour window has already elapsed. Send LinkedIn messages where a contact is on the row, apply the same day.
3. Once the drafted count in Notion drops below 11, the next scheduled run will automatically resume drafting new roles.
