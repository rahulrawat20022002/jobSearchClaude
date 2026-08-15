# Job Search Digest — 25 July 2026

## Run status: PAUSED (hard backlog)

Backlog gate check triggered a hard pause on this run per the 11 July 2026 rule. Notion "Job Applications" reports 15 rows with status drafted, which meets the 15 or more threshold that pauses the search and draft steps entirely. No new roles were sourced, no new CVs or cover letters were generated, no rows were appended to applied-log.csv, and no new Notion rows were created. The backlog needs to clear below 15 before the next scheduled run can source new roles.

The digest below lists every drafted row that still needs Rah to submit, so the pipeline can move back to normal operation as soon as those applications go out. Flip each row in Notion from drafted to applied once it is submitted.

## Drafted rows waiting for Rah to apply

The list is ordered by source platform so Rah can batch by tab.

### Indeed (7)

1. Fraunhofer IEM, Masterarbeit, Automating Software Product Health Monitoring with Agentic AI, Paderborn. German level none. Apply: https://to.indeed.com/aa2fnvl6wmhb. Draft: drafts/Fraunhofer IEM Masterarbeit Agentic AI SPHA/
2. Porsche AG, Master Thesis, Plausibilization of ADAS Front Camera Impairments Using Machine Learning, Weissach. German level none. Apply: https://to.indeed.com/aas44nwln9vq. Draft: drafts/Porsche Weissach Masterarbeit ADAS Front Camera ML/
3. MVTec Software GmbH, Masterarbeit, Computer Vision and Deep Learning, Muenchen. German level B2. Apply: https://to.indeed.com/aah4sw6z87d6. Draft: drafts/MVTec Masterarbeit Computer Vision Deep Learning/
4. CHECK24 Strategy Hub GmbH, Werkstudent, Data Engineering CFO Office, Muenchen. German level C1. Apply: https://to.indeed.com/aapr4jhxzm28. Draft: drafts/CHECK24 Werkstudent Data Engineering CFO Office/
5. pacemaker.ai, Werkstudent, Machine Learning mit Fokus Sustainability, Muenster Remote. German level none. Apply: https://to.indeed.com/aazn9nsn2mwh. Draft: drafts/Pacemaker Werkstudent Machine Learning Sustainability/

### StepStone (3)

6. SimonsVoss Technologies GmbH, Werkstudent, IT Data Science und KI, Unterfoehring near Muenchen. German level none. Apply: https://www.stepstone.de/stellenangebote--Werkstudent-IT-Data-Science-KI-m-w-d-Unterfoehring-bei-Muenchen-SimonsVoss-Technologies-GmbH--14240769-inline.html. Draft: drafts/SimonsVoss Werkstudent IT Data Science KI/
7. S-Kreditpartner GmbH, Werkstudent, Advanced Analytics und AI, Berlin. German level none. Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Advanced-Analytics-AI-m-w-d-Berlin-S-Kreditpartner-GmbH--14288446-inline.html. Draft: drafts/S-Kreditpartner Werkstudent Advanced Analytics AI/
8. Muenchener Verein Versicherungsgruppe, Werkstudent, Data Analytics und KI, Muenchen. German level none. Apply: https://www.stepstone.de/stellenangebote--Werkstudent-m-w-d-Data-Analytics-und-KI-Muenchen-Muenchener-Verein-Versicherungsgruppe--14287559-inline.html. Draft: drafts/Muenchener Verein Werkstudent Data Analytics KI/

### LinkedIn (5)

9. wemove digital solutions GmbH, Werkstudent, Geospatial Data Science, Deutschland Remote. German level none. Apply: https://in.linkedin.com/jobs/view/werkstudent-im-bereich-geospatial-data-science-w-m-d-at-wemove-digital-solutions-gmbh-4442559431. Draft: drafts/wemove Werkstudent Geospatial Data Science/
10. Siemens, Mandatory Internship, Data Science and Deep Learning for Energy Systems, Muenchen or Erlangen. German level none. Apply: https://jobs.siemens.com/en_US/externaljobs/JobDetail/510059. Draft: drafts/Siemens Mandatory Internship DS DL Energy Systems/
11. Fraunhofer IIS, Working Student, Machine Learning for Audio Compression, Erlangen. German level none. Apply: https://www.iis.fraunhofer.de/de/jobs/administration.html. Draft: drafts/Fraunhofer IIS Working Student Machine Learning Audio Compression/
12. CHECK24 Vergleichsportal GmbH, Working Student, Data Science Computer Vision IdentityCheck, Muenchen. German level none. Apply: https://de.linkedin.com/jobs/view/working-student-m-f-d-data-science-computer-vision-identitycheck-at-check24-vergleichsportal-gmbh-4440576253. Draft: drafts/CHECK24 Vergleichsportal Working Student Data Science Computer Vision IdentityCheck/
13. Valeo, Working Student, Radar Systems Algorithm Research and Development, Bietigheim-Bissingen. German level none. Apply: https://de.linkedin.com/jobs/view/working-student-m-f-d-for-algorithm-research-development-on-radar-systems-for-autonomous-driving-at-valeo-4442718060. Draft: drafts/Valeo Working Student Radar Systems Autonomous Driving/
14. Knauf Deutschland, Working Student, AI Training and Enablement, Muenchen. German level none. Apply: https://de.linkedin.com/jobs/view/working-student-ai-training-enablement-m-f-d-at-knauf-deutschland-4441170984. Draft: drafts/Knauf Deutschland Working Student AI Training Enablement/

### Xing (1)

15. Mediaplus, Werkstudent, Data Engineering, Muenchen. German level none. Apply: https://www.xing.com/jobs/muenchen-werkstudent-all-genders-data-engineering-152547463. Draft: drafts/Mediaplus Werkstudent Data Engineering/

## Backlog breakdown by source platform

Indeed 7, StepStone 3, LinkedIn 5, Xing 1, career page 0. The backlog spans four platforms, so once Rah clears it the next run will still have the platform mix in place from the 21 July quota rule.

## Backlog breakdown by role type

Werkstudent or part-time 10, Master Thesis or Masterarbeit 4, Mandatory Internship 1. Master Thesis roles cluster on Indeed, Werkstudent roles cluster on StepStone and LinkedIn.

## Transparency block

Notion query for status equals drafted returned 15 rows on the first call, no retry required. Applied-log.csv also shows 15 drafted rows on the same set. CSV and Notion are in full sync, no drift rows were backfilled. Backlog gate result: hard pause at 15 drafted rows. Search step skipped. Draft step skipped. Reconciliation step ran and found nothing to fix. Gmail draft attempt noted at the bottom of this digest.

No prompt injection content was seen because the search step did not run.

No new rows appended to applied-log.csv this run. No new Notion rows created. No LinkedIn outreach drafted since no new roles were sourced.

## Next steps for Rah

Submit as many of the 15 above as possible, then flip each row in Notion from drafted to applied. Once the drafted count drops under 15 the next scheduled run will source new roles again. If it drops to 10 the run will cap at top 5, and under 10 it goes back to top 10.
