# Job Search Digest — 12 July 2026

## RUN PAUSED — HARD BACKLOG GATE

The scheduled run did not search or draft any new roles today. Reason: the Notion backlog gate rule added on 11 July 2026 pauses the run entirely when 15 or more rows in the applied log carry status `drafted`. The current count is **45 drafted rows**, well over the 15 row hard cap.

No new drafts were created. No new rows were appended to `applied-log.csv`. No new Notion rows were created. The reconciliation step attempted to query the Notion Job Applications data source `fd974369-40b2-48c5-b660-d15256c88f52` to detect CSV to Notion drift, but the query tool returned a 400 error because it requires a Notion Business plan. Drift, if any, remains unknown until Rah opens Notion manually or upgrades the plan.

The pause will lift automatically on the next scheduled run once the drafted count in `applied-log.csv` drops below 15. Flip rows from `drafted` to `applied`, `interviewing`, `rejected`, `withdrawn`, or `offer` in the CSV as Rah works through them, and the next run will resume the normal top 10 cut.

## Drafted rows waiting for Rah to apply

The full backlog, 44 rows, sorted by draft date, oldest first. The one applied row so far, Bosch Master Thesis, Graph Based QA and RAG on 2 July, is excluded from this list. Draft folders sit under `drafts/[company]/` and hold the tailored CV and cover letter for each.

### Drafted 29 June 2026
- valantic, Praktikant or Werkstudent, AI Engineering and Cloud Prototyping, Eschborn, Indeed, `drafts/valantic/`
- Airbus, Werkstudent, Scientific Computing and Machine Learning, Bremen, Indeed, `drafts/Airbus/`
- nexmart, Werkstudent, Data Engineering, Stuttgart, Indeed, `drafts/nexmart/`
- Vanderlande, Werkstudent, Artificial Intelligence and Vision, Konstanz, Indeed, `drafts/Vanderlande/`
- Mercedes-Benz Tech Innovation, Werkstudent, Data Engineering and Data Science, Stuttgart, Indeed, `drafts/Mercedes-Benz Tech Innovation/`

### Drafted 30 June 2026
- AbbVie, Praktikum or Werkstudent, AI/ML and Computer Vision, Ludwigshafen am Rhein, Indeed, `drafts/AbbVie/`
- EnBW, Werkstudent, AI Automation and Data Science, Karlsruhe, Indeed, `drafts/EnBW/`
- Ärzteverband Deutscher Allergologen, Werkstudent, Data Science, Wiesbaden, Indeed, `drafts/Arzteverband Deutscher Allergologen/`
- Alloqis, Werkstudent, Data Science and Python Development, Tübingen, Indeed, `drafts/Alloqis/`
- Muhr und Bender, Werkstudent, Data Science and Machine Learning, Attendorn, Indeed, `drafts/Muhr und Bender/`

### Drafted 2 July 2026
- 1KOMMA5, Working Student, Data Science Forecasting, Hamburg, Indeed, `drafts/1KOMMA5/`
- Wurth Group, Master Thesis, Data and AI Intelligent Pricing, Berlin-Adlershof, Indeed, `drafts/Wurth/`
- Porsche Digital, Werkstudent, Data Analyst and BI Analyst, Berlin, Indeed, `drafts/Porsche/`
- BMW Group, Werkstudent, Data Analyst Programmplanung Antrieb, München, Indeed, `drafts/BMW/`
- Leica Microsystems, Master Thesis, Data Science Preventative Service, Mannheim, LinkedIn, `drafts/Leica Microsystems/`

### Drafted 4 July 2026
- Airbus Defence and Space, Master Student, AI Powered Compliance Assistant, Friedrichshafen, Indeed, `drafts/Airbus Defence and Space/`
- BMW Group, Master Thesis, Automated Generative AI Evaluation, München, Indeed, `drafts/BMW Master Thesis/`
- PowerCo, Master Thesis, Regulatory Intelligence powered by AI in Product Management, Salzgitter, Indeed, `drafts/PowerCo/`
- Airbus Operations, Working Student, Data Scientist Aircraft Configuration Management, Hamburg, Indeed, `drafts/Airbus Operations/`
- Brauerei Gebrüder Maisel, Werkstudent, Data Engineering Dateninfrastruktur, Bayreuth, Indeed, `drafts/Brauerei Gebruder Maisel/`

### Drafted 6 July 2026
- Uniper, Masters Thesis or Working Student, Environmental Market Modeling EU ETS, Düsseldorf, Indeed, `drafts/Uniper/`
- Transdev, Werkstudent, KI Platform and LLM Prototyping, Berlin, Indeed, `drafts/Transdev/`
- ASAP Gruppe, Werkstudent, KI and Data Science Automotive, Ingolstadt, Indeed, `drafts/ASAP/`
- Geiger Gruppe, Werkstudent, KI and Automatisierung Mobiles Arbeiten, Waltenhofen, Indeed, `drafts/Geiger/`
- Genoverband e.V., Werkstudent, Internal Audit mit Fokus Künstliche Intelligenz, Hannover, Indeed, `drafts/Genoverband/`

