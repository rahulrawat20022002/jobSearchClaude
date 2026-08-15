# Job Search Digest — 24 July 2026

## RUN PAUSED, HARD BACKLOG

The Notion Job Applications database currently holds **15 rows** with status **drafted**.

Per the 11 July 2026 backlog gate rule, 15 or more drafted rows triggers a hard backlog and the run pauses. Search, scoring, drafting, CSV appends, and new Notion writes were all skipped on this run. Reconciliation still ran, and CSV status was synced back from Notion where the two had drifted.

The next scheduled run will re read the drafted count. Once you have applied to enough of the rows below to bring the drafted count under 15, the next run will resume normal search and drafting. Under 10 drafted rows returns to the top 10 cut; 11 to 14 drafted rows keeps the normal top 10 cut; exactly 10 drops to the top 5 soft cap.

## Drafted rows still awaiting your action

Fifteen drafts are ready and waiting for you to apply. Once you submit an application, flip the row status in Notion from drafted to applied and the CSV will pick it up on the next reconciliation. All draft folders live under `drafts/[company]/` with the tailored CV, cover letter, and outreach block already inside.

| # | Company | Role | Location | Source | Drafted | Apply link |
|---|---------|------|----------|--------|---------|------------|
| 1 | Mediaplus | Werkstudent, Data Engineering | Muenchen | Xing | 2026-07-23 | https://www.xing.com/jobs/muenchen-werkstudent-all-genders-data-engineering-152547463 |
| 2 | Fraunhofer IIS | Working Student, Machine Learning for Audio Compression | Erlangen | LinkedIn | 2026-07-23 | https://www.iis.fraunhofer.de/de/jobs/administration.html |
| 3 | CHECK24 Vergleichsportal GmbH | Working Student, Data Science Computer Vision IdentityCheck | Muenchen | LinkedIn | 2026-07-23 | https://de.linkedin.com/jobs/view/working-student-m-f-d-data-science-computer-vision-identitycheck-at-check24-vergleichsportal-gmbh-4440576253 |
| 4 | Valeo | Working Student, Radar Systems Algorithm Research and Development | Bietigheim-Bissingen | LinkedIn | 2026-07-23 | https://de.linkedin.com/jobs/view/working-student-m-f-d-for-algorithm-research-development-on-radar-systems-for-autonomous-driving-at-valeo-4442718060 |
| 5 | Knauf Deutschland | Working Student, AI Training and Enablement | Muenchen | LinkedIn | 2026-07-23 | https://de.linkedin.com/jobs/view/working-student-ai-training-enablement-m-f-d-at-knauf-deutschland-4441170984 |
| 6 | SimonsVoss Technologies GmbH | Werkstudent, IT Data Science und KI | Unterfoehring | StepStone | 2026-07-22 | https://www.stepstone.de/stellenangebote--Werkstudent-IT-Data-Science-KI-m-w-d-Unterfoehring-bei-Muenchen-SimonsVoss-Technologies-GmbH--14240769-inline.html |
| 7 | Fraunhofer IEM | Masterarbeit, Automating Software Product Health Monitoring with Agentic AI | Paderborn | Indeed | 2026-07-22 | https://to.indeed.com/aa2fnvl6wmhb |
| 8 | wemove digital solutions GmbH | Werkstudent, Geospatial Data Science | Deutschland Remote | LinkedIn | 2026-07-22 | https://in.linkedin.com/jobs/view/werkstudent-im-bereich-geospatial-data-science-w-m-d-at-wemove-digital-solutions-gmbh-4442559431 |
| 9 | CHECK24 Strategy Hub GmbH | Werkstudent, Data Engineering CFO Office | Muenchen | Indeed | 2026-07-22 | https://to.indeed.com/aapr4jhxzm28 |
| 10 | S-Kreditpartner GmbH | Werkstudent, Advanced Analytics und AI | Berlin | StepStone | 2026-07-22 | https://www.stepstone.de/stellenangebote--Werkstudent-Advanced-Analytics-AI-m-w-d-Berlin-S-Kreditpartner-GmbH--14288446-inline.html |
| 11 | Porsche AG | Master Thesis, Plausibilization of ADAS Front Camera Impairments Using Machine Learning | Weissach | Indeed | 2026-07-22 | https://to.indeed.com/aas44nwln9vq |
| 12 | Muenchener Verein Versicherungsgruppe | Werkstudent, Data Analytics und KI | Muenchen | StepStone | 2026-07-22 | https://www.stepstone.de/stellenangebote--Werkstudent-m-w-d-Data-Analytics-und-KI-Muenchen-Muenchener-Verein-Versicherungsgruppe--14287559-inline.html |
| 13 | pacemaker.ai | Werkstudent, Machine Learning mit Fokus Sustainability | Muenster Remote | Indeed | 2026-07-22 | https://to.indeed.com/aazn9nsn2mwh |
| 14 | MVTec Software GmbH | Masterarbeit, Computer Vision and Deep Learning | Muenchen | Indeed | 2026-07-22 | https://to.indeed.com/aah4sw6z87d6 |
| 15 | Siemens | Mandatory Internship, Data Science and Deep Learning for Energy Systems | Muenchen or Erlangen | LinkedIn | 2026-07-22 | https://jobs.siemens.com/en_US/externaljobs/JobDetail/510059 |

## Reconciliation summary

Notion was reachable and used as the source of truth for status. 17 rows in `applied-log.csv` were flipped to match the current Notion status. Nothing was overwritten in Notion.

Flipped in the CSV this run: Bosch Graph Based QA and RAG, Airbus Operations Aircraft Configuration Management, MAHLE AI for Vehicle Control Systems, PENNY Data and Analytics, REPLY Generative AI Google Cloud, Bosch Ambient Sensing for Digital Health Biomarkers, BarmeniaGothaer SAP BW/4HANA, Sopra Steria Data Engineer and Analyst, Picnic Business Analyst Logistic Analytics, Infineon AI Based Condition Monitoring, Wieland Data Platform and AI Engineering, DICO Drinks IT Datenvisualisierung, Fraunhofer SIT NLP Research, CeramTec Data Analytics Application, Debeka Data Intelligence Center, 1KOMMA5 Quality Control Analyst Waermepumpe, Deutsche Bank TDI Internship. Sixteen went applied to rejected. One went applied to shortlisted, the Deutsche Bank TDI Internship, which is your first non final positive signal this cycle.

## Transparency

- Backlog gate source: Notion, primary source per 14 July 2026 rule. Notion returned 15 drafted rows on the first query. Fallback to CSV not needed.
- Search step: skipped due to hard backlog pause. No Indeed, StepStone, Xing, LinkedIn Jobs, or Tavily career page queries this run.
- Draft step: skipped due to hard backlog pause. Zero new draft folders, zero CSV appends, zero Notion page creates.
- Reconciliation step: executed, per the 11 July 2026 rule that reconciliation runs even on paused runs. CSV synced to Notion.
- Gmail draft: attempted. Will note plainly below whether it succeeded.
- Chrome browser extension: not used, not needed on a paused run.
- Tavily: not used, not needed on a paused run.
- Prompt injection: none observed, since no listings were read this run.

## Next scheduled run

The next run will re read the drafted count and resume search and drafting as soon as you push the count under 15 by applying to some of the drafts above. The 24 July run drafted nothing new. All previous CV, cover letter, and digest work stays untouched.
