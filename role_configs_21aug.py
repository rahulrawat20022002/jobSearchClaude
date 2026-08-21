"""Role configurations for the 21 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in
status 'drafted' at run start. Under 8 drafted falls in the normal top
3 to 5 tier under the 28 July 2026 yield reset.

Reconciliation this run updated 5 CSV rows from 'drafted' to their true
Notion Status (Amprion Masterarbeit applied, Ed. Zueblin applied, PwC
applied, Bosch Rexroth applied, Ardex Not listed Anymore) and created
one missing Notion row for the Amprion Werkstudent KI role that was in
the CSV but absent from Notion.

Top 3 cut per 28 July 2026 yield reset: with 0 drafted at run start,
the run targets fresh roles. Held to top 3 today because the fresh
non-Indeed lead pool for the day was thin.

Platform mix for this run per 28 July 2026 yield weighting (Indeed
capped at 1 per run):
  - Company Page: 2 (Bosch jobs.bosch.de, Sana careers.sana.de via
    SmartRecruiters)
  - Indeed: 1 (FLEX Capital Berlin, only fresh strong-fit Werkstudent
    Data Science and AI role I could confirm today on any platform)
  - LinkedIn / StepStone / Xing: 0 this run

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. Sana HR Solutions GmbH Werkstudent Data Engineer (Muenchen), posted
     17 Aug 2026 (4 days ago), Werkstudent, DE track
  2. Bosch Renningen Masterarbeit Agentisches KI-System fuer eine
     Halbleiterdatenbank (Renningen), posted 11 Aug 2026 (10 days ago),
     Masterarbeit, DE track
  3. FLEX Capital Management GmbH Werkstudent Data Science and AI
     (Berlin), posted 12 Aug 2026 (9 days ago), Werkstudent, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Sana posting body in German -> DE track
  2. Bosch posting body in German (contains English keywords like MCP,
     Agentic AI as technology names only) -> DE track
  3. FLEX Capital posting body in German (Deine Aufgaben, Wen wir
     suchen, Sehr gute Deutsch- und Englischkenntnisse) -> DE track

Dedup check against applied-log.csv and Notion:
  - Sana HR Solutions GmbH: never applied. New company.
  - Bosch Renningen: parent Bosch is in the log for two Master Thesis
    roles (Graph Based QA and RAG rejected, Ambient Sensing for Digital
    Health Biomarkers rejected). This Masterarbeit on Agentic KI for
    Halbleiterdatenbank is a different team (semiconductor DB group at
    Renningen) and different work stream, allowed under the standing
    'different roles at the same company' rule.
  - FLEX Capital Management GmbH: never applied. New company (Berlin
    based private equity fund).

All three tag as Werkstudent or Masterarbeit; all three are in-scope
target roles under the master-projects.md 'Werkstudent / part time' and
'Master Thesis' work types.

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
)


CONFIGS_21AUG = [
    # 1. Sana HR Solutions GmbH, Muenchen
    # Werkstudent Data Engineer (m/w/d), Taetigkeits-ID 7016
    # Company page careers.sana.de, also on Indeed. Posted 17 Aug 2026
    # 12:10, Teilzeit / Werkstudent, min 2 more semesters required.
    # Stack: dbt, Python, SQL, Power BI, Oracle Analytics, Linux/Bash,
    # CI/CD, connector development. Team: Sana HR Solutions digitising
    # workflow supported HR processes across the Sana Konzern.
    # Apply: https://to.indeed.com/aan49kxw2vy8
    {
        "folder": "Sana HR Solutions Muenchen Werkstudent Data Engineer",
        "company": "Sana HR Solutions GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Analytics Pipelines und dbt Modelle | Python + SQL + BigQuery + Power BI",
        "role_strip": "Werkstudent Data Engineer",
        "cl_date": "21. August 2026",
        "cl_subject": "Werkstudent Data Engineer, Taetigkeits-ID 7016, am Standort Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenpipelines, dbt Modellen und interaktiven Dashboards fuer produktionsnahe Umgebungen. Ich habe eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit einem 5 seitigen Looker Studio Dashboard geliefert und in einer Real Time Flight Tracking Pipeline Python Collectors, PySpark Cleaning und dbt Modelle auf Google Cloud kombiniert. Sicher in Python, SQL, dbt, BigQuery, Airflow, Power BI und Looker Studio sowie in Linux Shell und CI/CD Grundlagen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Engineer unter der Taetigkeits-ID 7016 am Standort Muenchen bei der Sana HR Solutions GmbH. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die Kombination aus dbt Datenmodellierung, Anbindung neuer Datenquellen und der Aufbereitung fuer Power BI und Oracle Analytics, weil ich in den letzten Monaten genau an dieser Kette Systeme gebaut habe, die aus Rohdaten Berichte machen, denen Stakeholder vertrauen koennen.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, die Daten mit dbt in analysebereite Tabellen modelliert und den naechstgelegenen Flughafen pro Flugzeug mit PySpark berechnet. Das Gesamtsystem laeuft alle 15 Minuten unbeaufsichtigt auf Apache Airflow mit GCS und Dataproc, und die Ergebnisse liegen in einem Tableau Workbook mit Python Statistik ueber TabPy. Genau dieses Muster, roh Signale zu sauberen dbt Modellen und dann zu einem BI Dashboard, laesst sich direkt auf die HR Datenlandschaft der Sana HR Solutions uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung, Deduplizierung ueber Window Functions und Genre Normalisierung in ein relationales Modell gehaertet und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit einem 3 Pass Outlier System belastbar gemacht, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff freilegte. Das Muster Datenqualitaet vor Modell und Datenkonsistenz vor Dashboard ist genau das, was ETL Konnektoren und Requirements Engineering fuer neue Schnittstellen bei Sana brauchen.",
            "Ich arbeite sicher in Python, SQL, dbt, BigQuery und Airflow, kenne mich mit Linux Shell und Bash aus, arbeite mich zuegig in Power BI und Oracle Analytics ein und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Kommunikation im Team vollstaendig auf Deutsch moeglich bleibt. Als Werkstudent kann ich in Muenchen im Rahmen des Werkstudentenmodells einsteigen und habe noch mindestens zwei Semester vor mir. Gerne bespreche ich meinen Beitrag zum Sana HR Solutions Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Bosch Renningen (Robert Bosch GmbH)
    # Masterarbeit: Agentisches KI-System fuer eine Halbleiterdatenbank
    # (w/m/div.), Ref REF293881R. Company page jobs.bosch.de. Posted
    # 11 Aug 2026. 6 month Masterarbeit, Vor Ort erforderlich. Stack:
    # Python, Machine Learning, Agentic AI, SQL, Git, MCP.
    # Team: Cross-Domain Computing Solutions / Bosch Center for AI at
    # the Renningen research campus.
    # Apply: https://jobs.bosch.de/job/Masterarbeit_-Agentisches-KI-System-fuer-eine-Halbleiterdatenbank-w_m_div.-Renningen?id=7c44c060-25f7-4616-88ba-264de32fd3d7
    {
        "folder": "Bosch Renningen Masterarbeit Agentisches KI Halbleiterdatenbank",
        "company": "Robert Bosch GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentic AI und LLM Evaluation | Python + LangGraph + SQL + MCP",
        "role_strip": "Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank",
        "cl_date": "21. August 2026",
        "cl_subject": "Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank, Referenz REF293881R, in Renningen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von agentischer KI, Large Language Models und ehrlicher Evaluation. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B als Generator und Qwen2.5 14B als Judge gebaut, mit einem LangGraph orchestrierten Agentengraph und einem EvalAgent, der 5 Retrieval und 4 Generation Metriken pro Sprache in JSON und Markdown Reports aggregiert. Sicher in Python, LangGraph, SQL, Streamlit und im Uebersetzen von natuerlicher Sprache in deterministische Datenbankoperationen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit Agentisches KI-System fuer eine Halbleiterdatenbank unter der Referenz REF293881R am Standort Renningen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die im Aufgabentext beschriebene Verbindung aus einem agentischen Reasoning System, einer produktionsnahen Halbleiterdatenbank und der Frage, wie ehrlich der Agent natuerliche Sprachabsichten in deterministische Datenbankoperationen uebersetzen kann, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, in denen Agenten nicht nur antworten, sondern auch messbar richtig antworten.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Der LanguageAgent zentralisiert Sprache und Ausgabesteuerung, der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Genau dieses Muster laesst sich direkt auf die geforderte Analyse der Effizienz und Genauigkeit autonomer Reasoning Schleifen im Vergleich zu klassischen Human in the Loop Data Science Workflows uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run gebaut, den Silver Layer mit Schema Enforcement, Typkonvertierung und Deduplizierung ueber Window Functions gehaertet und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit CatBoost MultiQuantile und asymmetrischen 80 Prozent Vorhersageintervallen und einem 3 Pass Outlier System geliefert. Die Kombination aus SQL, Schema Denken und einem ehrlichen Evaluationsblick auf Modellverhalten deckt sich mit dem, was der Agent auf der Halbleiterdatenbank braucht, wenn er Hypothesen anhand historischer Daten testet.",
            "Ich arbeite sicher in Python, LangGraph, SQL, Streamlit und Git und habe erste Beruehrung mit dem Model Context Protocol im Rahmen meiner Agentic AI Projekte. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Team vollstaendig auf Deutsch moeglich bleibt. Als Masterstudent bin ich an der SRH Heidelberg immatrikuliert, kann die Prasenz vor Ort in Renningen sicherstellen und die 6 monatige Laufzeit nach vorheriger Vereinbarung starten. Gerne bespreche ich meinen Beitrag zur Robert Bosch IT-Infrastruktur in einem persoenlichen Gespraech.",
        ],
    },

    # 3. FLEX Capital Management GmbH, Berlin
    # Werkstudent (w/m/d) Data Science and AI. Indeed, posted 12 Aug 2026,
    # Part-time. Werkstudent role in the Data and AI team of a Private
    # Equity fund focused on Software and Tech Mittelstand. Focus areas:
    # ML and LLM based solutions like RAG systems, chatbots, automation,
    # agentic AI use cases, portfolio company analytics.
    # Apply: https://to.indeed.com/aakn8m867dsn
    {
        "folder": "FLEX Capital Berlin Werkstudent Data Science AI",
        "company": "FLEX Capital Management GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | RAG Systeme und Agentic AI | Python + LangGraph + Streamlit",
        "role_strip": "Werkstudent Data Science and AI",
        "cl_date": "21. August 2026",
        "cl_subject": "Werkstudent Data Science and AI im Data and AI Team am Standort Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Large Language Models, RAG Systemen und AI Agenten. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B und Qwen2.5 14B mit voller EN und DE Unterstuetzung gebaut und in CreditIQ ein reguliertes Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt hat. Sicher in Python, SQL, scikit-learn, LangGraph und Streamlit sowie in der Uebertragung von Prototypen bis in produktive Anwendungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science and AI im Data and AI Team am Standort Berlin bei der FLEX Capital Management GmbH. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus datengetriebenen Loesungen fuer Portfoliounternehmen, ML und LLM basierten Anwendungen wie RAG Systemen und Chatbots und agentischen Automatisierungen im Kundensupport, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme von der Idee bis zur produktiven Umsetzung gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber eine hybride BM25 plus Dense Retrieval Pipeline in Englisch oder Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Genau dieses Muster laesst sich direkt auf agentische Use Cases bei Portfoliounternehmen anwenden, damit ein neuer AI Assistent belastbar KPI getrieben statt anekdotisch bewertet werden kann.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben, mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent gefallen bei einer stabilen Accuracy von 75 Prozent, und das Modell laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer und einer Unit Test Suite mit 100 Prozent Branch Coverage. Genau diese Verbindung aus klassischen ML Aufgaben, Modelltraining, Evaluierung und explorativen KPI Deep Dives ist das, was die Ausschreibung als Sparring mit erfahrenen Data Scientists und AI Engineers beschreibt.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph und Streamlit sowie in den ueblichen Cloud Plattformen AWS und GCP und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ich habe sehr gute Englisch und gute Deutschkenntnisse auf B1 laufend und hebe mein Deutsch aktiv weiter, damit die Kommunikation im Team vollstaendig auf Deutsch moeglich bleibt. Als Werkstudent kann ich in Berlin im Rahmen des Werkstudentenmodells einsteigen und uebernehme gern Verantwortung fuer eigene Teilprojekte von der Idee bis zum Deployment. Gerne bespreche ich meinen Beitrag zum Data and AI Team in einem persoenlichen Gespraech.",
        ],
    },
]