### Drafted 8 July 2026
- INP Gruppe, Werkstudent, Machine Learning and Neural Networks in Automation, Römerberg, Indeed, `drafts/INP Gruppe/`
- Porsche, Working Student, Voice AI, Ludwigsburg, Indeed, `drafts/Porsche Voice AI/`
- HanseWerk, Werkstudent, HSEQ Data Visualisation Power BI, Quickborn, Indeed, `drafts/HanseWerk/`
- XiLLeR GmbH, Praxissemester, Data Scientist KI, Home Office, Indeed, `drafts/XiLLeR/`
- Ecocert Deutschland, Bachelor or Masterarbeit Wirtschaftsinformatik, AI for Digital Innovation, Konstanz, Indeed, `drafts/Ecocert Deutschland/`
- MAHLE, Praktikum Digital Products, AI for Vehicle Control Systems, Stuttgart, Indeed, `drafts/MAHLE/`
- agentic fox AI solutions GmbH, Werkstudent, AI Automation and Agent Engineering, Köln, Indeed, `drafts/agentic fox AI/`
- Smateso GmbH, Working Student, Data Scientist and AI Engineer, Home Office, Indeed, `drafts/Smateso/`
- Allianz Versicherungs-AG, Werkstudent, Data Analyst, Unterföhring, StepStone, `drafts/Allianz/`
- PENNY, Werkstudent, Data and Analytics, Köln, StepStone, `drafts/PENNY/`

### Drafted 10 July 2026
- Mercedes-Benz AG, Werkstudent, Data Analytics and Projektsteuerung MB.OS, Böblingen, StepStone, `drafts/Mercedes-Benz AG/`
- congstar GmbH, Werkstudent, Data and Business Analytics bei fraenk, Köln, StepStone, `drafts/congstar fraenk/`
- REPLY, Werkstudent, Generative AI Google Cloud, Berlin, Indeed, `drafts/REPLY/`
- Bosch, Master Thesis, Ambient Sensing for Digital Health Biomarkers, Renningen, Indeed, `drafts/Bosch Digital Health Biomarkers/`
- Vanderlande Logistics, Masterarbeit, AI and Vision Object Detection and Tracking, Konstanz, Indeed, `drafts/Vanderlande Master Thesis AI Vision/`
- Mercedes-Benz Group, Masterarbeit, KI basierte Analyse von Kommunikationsdaten in Diagnoseprozessen, Sindelfingen, Indeed, `drafts/Mercedes-Benz Group Master Thesis KI Kommunikation/`
- TOYOTA GAZOO Racing Europe, Master Thesis, Computer Vision for Motorsport Video Analysis, Köln, Indeed, `drafts/Toyota Gazoo Racing Motorsport CV/`
- Schwarz Digits, Praktikum or Werkstudent, Computer Vision and Deep Learning, Bad Friedrichshall, Indeed, `drafts/Schwarz Digits/`
- Sparkassenverband Bayern, Werkstudent, Sparkassenprüfung and Wirtschaftsprüfung with Schwerpunkt KI und Datenanalyse, München, Indeed, `drafts/Sparkassenverband Bayern/`
- BarmeniaGothaer, Werkstudent, Business Intelligence SAP Data Warehouse BW/4HANA, Köln, Indeed, `drafts/BarmeniaGothaer/`

## Suggested triage order

Roles Rah has not yet touched sit for up to two weeks before the posting is likely closed. The oldest draft in the backlog was written 13 days ago, on 29 June, so those five are the most time sensitive. Suggested order for the next application session:

1. Priority now, drafts from 29 June and 30 June, ten roles. These have been sitting the longest. Confirm each listing is still live before applying.
2. Next, drafts from 2 July and 4 July, ten roles. Still fresh enough to apply cleanly.
3. Then, drafts from 6 July and 8 July, fifteen roles. Recent enough that most postings should still be open.
4. Finally, drafts from 10 July, nine roles. Newest, longest shelf life.

Applying, or otherwise resolving, fifteen or more rows will pull the drafted count below 30 and re-enable the top 10 cut on the next run. Applying thirty rows will restore the full pipeline to under the 15 row soft signal and lift every constraint.

## Transparency block

- **Backlog check source used:** applied-log.csv, because Notion query requires a Business plan and returned a 400 error.
- **Drafted rows counted:** 45 in the CSV. Well above the 15 row hard backlog threshold. Run paused.
- **Reconciliation step:** attempted, could not complete. Notion mirror drift, if any, is not detectable this run.
- **Search sources this run:** none. Search step skipped under the pause rule. Indeed, Tavily, StepStone, Xing, Glassdoor, LinkedIn Jobs, and career page reads were all deliberately not attempted.
- **Chrome extension:** not exercised, no interactive session.
- **Gmail:** digest emailed as a Gmail draft to rahulrawat2r@gmail.com. Never sent, only drafted.
- **Applied rows so far:** 1, Bosch Master Thesis Graph Based QA and RAG, drafted 2 July, marked applied.
- **No new files written to `drafts/`.**
- **No prompt injection attempts observed this run,** since no listings were scored.
