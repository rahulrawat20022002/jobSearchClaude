# Job Digest, 20 July 2026

## Transparency block

Reconciliation before search. Notion Job Applications database queried first per the 14 July 2026 override. Result, 0 drafted rows in Notion, 53 applied, 16 rejected, 3 Not listed Anymore. CSV was stale, the 11 rows sitting at status drafted from the 18 July run had all been flipped in Notion but not in the CSV. CSV synced back to Notion for those 11 rows during reconciliation, 10 to applied and 1 to Not listed Anymore for the SAP Master Thesis SCM Agentic AI row which the recruiter took down. No new Notion rows created during reconciliation, only status flips into the CSV, per the 11 July rule that Notion is the human facing source of truth for status.

Backlog gate check. Authoritative count from Notion, 0 rows at drafted. That falls under 10, so the normal top 10 rule applies this run. Fallback would have used the CSV, which after reconciliation also shows 0 drafted.

Search sources reachable. Indeed connector, reachable, primary structured source, 15 searches returning fresh listings from around Germany. Tavily, reachable, used to cover StepStone, XING, and career pages, confirming Freudenberg Weinheim Masterarbeit listing sits on StepStone. Claude in Chrome extension, not attached in this automated run. LinkedIn Jobs, Glassdoor, and full career page walks not reachable without the extension. No Indeed only gap this run since Tavily filled the StepStone side.

Top count. 9 clean candidates cleared the filters after Step 3, so the top 10 is capped by supply, not by rule. The 9 are drafted in full.

Language track decisions per role, using the 20 July 2026 hard rule that the posting body language IS the deliverable language, no stated German level required. All bodies were read from the source URL before setting cfg lang.

- MTU Aero Engines, German body, German track.
- Dräger Lübeck, German body, German track.
- Witt-Gruppe, German body, German track.
- HELLA Lippstadt, German body, English strongly preferred but body written in German, German track.
- BwFuhrparkService, German body, German track.
- Siemens Mobility Erlangen, German body, German track.
- Craftview Software, German body, German track.
- Forschungszentrum Jülich, English body, English track.
- Rheinmetall Bremen, German body, German track.

Freshness dates used for ordering.

- MTU Aero Engines: 16 July 2026 posted
- Dräger Lübeck KI ML Prozessoptimierung: 16 July 2026
- Witt-Gruppe: 15 July 2026
- HELLA: 15 July 2026
- BwFuhrparkService: 8 July 2026
- Siemens Mobility Erlangen: 7 July 2026
- Craftview Software: 7 July 2026
- Forschungszentrum Jülich: 19 June 2026
- Rheinmetall Bremen: 9 June 2026

Notion, CSV both healthy this run. LinkedIn outreach block was executed under strict verification rules and no linkedin.com/in/ URL could be verified without the Chrome extension. Per the 12 July 2026 rule, unverified contacts are dropped, and every Notion row for this batch carries "no clear contact this run" in LinkedIn Contact. Witt-Gruppe carries Jennifer Bäuml, Rheinmetall carries Julia Behrens, both named in their Ausschreibung, both without a verified LinkedIn URL, so they stay as reference notes only. Gmail draft created against rahulrawat2r@gmail.com, no send.

No prompt injection content was observed in any listing this run.

## Top 9 drafts, per rule ordering, geographic tier Germany first, then freshness, then role type, then Best for overlap

### 1. MTU Aero Engines, Werkstudent Customer Support und Data Analytics Industriegasturbine, Ludwigsfelde

Apply: https://to.indeed.com/aav8n76f77kg
German level required: B2 (gute Deutsch und Englischkenntnisse).
Track: German. Draft path: drafts/MTU Aero Engines Werkstudent Data Analytics Industriegasturbine/
Fit rationale: Werkstudent Customer Support and Data Analytics work for the aeroderivate industrial gas turbines LM2500 and LM6000, mirrors the Movie Analytics BigQuery Medallion plus Looker Studio reporting, Fast Food Tableau dashboarding, and Climate Random Forest business insight projects, all in German.
LinkedIn outreach: no clear contact this run.

### 2. Dräger Lübeck, Praktikum Künstliche Intelligenz und maschinelles Lernen für interne Prozessoptimierung

