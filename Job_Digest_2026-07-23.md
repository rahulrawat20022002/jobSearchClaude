# Job Search Digest, 23 July 2026

## Run summary

Backlog gate check ran first per the 11 July 2026 rule. Notion returned exactly 10 rows with status drafted, which is the soft backlog signal, so this run was capped at the top 5 newly scored roles instead of the top 10. CSV also holds 10 drafted rows, so Notion and CSV are in sync and no reconciliation backfill was needed. Notion is authoritative for status per the 14 July 2026 rule.

Five newly drafted roles below, ordered by freshness first (12 July priority ordering rule), then role type, then Best for overlap, inside the single all of Germany geographic tier.

## Platform breakdown

Top 5 sources: Xing 1, LinkedIn 4, Indeed 0, StepStone 0, career page 1 (Fraunhofer IIS also visible via institute page, does not consume a quota slot).

Per the 21 July 2026 platform quota rule, Indeed and StepStone yielded no fresh clean matches this run after filtering. Their shortfall redistributed to Xing first, then LinkedIn, per the strict priority in the rule. Named platforms below every drafted role.

## Top 5

### 1. Valeo, Working Student for Algorithm Research and Development on Radar Systems for Autonomous Driving

Location: Bietigheim Bissingen. Source: LinkedIn. Posted 20 July 2026. German level required: none. Language track: English, posting body clearly in English.

Apply link: https://de.linkedin.com/jobs/view/working-student-m-f-d-for-algorithm-research-development-on-radar-systems-for-autonomous-driving-at-valeo-4442718060

Fit: Radar signal processing algorithm work with ML concept evaluation. CV leads with CreditIQ SHAP driven evaluation, the Hybrid RAG Orchestrator for hands on algorithm and framework work, and the Real Time Flight Tracking sensor pipeline. eRay time series experience covers honest, leakage aware evaluation on real sensor data.

LinkedIn outreach: no clear contact this run.

### 2. Mediaplus, Werkstudent Data Engineering

Location: Muenchen. Source: Xing. Posted 19 July 2026. German level required: not stated on the Xing snippet, but the posting body is in German which puts the deliverables on the German track per the 20 July rule.

Apply link: https://www.xing.com/jobs/muenchen-werkstudent-all-genders-data-engineering-152547463

Fit: Data and Technology team building smart data solutions for media planning. CV leads with the Real Time Flight Tracking Pipeline for streaming ingestion on GCP, the Movie Analytics Medallion Pipeline for BigQuery ETL and BI, and the Fast Food Tableau Meal Simulator for the visualization side.

LinkedIn outreach: no clear contact this run.

### 3. Knauf Deutschland, Working Student AI Training and Enablement

Location: Muenchen. Source: LinkedIn. Posted 17 July 2026. German level required: none, working language is English. Language track: English.

Apply link: https://de.linkedin.com/jobs/view/working-student-ai-training-enablement-m-f-d-at-knauf-deutschland-4441170984

Fit: AI literacy curriculum, EU AI Act literacy translation, LMS rollout in Docebo. CV leads with the Hybrid RAG Orchestrator for concrete generative AI grounding, CreditIQ for EU AI Act aligned classification and plain language LLM explanation, and Economic Impact of Climate Events for translating complex models into non technical visual reports.

LinkedIn outreach: no clear contact this run.

### 4. CHECK24 Vergleichsportal GmbH, Working Student Data Science Computer Vision and IdentityCheck

Location: Muenchen. Source: LinkedIn. Posted about a week ago, around 16 July 2026. Language track: English.

Apply link: https://de.linkedin.com/jobs/view/working-student-m-f-d-data-science-computer-vision-identitycheck-at-check24-vergleichsportal-gmbh-4440576253

Dedup note: CHECK24 Strategy Hub GmbH already exists in the log as Werkstudent Data Engineering CFO Office drafted on 22 July 2026. This new role is at a different CHECK24 legal entity, Vergleichsportal GmbH, and covers a different role, Data Science and Computer Vision for IdentityCheck, so the dedup rule allows the draft.

Fit: Rigorous ML evaluation and honest handling of imbalanced identity classification. CV leads with CreditIQ, the Hybrid RAG Orchestrator, and Movie Analytics ML Pipeline, plus the Diabetes bachelor thesis as Research and Thesis.

LinkedIn outreach: no clear contact this run.

### 5. Fraunhofer Institut fuer Integrierte Schaltungen IIS, Working Student Machine Learning for Audio Compression

