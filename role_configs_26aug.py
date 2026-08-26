"""Role configurations for the 26 August 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. All 16 rows that showed status 'drafted' in the CSV
(NewTec, Anstalt fuer Kommunale Datenverarbeitung in Bayern, Boellhoff
Gruppe, logen.ai, Schaeffler Technologies, ADAC, Rosenberger
Hochfrequenztechnik, DELO Industrie Klebstoffe, nerou GmbH, KPMG
Deutschland, MEAG MUNICH ERGO AssetManagement, Senacor Technologies,
Fraunhofer IPT, Fraunhofer SIT Alterschaetzung, dmTECH, Fraunhofer IPA
Bewertungsmatrix ATMP) turned out to already carry a real Notion Status
(15 flipped to 'applied' by OpenClaw, 1 NewTec flipped to 'Not listed
Anymore') as of this run, so the CSV was reconciled to match Notion per
invariant 1. A further 6 rows had Notion Status drift against the CSV
(Bosch Graph Based QA and RAG csv rejected vs Notion 'shortlisted but no
interview', Mercedes-Benz Group KI Kommunikationsdaten Masterarbeit csv
applied vs Notion rejected, Johnson and Johnson Data Science Praktikum csv
applied vs Notion rejected, Ed. Zueblin Werkstudent BI csv applied vs
Notion rejected, Arthrex Working Student Business Analytics csv applied vs
Notion rejected, FLEX Capital Management Werkstudent Data Science and AI
csv applied vs Notion rejected) and were corrected in the CSV to match
Notion, never the reverse direction. 0 drafted falls under the 28 July
2026 gate's under 8 tier, so this run uses the normal top 3 to 5 cut.

Platform mix this run:
  - Company Page: 2 (Rohde and Schwarz career site, Volkswagen Group
    career site)
  - JobTeaser: 1 (Reply Deutschland SE / Blue Reply, sourced via JobTeaser
    per the 25 August 2026 JobTeaser search source rule)
  - Company Page: 1 (Kaufland career site)

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. Reply Deutschland SE (Blue Reply) Werkstudent fuer AI, Data
     Engineering und Tool-Entwicklung (Duesseldorf or Berlin), posted 16
     August 2026, Werkstudierende, DE track
  2. Rohde und Schwarz Werkstudent Data Analytics und Data Science
     (Memmingen), posted this week, Werkstudent, DE track
  3. Volkswagen Group Praktikum or Abschlussarbeit Customer Data
     Analytics und AI (Wolfsburg), Praktikum or Abschlussarbeit, DE track
  4. Kaufland Praktikant Data Science (Heilbronn), entry date 01 or 02
     February 2027, Praktikum, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all four postings are written in
German -> DE track for all four.

Language level transparency: Reply asks for "gute Deutsch- und
Englischkenntnisse", Rohde und Schwarz states no explicit German level in
the posting text pulled this run, Volkswagen states no explicit German
level in the posting text pulled this run, and Kaufland asks for fluent
written and spoken German and English ("fliessende Kommunikation in Wort
und Schrift"). Rah's German is B1, currently in progress, below the
explicit Reply and Kaufland bars. Shipped anyway per the standing rule
that language level does not filter listings, and the cover letters are
upfront about the current B1 level. Flagged in the digest transparency
block.

Apply method transparency: all four apply links land on the employer's own
careers domain (rohde-schwarz.com, jobs.volkswagen-group.com, the Blue
Reply application flow reached via jobteaser.com, career5.successfactors.eu
for Kaufland) rather than staying inside a platform-native Easy Apply flow
on linkedin.com, xing.com, stepstone.de, or indeed.com. Per the OpenClaw
scope rule in CLAUDE.md this makes all four company-portal, out of
OpenClaw's automated submission scope; Rah submits manually. Noted per
role below and in the digest.

Dedup check against applied-log.csv and Notion: Reply Deutschland SE,
Rohde und Schwarz, Volkswagen Group, and Kaufland are all new companies for
this specific role and location combination, never previously logged (the
existing Volkswagen entry in the log is a different role, Master Thesis
Deep Learning for Autonomous Driving in Wolfsburg, Not listed Anymore,
allowed under the different roles at the same company rule).

Dropped this run: CompanyMind GmbH (Oldenburg) Data Scientist Kuenstliche
Intelligenz Praktikum or Bachelor-/Masterarbeit required "sehr gute
Deutschkenntnisse, Muttersprache oder C1/C2-Niveau", a native or near
native German bar far above Rah's current B1 in progress level and a
sharper mismatch than the roles shipped this run, so it was dropped rather
than drafted. Noted in the digest Dropped section.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses/brackets in bullets, Languages EN+DE only (no Hindi),
German level locked to 'Deutsch: B1, laufend' on DE track, no page
numbers/headers/footers, 2 page hard cap, Ojas style header (name, tag,
contact lines, italic status), Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title, and
banned strings on the validation gate are met by the new header.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_26AUG = [
    # 1. Reply Deutschland SE (Blue Reply), Duesseldorf or Berlin
    # Werkstudent fuer AI, Data Engineering und Tool-Entwicklung (m/w/d)
    # JobTeaser, posted 16 August 2026, Werkstudierende, DE track
    # Tasks: konzeptionelle und implementierungstechnische Unterstuetzung
    # in Agentic AI Frameworks, Data Engineering und Data Lakehouse,
    # Technologien wie LLM, OpenAI, Anthropic Claude, Google Gemini, Spark,
    # Kafka, Snowflake, Databricks, AWS, Azure, Mitarbeit an innovativen
    # Tools und Frameworks.
    # Requirements: Studium Wirtschaftsinformatik, Wirtschaftsmathematik,
    # Physik, BWL oder aehnlich, Interesse an Cloud basierter
    # Softwareentwicklung mit Python oder Java, erste Beruehrungspunkte mit
    # GenAI, LLMs und Agentic, gute Deutsch und Englischkenntnisse.
    # Apply: https://www.jobteaser.com/de/job-offers/8c53099a-89d7-43b8-8ad3-1ce7d73f4c20-reply-deutschland-se-werkstudent-fur-ai-data-engineering-und-tool-entwicklung-m-w-d
    # Apply method: company-portal (Blue Reply application flow reached via
    # the JobTeaser listing, not a platform-native Easy Apply flow)
    {
        "folder": "Reply Duesseldorf Berlin Werkstudent AI Data Engineering Tool Entwicklung",
        "company": "Reply Deutschland SE",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentic AI und LLM Tooling | Python + LangGraph + Data Engineering",
        "role_strip": "Werkstudent fuer AI, Data Engineering und Tool Entwicklung",
        "cl_date": "26. August 2026",
        "cl_subject": "Werkstudent fuer AI, Data Engineering und Tool Entwicklung bei Blue Reply",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau agentischer LLM Systeme und in der Entwicklung interner Tools und Frameworks fuer Data Engineering. Ich habe ein Multi Agent RAG System mit LangGraph, lokalen LLMs und LLM as Judge Evaluation gebaut und in einem Cloud Data Projekt eine vollautomatisierte Pipeline von der Rohdatenaufnahme bis zum Gold Layer entwickelt. Sicher in Python, LangGraph, Cloud Plattformen und in der praktischen Arbeit mit OpenAI, Anthropic Claude und aehnlichen LLM Anbietern.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit fuer AI, Data Engineering und Tool Entwicklung bei Blue Reply am Standort Duesseldorf oder Berlin. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus Agentic AI Frameworks, Data Engineering und Data Lakehouse Arbeit sowie dem produktiven Einsatz von LLM Anbietern wie OpenAI, Anthropic Claude und Google Gemini, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen mehrsprachigen Policy Korpus end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft, wobei ein build_pipeline Factory Pattern den Import des Orchestrators von externen Credentials entkoppelt. Genau diese Faehigkeit, agentische Frameworks robust und testbar zu gestalten, deckt sich mit der in der Ausschreibung beschriebenen Mitarbeit an innovativen Tools und Frameworks im Agentic AI Bereich.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, die Daten mit dbt modelliert und das Gesamtsystem mit Apache Airflow auf GCS Speicher und Dataproc Compute vollstaendig automatisiert. Diese Erfahrung mit Data Engineering Pipelines, Orchestrierung und Cloud Infrastruktur deckt sich direkt mit dem in der Ausschreibung beschriebenen Data Engineering und Data Lakehouse Schwerpunkt der Rolle.",
            "Ich arbeite sicher in Python, LangGraph und den ueblichen Cloud Plattformen AWS und GCP und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann als Werkstudent in Duesseldorf oder Berlin einsteigen, mit der Moeglichkeit teilweise remote zu arbeiten. Gerne bespreche ich meinen Beitrag zum Blue Reply Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Rohde und Schwarz GmbH und Co. KG, Memmingen
    # Werkstudent Data Analytics und Data Science (m/w/d)
    # Company career page, posted this week, Werkstudent, DE track
    # Tasks: Aufbereitung und Strukturierung von Rohdaten fuer Dashboards,
    # ad hoc Reports und Visualisierungen, Datenmodellierung und
    # ETL/ELT Pipelines, Data Quality Checks und Monitoring, Mitarbeit an
    # Projekten zur Validierung statistischer Verfahren und ML Modelle.
    # Requirements: Studium (Wirtschafts-)Informatik, Software Engineering
    # oder vergleichbar, fortgeschrittenes Bachelor oder Masterstudium,
    # Verstaendnis fuer Datenbankstrukturen, Python und R, erste Erfahrung
    # mit Git und OOP oder MS Powertools.
    # Apply: https://www.rohde-schwarz.com/de/karriere/stellenangebote/werkstudent-data-analytics-data-science-m-w-d_251563-1618307.html
    # Apply method: company-portal (rohde-schwarz.com career site)
    {
        "folder": "Rohde Schwarz Memmingen Werkstudent Data Analytics Data Science",
        "company": "Rohde und Schwarz GmbH und Co. KG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | ETL Pipelines und Dashboards | Python + SQL + PySpark + dbt",
        "role_strip": "Werkstudent Data Analytics und Data Science",
        "cl_date": "26. August 2026",
        "cl_subject": "Werkstudent Data Analytics und Data Science am Standort Memmingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von ETL Pipelines, Dashboards und der Validierung von Machine Learning Modellen in produktionsnahen Umgebungen. Ich habe eine Real Time Flight Tracking Pipeline mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen gebaut und in einem Cloud Data Projekt eine 3 stufige Bronze Silver Gold Medaillon Architektur mit Data Quality Checks gehaertet. Sicher in Python, SQL, PySpark, dbt, Git und in der strukturierten Aufbereitung von Rohdaten fuer Dashboards und Reports.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Analytics und Data Science am Standort Memmingen bei Rohde und Schwarz. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus der Aufbereitung von Rohdaten fuer benutzerfreundliche Dashboards, der Weiterentwicklung von ETL und ELT Pipelines und der Mitarbeit an Projekten zur Validierung statistischer Verfahren und Machine Learning Modelle, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, die Daten mit dbt in analysebereite Tabellen modelliert und das Gesamtsystem mit Apache Airflow auf GCS Speicher und Dataproc Compute vollstaendig automatisiert. Genau dieses Muster, Rohdaten strukturieren, in ETL Pipelines ueberfuehren und auf ad hoc Reports und Dashboards ausrichten, deckt sich mit der in der Ausschreibung beschriebenen Aufbereitung und Strukturierung von Rohdaten als Grundlage fuer Analysen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung, Deduplizierung ueber Window Functions und Data Quality Checks gehaertet, was saubere referenzielle Integritaet ueber alle nachgelagerten Gold Tabellen lieferte, und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Diese Erfahrung mit Data Quality Checks, Monitoring und der Validierung von Machine Learning Modellen deckt sich direkt mit dem in der Ausschreibung beschriebenen Aufgabenfeld.",
            "Ich arbeite sicher in Python, SQL, PySpark, dbt, Git und Apache Airflow fuer die Orchestrierung und nutze ChatGPT und Claude aktiv im Alltag. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann als Werkstudent in Memmingen einsteigen. Gerne bespreche ich meinen Beitrag zum Data Analytics und Data Science Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Volkswagen Group, Wolfsburg
    # Praktikum / Abschlussarbeit Customer Data Analytics und AI (w/m/d)
    # Company career page, DE track
    # Keywords from posting: Artificial Intelligence, Statistik,
    # Elektromobilitaet, Elektromotor, BEV, Mobilitaetsforschung,
    # Innovationsmanagement, Technologiebewertung, Datenoekosysteme,
    # Zukunftstechnologien. Requires good Python programming and
    # experience with big data and scalable systems per secondary source.
    # Vergueted per Mindestlohn for Praktikum and Abschlussarbeit.
    # Apply: https://jobs.volkswagen-group.com/Volkswagen/job/Wolfsburg-Praktikum-Abschlussarbeit-Customer-Data-Analytics-&-AI-%28wmd%29-38436/1427423533
    # Apply method: company-portal (jobs.volkswagen-group.com career site)
    {
        "folder": "Volkswagen Wolfsburg Praktikum Abschlussarbeit Customer Data Analytics AI",
        "company": "Volkswagen Group",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Predictive Analytics und KI fuer Mobilitaet | Python + Statistik + Random Forest",
        "role_strip": "Praktikum oder Abschlussarbeit Customer Data Analytics und AI",
        "cl_date": "26. August 2026",
        "cl_subject": "Praktikum oder Abschlussarbeit Customer Data Analytics und AI am Standort Wolfsburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Predictive Analytics, statistischer Modellierung und dem Uebersetzen von Kundendaten in belastbare Entscheidungsgrundlagen. Ich habe Random Forest Modelle zur Analyse wirtschaftlicher Zusammenhaenge entwickelt und in einem Cloud Data Projekt einen BigQuery ML Klassifikator mit sauber getrennten Pre Release Signalen trainiert. Sicher in Python, SQL, scikit-learn, statistischer Modellierung und in der Kommunikation technischer Ergebnisse an nicht technische Stakeholder.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CLIMATE_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_GOOGLE_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Praktikum oder die Abschlussarbeit im Bereich Customer Data Analytics und AI am Standort Wolfsburg. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Verbindung aus Artificial Intelligence, Statistik und Mobilitaetsforschung rund um Elektromobilitaet und Elektromotoren, weil ich in den letzten Monaten genau an dieser Schnittstelle aus Datenanalyse und produktnaher Entscheidungsunterstuetzung gearbeitet habe.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich ein end to end Projekt von der Roh CSV bis zum management fertigen Report gefuehrt, Ausreisser, fehlende Werte und inkonsistente Skalen bereinigt und Random Forest Modelle entwickelt, um den Zusammenhang zwischen Ereignisdauer und finanzieller Wirkung ueber Feature Importance und Residualanalyse zu erklaeren. Genau diese Faehigkeit, aus rohen Datenoekosystemen eine belastbare, statistisch fundierte Technologiebewertung abzuleiten, deckt sich mit der in der Ausschreibung beschriebenen Innovationsmanagement und Zukunftstechnologien Aufgabe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit einem EvalAgent gebaut, der 5 Retrieval Metriken und 4 Generation Metriken aggregiert pro Sprache in JSON und Markdown Reports auswertet, sodass Systementscheidungen auf gemessenen Kennzahlen statt auf Bauchgefuehl beruhen. Diese Faehigkeit, komplexe KI Systeme mit belastbaren Metriken zu bewerten, uebertraegt sich direkt auf die in der Ausschreibung beschriebene Technologiebewertung neuer KI Ansaetze fuer Datenoekosysteme im Kundenumfeld.",
            "Ich arbeite sicher in Python, SQL, scikit-learn und statistischer Modellierung und nutze ChatGPT und Claude aktiv im Alltag. Ich halte die AWS Academy Cloud Foundations, Google Data Analytics und SAS Certified Specialist Visual Business Analytics Using SAS Viya Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann das Praktikum oder die Abschlussarbeit in Wolfsburg antreten. Gerne bespreche ich meinen Beitrag zum Customer Data Analytics und AI Team in einem persoenlichen Gespraech.",
        ],
    },

    # 4. Kaufland, Heilbronn
    # Praktikant Data Science (m/w/d)
    # Company career page (jobs.kaufland.com), entry date 01.02.2027,
    # Praktikum, Vollzeit, befristet, DE track
    # Tasks: Bearbeitung von Analytics Use Cases entlang der
    # Wertschoepfungskette, Auswertung von Unternehmensdaten wie Bondaten,
    # Entwicklung von Vorhersagemodellen, Anwendung generativer KI Modelle,
    # Visualisierung der Ergebnisse.
    # Requirements: Studium Statistik, (Wirtschafts-)Mathematik, Physik,
    # Wirtschafts- oder Sozialwissenschaften, Informatik, Psychologie oder
    # vergleichbar, Grundlagenkenntnisse in Statistik und Machine
    # Learning, Python oder R, erste Erfahrung mit Datenbanken und SQL,
    # fliessende Deutsch und Englischkenntnisse.
    # Apply: https://jobs.kaufland.com/Deutschland/job/Heilbronn-Praktikant-Data-Science-(mwd)-74072/1279873801
    # Apply method: company-portal (career5.successfactors.eu application
    # flow reached via the Kaufland career site)
    {
        "folder": "Kaufland Heilbronn Praktikant Data Science",
        "company": "Kaufland",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Vorhersagemodelle und Generative KI | Python + SQL + Machine Learning",
        "role_strip": "Praktikant Data Science",
        "cl_date": "26. August 2026",
        "cl_subject": "Praktikant Data Science am Standort Heilbronn",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau von Vorhersagemodellen, im Einsatz generativer KI Modelle und in der Visualisierung von Analyseergebnissen entlang einer Wertschoepfungskette. Ich habe bei eRay GmbH eine rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile Vorhersagemodellen fuer vier Umweltindikatoren geliefert und ein Multi Agent RAG System mit generativen LLMs gebaut. Sicher in Python, SQL, Machine Learning und in der strukturierten Auswertung grosser Unternehmensdatensaetze.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Praktikum Data Science am Standort Heilbronn bei Kaufland ab Februar oder Maerz 2027. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus der Auswertung vielfaeltiger Unternehmensdaten, der Entwicklung von Vorhersagemodellen und dem Einsatz generativer KI Modelle entlang der gesamten Wertschoepfungskette, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "Bei eRay GmbH habe ich waehrend einer 6 monatigen Kollaboration mit der SRH Heidelberg eine end to end rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren ueber einen 40 Feature Raum geliefert und mich nach einem Benchmark von 6 Modellkandidaten fuer CatBoost MultiQuantile mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff freilegte. Genau diese Faehigkeit, robuste Vorhersagemodelle auf realen, verrauschten Datensaetzen zu entwickeln und ihre Guete ehrlich zu berichten, deckt sich mit der in der Ausschreibung beschriebenen Entwicklung von Vorhersagemodellen aus Unternehmensdaten wie Bondaten.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit generativen LLMs Mistral 7B und Qwen2.5 14B gebaut, das Fragen ueber einen Policy Korpus end to end beantwortet, und einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet. Diese praktische Erfahrung im produktiven Einsatz generativer KI Modelle und in der sauberen Visualisierung ihrer Ergebnisse in JSON und Markdown Reports deckt sich direkt mit dem in der Ausschreibung beschriebenen Einsatz generativer KI Modelle und der Visualisierung der Ergebnisse.",
            "Ich arbeite sicher in Python, SQL, scikit-learn und Machine Learning und nutze ChatGPT und Claude aktiv im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann das Praktikum ab Februar oder Maerz 2027 in Heilbronn antreten. Gerne bespreche ich meinen Beitrag zum Analytics Team in einem persoenlichen Gespraech.",
        ],
    },
]