Apply: https://to.indeed.com/aazg8fsgdb94
German level required: none stated.
Track: German. Draft path: drafts/Draeger Praktikum KI ML Prozessoptimierung/
Fit rationale: Corporate Technology and Innovation praktikum on AI and ML for internal process optimisation, mirrors the eRay recursive time series pipeline, CreditIQ ML validation with 100 percent branch coverage, and RAG orchestrator work, all in German.
LinkedIn outreach: no clear contact this run.

### 3. Witt-Gruppe, Praktikum Künstliche Intelligenz und Machine Learning 50 Prozent Remote, Weiden

Apply: https://to.indeed.com/aagyjwp94mzw
German level required: none stated.
Track: German. Draft path: drafts/Witt-Gruppe Praktikum KI ML/
Fit rationale: End to end KI model development in Google Cloud or Azure with XGBoost, scikit learn, and TensorFlow, mirrors CreditIQ, Movie Analytics BigQuery ML, and RAG orchestrator, all in German.
LinkedIn outreach: Jennifer Bäuml is named on the Ausschreibung as recruiting contact with email jennifer.baeuml@witt-gruppe.eu, no verified linkedin.com/in/ URL this run, kept as reference note on the Notion row.

### 4. FORVIA HELLA, Praktikum im Bereich Data und AI, Lippstadt

Apply: https://to.indeed.com/aaps8kxdgnc9
German level required: none stated, English C1 required.
Track: German. Draft path: drafts/HELLA Praktikum Data AI/
Fit rationale: Business Transformation Studio praktikum on datengetriebene Produkte with Machine Learning, Generative AI, and NLP, mirrors Movie Analytics BigQuery Medallion, RAG orchestrator, and Climate Random Forest, all in German.
LinkedIn outreach: no clear contact this run.

### 5. BwFuhrparkService, Werkstudent Controlling und Data Analytics, Siegburg

Apply: https://to.indeed.com/aaqbqq94lqys
German level required: C1 (sehr gute Deutsch Kenntnisse).
Track: German. Draft path: drafts/BwFuhrparkService Werkstudent Controlling Data Analytics/
Fit rationale: Controlling naher Reporting Werkstudent with PowerBI, Excel, PowerPivot, mirrors Fast Food Tableau dashboard, Movie Analytics BigQuery pipeline plus Looker Studio, and Climate Random Forest, all in German.
LinkedIn outreach: no clear contact this run.

### 6. Siemens Mobility, Werkstudent IT-Controlling und Data Analytics, Erlangen

Apply: https://to.indeed.com/aaq2tjr4qq9s
German level required: B2 (fließend Deutsch und Englisch).
Track: German. Draft path: drafts/Siemens Erlangen Werkstudent IT-Controlling Data Analytics/
Fit rationale: Werkstudent IT-Controlling on Ist Analyse, Forecast, Budget, and AI plus Data Analytics rollout, mirrors Movie Analytics BigQuery Medallion, Fast Food Tableau dashboarding, and RAG orchestrator, all in German.
LinkedIn outreach: no clear contact this run.

### 7. Craftview Software GmbH, Werkstudent People Analytics und AI Reporting, 100 Prozent Remote, Frankfurt am Main

Apply: https://to.indeed.com/aa4q9jv6jg8p
German level required: none stated, German and English von Vorteil.
Track: German. Draft path: drafts/Craftview Werkstudent People Analytics AI Reporting Remote/
Fit rationale: 100 percent remote HR Controlling greenfield with KI Automation for reporting and Power BI or Tableau or Looker, mirrors Movie Analytics BigQuery Medallion plus Looker, Fast Food Tableau, and RAG orchestrator, all in German.
LinkedIn outreach: no clear contact this run.

### 8. Forschungszentrum Jülich, Master Thesis Benchmarking and Transferability of Grid Foundation Models for Power Grid Analysis

Apply: https://to.indeed.com/aal9c2lytdfh
German level required: none stated, very good English.
Track: English. Draft path: drafts/Juelich Master Thesis Grid Foundation Models/
Fit rationale: Master Thesis on benchmarking GNNs and physics informed ML on grid data, mirrors the eRay recursive forecasting pipeline benchmarking six models with anti leakage rules, CreditIQ subgroup benchmarking, and the Flight Tracking geospatial signal pipeline.
LinkedIn outreach: no clear contact this run.