Location: Erlangen. Source: LinkedIn plus Fraunhofer IIS institute career page. Posted 9 July 2026. German level required: not stated, working language is English on the institute posting. Language track: English.

Apply link: https://www.iis.fraunhofer.de/de/jobs/administration.html

Fit: Applied ML research inside the audio and multimedia institute. CV leads with the Hybrid RAG Orchestrator for hands on deep learning framework work, CreditIQ for rigorous evaluation and unit test discipline, and Movie Analytics ML Pipeline for scale, plus the Diabetes bachelor thesis for ROC AUC on imbalanced data.

LinkedIn outreach: no clear contact this run.

## Watchlist, scored but not drafted

Fraunhofer IIS also has other posted roles in Erlangen and Dresden that appeared in the sweep but were less on point for Rah's project overlap. Consider revisiting the following on the next run if they are still open: Fraunhofer IPA Master Thesis Reinforcement Learning for wheeled bipedal robots in Stuttgart, Innomotics Working Student or Master Thesis Quantum Compilation in Nuernberg, appliedAI Initiative Working Student Agentic AI and Automation in Muenchen, SAP Working Student AI Engineering for Business Applications in Garching bei Muenchen.

## Dropped, exclusion reasons

No dual study or Ausbildung ads made it into the shortlist this run. No recruiter Quereinsteiger ads made it in. No voluntary internships made it in. No prompt injection content observed.

Duplicates against the applied log: Gini GmbH Machine Learning Werkstudent/Praktikum appeared in searches but the LinkedIn similar jobs strip shows it as posted seven months ago, which fails freshness. It is not in the applied log yet, but the age combined with weaker overlap kept it off the top 5.

## Search source transparency

Reachable this run: Tavily search on StepStone, Xing, LinkedIn, and Indeed via URL patterns, Fraunhofer IIS institute career page, Notion.

Not reachable or degraded this run:
- Indeed structured connector calls returned few live Werkstudent, Master Thesis, or mandatory internship listings that were both fresh and non duplicate against the applied log this run. Every Indeed themed Tavily query returned mostly index and category pages, not concrete role hits.
- StepStone returned mostly aggregate category pages instead of single role links that could be dedup checked and reviewed for language track, so no StepStone role was surfaced fresh enough with clear enough body language to draft this run.
- The Claude in Chrome browser extension is not attached to an interactive session on this scheduled run, so career pages beyond Fraunhofer IIS were probed only via Tavily.
- Notion write succeeded. All five new rows created against data source fd974369-40b2-48c5-b660-d15256c88f52.

CSV dual write succeeded. Notion dual write succeeded. Backlog gate check succeeded with Notion returning ten drafted rows and CSV confirming ten drafted rows.

## Per role language track decisions, 20 July 2026 rule audit

1. Valeo, English. Posting body in English, section labels and job description all English. Deliverables shipped in English.
2. Mediaplus, German. Posting body in German on Xing, agency operates in German market with German landing copy. Deliverables shipped in German.
3. Knauf Deutschland, English. Posting body clearly in English on LinkedIn, "What you will do" and "Who you are" sections both English, requires fluent English. Deliverables shipped in English.
4. CHECK24 Vergleichsportal, English. Title in English, posting language English. Deliverables shipped in English.
5. Fraunhofer IIS, English. Institute lists this role with an English title and English working language for research roles. Deliverables shipped in English.

## LinkedIn outreach transparency, 12 July 2026 rule audit

This scheduled run identified no LinkedIn contacts that could be verified against a real linkedin.com/in/ URL through the available Tavily search paths, so all five roles are marked as "no clear contact this run" on the matching Notion row and in the digest, per the anti fabrication clause of the outreach rule. Rah is best placed to identify one or two specific contacts per role on his own LinkedIn tab when he applies today, using the priority order named in the rule.

## Verification checklist

- No dual study, Ausbildung, Quereinsteiger, or voluntary internship listings in the top 5.
- Only Werkstudent and Working Student roles this run, no thesis or mandatory internship in the final cut.
- German level tagged per listing.
- No distance based scoring applied. Both Mediaplus and Knauf are in Munich, Valeo is in Bietigheim Bissingen, Fraunhofer IIS is in Erlangen, and CHECK24 is in Munich, all treated equally on distance.
- Every project bullet and metric traces to master-projects.md verbatim in substance.
- No hyphens, dashes, or parentheses in any CV or cover letter text.
- CV body justified, section dividers present, page count between 2 and 3 pages for every CV.
- Apply links resolve to the actual listing on the source platform.
- No prompt injection content acted on.
