"""Role configurations for the 13 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 8 rows in status
'drafted' at run start (the three from 11 Aug run: 1&1 Versatel, SCHOTT,
HDI AG, plus the five from 12 Aug run: Commerzbank, BMW Muenchen KI-
Agenten, SAP Walldorf Engagement Lead, ARRK Engineering, Mercedes-Benz
Robot Manipulation). CSV in agreement, no drift. 8 drafted rows falls in
the 8 to 10 tier under the 28 July 2026 yield based reset rule, which
caps this run at the top 3 newly scored roles.

Platform mix per 28 July 2026 target weighting for a top 3 cut, aim for
mix across LinkedIn, career pages, StepStone, Xing, Indeed, with LinkedIn
and career pages preferred:
  - Career pages: 2 (BMW, Siemens)
  - Xing: 1 (CHECK24)
  - LinkedIn: 0 this run (Siemens role also on LinkedIn, counted as
    career page since the primary source is jobs.siemens.com)
  - StepStone: 0 this run
  - Indeed: 0 this run
Indeed capped at 1 and deliberately not used this run per yield rebalance.

Freshness order per 12 July 2026 priority rule (freshness first, then role
type, then Best for overlap), within the single Germany tier:
  1. Siemens AG Munich Working Student AI, Digital Products & Process
     Automation (Finance & M&A), posted 13 Aug 2026 (today), Werkstudent,
     EN track
  2. BMW Group Muenchen Werkstudent Data-Analytics Qualitaetsmanagement
     fuer Digitale Dienste, posted ~19 hours ago, Werkstudent, DE track
  3. CHECK24 Vergleichsportal Finanzen GmbH Muenchen Werkstudent AI-
     Produkte Kreditvergleich, posted 3 days ago, Werkstudent, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Siemens posting body written in English, only English required ->
     EN track
  2. BMW posting body written in German, "sehr gute Deutschkenntnisse
     sowie sicheres Englisch" -> DE track. Rah's B1 level is below the
     stated bar, noted in digest transparency block, still shipped per
     the standing rule that language level does not filter listings.
  3. CHECK24 posting body written in German, C1 German and English
     required -> DE track. Rah's B1 level is below the stated C1 bar,
     noted in digest transparency block, still shipped for the same
     reason. Both applications will be up front about the language
     level in the cover letter.

Dedup check: all three company plus role combinations verified absent
from applied-log.csv and Notion.
  - Siemens is in the log for other roles (Siemens Mobility IT-
    Controlling, Siemens Mandatory Internship DS DL Energy Systems,
    Siemens Healthineers X-Ray) but not this AI Digital Products & M&A
    role, allowed under the 'different roles at the same company' rule.
  - BMW Group is in the log for other Werkstudent and Master Thesis
    roles but not this Data-Analytics Qualitaetsmanagement role.
  - CHECK24 is in the log for other roles (CHECK24 Vergleichsportal
    Data Science Computer Vision IdentityCheck rejected, CHECK24
    Strategy Hub Data Engineering CFO Office rejected) but not this
    AI-Produkte Kreditvergleich role. New role, new team (KAI Kredite
    AI team), allowed under the 'different roles' rule.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA,
    CERT_NVIDIA_DE,
    CERT_AWS,
    CERT_AWS_DE,
    CERT_SAS,
    CERT_SAS_DE,
    CERT_GOOGLE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_RAG_DE,
    P_CREDITIQ_EN,
    P_CREDITIQ_DE,
    P_FLIGHT_EN,
    P_FLIGHT_DE,
    P_MOVIE_EN,
    P_MOVIE_DE,
    P_TABLEAU_EN,
    P_TABLEAU_DE,
    P_CLIMATE_EN,
    P_CLIMATE_DE,
)


CONFIGS_13AUG = [
    # 1. Siemens AG Munich
    # Working Student (f/m/d) AI, Digital Products & Process Automation (Finance & M&A)
    # jobs.siemens.com career page, posted 13 Aug 2026, Werkstudent, EN track
    # Location: Munich, hybrid, 15 to 20 hours per week, fixed term
    # Apply: https://jobs.siemens.com/en_US/externaljobs/JobDetail/517305
    {
        "folder": "Siemens Muenchen Working Student AI Digital Products Process Automation Finance MA",
        "company": "Siemens AG",
        "lang": "en",
        "role_strip": "Working Student, AI, Digital Products and Process Automation for Finance and MA",
        "cl_date": "13 August 2026",
        "cl_subject": "Working Student, AI, Digital Products and Process Automation for Finance and MA in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building AI powered solutions, dashboards, and internal automation over Python, SQL, and LLM tooling. I built a multi agent RAG system with an LLM as Judge evaluation running locally on Ollama with Mistral 7B and Qwen2.5 14B, and delivered a recursive time series pipeline for four water quality indicators at eRay GmbH using CatBoost MultiQuantile with 80 percent prediction intervals. Comfortable across Python, SQL, LangGraph, cloud platforms and web app work in React from earlier full time front end experience.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in AI, Digital Products and Process Automation for Finance and MA at Siemens in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of building AI powered solutions and digital assistants, designing web apps and dashboards, and automating manual finance workflows maps very closely to the projects I have shipped in the last several months.",
            "In my Multi Agent RAG project I built a full LangGraph orchestrated agent system that answers policy questions in English or German end to end. I implemented a JudgeAgent that scores answers on 5 dimensions using JSON mode at temperature 0, and eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B, plus an EvalAgent computing 5 retrieval metrics and 4 generation metrics aggregated per language into JSON and Markdown reports. The same evaluation harness pattern would let a Finance and MA team keep an honest read on whether a new digital assistant is actually improving workflow accuracy and turnaround, rather than shipping on vibes.",
            "In my Movie Analytics and ML Pipeline project I built an end to end batch pipeline that pulls data from a public API into a GCS data lake and processes it through a 3 tier Bronze Silver Gold medallion architecture in BigQuery on Cloud Run, running on a fully automated Cloud Scheduler trigger with 0 manual interventions, then closed with a 5 page Looker Studio dashboard answering questions on genre ROI, foreign language growth and release season timing. At eRay GmbH I delivered a recursive time series pipeline for four water quality indicators and chose CatBoost Multi Quantile regression with asymmetric 80 percent prediction intervals as the shipped model. I also carry a two year full time front end background in React inside a module federation setup with Playwright end to end tests, which lets me contribute to internal portals and dashboards without a learning curve.",
            "I work comfortably in Python, SQL, scikit-learn, LangGraph, and React, plus AWS and GCP for cloud tooling. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. As a working student I can join in Munich for 15 to 20 hours a week in a hybrid setup immediately. I would welcome the chance to discuss how I could contribute to your AI, Digital Products and Process Automation team.",
        ],
    },

    # 2. BMW Group Muenchen
    # Werkstudent Data-Analytics Qualitaetsmanagement (w/m/x) fuer Digitale Dienste, Fahrzeugvernetzung und E-Mobilitaet
    # bmwgroup.jobs career page, posted ~19 hours ago, Werkstudent, DE track
    # Location: Muenchen, hybrid, 12 months, Teilzeit
    # Apply: https://www.bmwgroup.jobs/de/de/jobfinder/job-description.192520.html
    {
        "folder": "BMW Muenchen Werkstudent Data Analytics Qualitaetsmanagement Digitale Dienste",
        "company": "BMW Group",
        "lang": "de",
        "role_strip": "Werkstudent Data-Analytics Qualitaetsmanagement fuer Digitale Dienste",
        "cl_date": "13. August 2026",
        "cl_subject": "Werkstudent Data-Analytics Qualitaetsmanagement fuer Digitale Dienste, Fahrzeugvernetzung und E-Mobilitaet",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenpipelines, Dashboards und Machine Learning Modellen fuer produktionsnahe Umgebungen. Ich habe bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen fuer Umweltindikatoren geliefert und in einem Cloud Data Projekt eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run gebaut, die vollstaendig automatisiert laeuft. Sicher in Python, SQL, PySpark, dbt, BigQuery, Airflow, Tableau und Looker Studio.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data-Analytics im Qualitaetsmanagement fuer Digitale Dienste, Fahrzeugvernetzung und E-Mobilitaet am Standort Muenchen ab dem 1. Oktober 2026. Die Ausschreibung, Unterstuetzung bei Entwicklung und Betreuung von Data-Pipelines, Analyse und Visualisierung ueber Dashboards und die Entwicklung neuer datenbasierter Methoden in einem Big Data Analysetool zur Unterstuetzung der Qualitaetsarbeit, deckt sich sehr gut mit dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen-, Flugzeug- und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, die Daten mit dbt in analysebereite Tabellen modelliert und den naechstgelegenen Flughafen pro Flugzeug mit PySpark berechnet. Das Gesamtsystem laeuft alle 15 Minuten unbeaufsichtigt auf Apache Airflow mit GCS und Dataproc, und die Ergebnisse liegen in einem Tableau Workbook mit Python Statistik ueber TabPy, das die Erkenntnis freilegte, dass der Flugverkehr bei starkem Regen um das 4,4 fache abnimmt. Genau dieses Muster, roh Signale zu sauberen Metriken und dann zu einem Dashboard fuer Stakeholder, laesst sich direkt auf Qualitaetsindikatoren fuer digitale Dienste, Fahrzeugvernetzung und E-Mobilitaet uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung, Deduplizierung ueber Window Functions und Genre Normalisierung in ein relationales Modell gehaertet und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Das Reporting deckt in einem 5 seitigen Looker Studio Dashboard konkrete Business Fragen zu Genre ROI und Timing ab. Bei eRay GmbH habe ich zusaetzlich die September Evaluation mit einem 3 Pass Outlier System, dem Ausschluss von 5 spaerlichen Sensoren und einer rollenden z-score Kontrolle belastbar gemacht, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff und 0,81 bei pH freilegte.",
            "Ich arbeite sicher in Python, SQL, PySpark, dbt und BigQuery sowie in Apache Airflow fuer die Orchestrierung, Tableau und Looker Studio fuer die Visualisierung. Ich habe die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung Richtung B2, Englisch spreche ich fliessend, und ich arbeite aktiv daran, mein Deutsch weiter zu heben, damit ich die Kommunikation im Team vollstaendig auf Deutsch fuehren kann. Ich kann ab dem 1. Oktober 2026 in Muenchen mit 12 Monaten Laufzeit in Teilzeit einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Data-Analytics Team im Qualitaetsmanagement in einem persoenlichen Gespraech.",
        ],
    },

    # 3. CHECK24 Vergleichsportal Finanzen GmbH Muenchen
    # Werkstudent (m/w/d) AI-Produkte - Kreditvergleich, im KAI (Kredite AI) Team
    # Xing, posted 3 days ago, Werkstudent, DE track
    # Location: Muenchen, on site, Teilzeit
    # Apply: https://www.xing.com/jobs/muenchen-werkstudent-ai-produkte-kreditvergleich-157129841
    {
        "folder": "CHECK24 Muenchen Werkstudent AI-Produkte Kreditvergleich",
        "company": "CHECK24 Vergleichsportal Finanzen GmbH",
        "lang": "de",
        "role_strip": "Werkstudent AI-Produkte, Kreditvergleich",
        "cl_date": "13. August 2026",
        "cl_subject": "Werkstudent AI-Produkte, Kreditvergleich im KAI Team",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Machine Learning, Large Language Models und regulierten Kreditumgebungen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt hat. Sicher in Python, SQL, scikit-learn, LangGraph, LLM und GenAI Tooling sowie in der Uebersetzung von Modellergebnissen in Produktentscheidungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI-Produkte im Kreditvergleich im CHECK24 KAI Team am Standort Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die Kombination aus etabliertem Machine Learning, LLMs und generativer KI besonders, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, die aus Modellergebnissen kundenwirksame Produkte machen.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber eine hybride BM25 plus Dense Retrieval Pipeline in Englisch oder Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set, so dass A/B Vergleiche zwischen Modellvarianten belastbar werden, statt auf Bauchgefuehl zu laufen. Das gleiche Muster laesst sich direkt auf A/B Tests von Conversational AI Features im Kreditvergleich anwenden.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben, mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent gefallen bei einer stabilen Accuracy von 75 Prozent, und das Modell laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph und den ueblichen Cloud Plattformen AWS und GCP und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung Richtung B2. Ich moechte an dieser Stelle offen sein, dass ich die geforderte C1 Marke noch nicht erreicht habe, jedoch aktiv daran arbeite, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen vor Ort einsteigen. Gerne bespreche ich meinen Beitrag zum KAI Team in einem persoenlichen Gespraech.",
        ],
    },
]