### 9. Rheinmetall Bremen, Praktikant und Masterarbeit Deep Learning zur Bildverbesserung

Apply: https://to.indeed.com/aalgb7p8c2kp
German level required: B2 (gute Deutsch und Englischkenntnisse).
Track: German. Draft path: drafts/Rheinmetall Praktikum Masterarbeit Deep Learning Bildverbesserung/
Fit rationale: Praktikum plus Masterarbeit on Deep Learning image improvement with PyTorch and CUDA, mirrors the eRay time series pipeline benchmarking, CreditIQ evaluation with 100 percent branch coverage, and the Flight Tracking Google Cloud pipeline, all in German.
LinkedIn outreach: Julia Behrens is named on the Ausschreibung as contact, no verified linkedin.com/in/ URL this run, kept as reference note on the Notion row.

## Watchlist, scored but not drafted this run

- Bechtle AG, Werkstudent AI Projektassistenz, Neckarsulm. Local to Mannheim, seen on StepStone, but the posting body was not directly readable in this Tavily pass, so left off the top cut this run and marked as follow up.
- Freudenberg Technology Innovation SE, Masterarbeit Data Science und Machine Learning im Spritzguss, Weinheim. Very local Master Thesis, seen on StepStone, but the direct listing URL and body could not be captured cleanly in this Tavily pass, follow up on the next run.
- Forschungszentrum Jülich has additional Werkstudent postings not directly seen this run.
- Herrmann Vermarktungsgesellschaft, Werkstudent Data Analyst, Neuss, 10 June, kept as watchlist due to age below the top cut.
- Hypoport BV and FIO SYSTEMS, Werkstudent Data and Reporting Analyst, Leipzig, 23 June, similar reason.
- Estateanfrage, Werkstudent AI Engineer, München, 19 June, kept as watchlist.

## Dropped this run, per Step 3 rules

- Volkswagen Wolfsburg, Praktikum or Abschlussarbeit Deep Learning autonomes Fahren, already in Notion as Not listed Anymore for the 15 July batch, dropped as dedup.
- Geiger Gruppe Werkstudent KI und Automatisierung Waltenhofen 20 July, already in the applied log as applied.
- Dico Drinks Werkstudent IT Datenvisualisierung Hückelhoven 15 July, already applied.
- RSG Group Werkstudent Data and Analytics Berlin 14 July, already applied.
- HanseWerk, Debeka, 1KOMMA5 Wärmepumpe, MVV Energie, Wieland Werkstudent Data Platform, Bosch Digital Health, Infineon Master Thesis AI Condition Monitoring, Fraunhofer SIT Werkstudent NLP, all already in applied log.
- Encavis Berufsbegleitendes Studium Data Science and AI, dropped as dual study by Step 3.
- 4flow AI Engineer Consulting Berlin, dropped as full time by Step 3.
- Dräger Abschlussarbeit Software Programmierung Computer Vision and Machine Learning Lübeck 16 July, dropped as dedup, already drafted and applied on 18 July.
- Yoona Ventures, KOSTAL, ahc GmbH, Valeo Wemding, Valeo Bietigheim-Bissingen, HMS Analytical Software, GEA Biedenkopf, EVOC Sports, Körber, RheinEnergie, IfTA GmbH, Formigas GmbH, HUMMEL energize, GRAMMER, dSPACE, STAR COOPERATION, Deloitte, all seen in results but not in the top 9 either due to age below the fresher listings that made the cut or lack of clear Master Thesis, Werkstudent, or mandatory Pflichtpraktikum signal.

## Notes

Every CV and cover letter shipped is in the same language as the posting body per the 20 July 2026 hard rule. 8 drafts on the German track, 1 on the English track. All drafts follow the 19 July Lebenslauf format, two column entry layout, Persönliche Daten table, tracked spaced caps section headings, navy plus rust palette, bold navy inline metrics on numeric quantities, signature tail with Mannheim date. Page counts sat inside the 2 to 3 A4 window on every PDF, no overflow surgery needed this run. Nothing was submitted anywhere, Rah applies manually.
