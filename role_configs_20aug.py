"""Role configurations for the 20 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in status
'drafted' at run start. Under 8 drafted falls in the normal top 3 to 5
tier under the 28 July 2026 yield reset. Reconciliation this run updated
11 CSV rows from 'drafted' to their true Notion Status (Retorio Not
listed Anymore, AssetMetrix applied, Phoenix Contact applied, BSH
rejected, viadee rejected, BMW Qualitaetsanalyse applied, KfW applied,
Allianz Insurance applied, Siemens Energy applied, Siemens AG operativer
Service rejected, Deloitte rejected). CSV is now aligned with Notion.

Platform mix for this run:
  - LinkedIn: 1 (PwC)
  - StepStone: 1 (Ed. Züblin)
  - Company Page: 1 (Amprion, primary source jobs.amprion.net; also
    listed on Xing)
  - Xing: 0 primary
  - Indeed: 0 (capped at 1 and not needed this run)

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. Amprion Werkstudent KI (Dortmund), posted ~2 days ago via Xing,
     Werkstudent, DE track
  2. Ed. Züblin AG Werkstudent BI & Data Analytics (Stuttgart), posted
     ~1 week ago on StepStone, Werkstudent, DE track
  3. PwC Deutschland Werkstudent AI Adoption & Enablement (Saarbrücken),
     posted ~1 week ago on LinkedIn, Werkstudent, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Amprion posting body in German -> DE track
  2. Ed. Züblin posting body in German -> DE track
  3. PwC posting body in German (w/m/d marker, German section headings
     Aufgaben/Anforderungen) -> DE track

Dedup check against applied-log.csv and Notion:
  - PwC Deutschland: never applied. New company.
  - Ed. Züblin AG: never applied. New company. STRABAG SE is the parent
    group; not previously applied to STRABAG either.
  - AMPRION: never applied. New company (energy TSO).

All three tag as 'Werkstudent'; all three are in-scope target roles
under the master-projects.md 'Werkstudent / part time' work type.

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


CONFIGS_20AUG = [
    # 1. Amprion GmbH, Dortmund
    # Werkstudent KI (m/w/d), Stellen-ID 7959, befristet
    # Company page primary source jobs.amprion.net, also on Xing (posted 2 days ago)
    # Team: Unternehmensweite IT-Loesungen, Wissens- und Dokumentenmanagement,
    # Digitalisierungsprojekte, digitaler Arbeitsplatz. DE track.
    # Apply: https://jobs.amprion.net/offer/werkstudent-ki-m-w-d/df7261d9-a116-4a2b-bc2e-70d2d113f93c
    {
        "folder": "Amprion Dortmund Werkstudent KI",
        "company": "Amprion GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | RAG und Wissensmanagement | Python + LangGraph + BigQuery",
        "role_strip": "Werkstudent KI",
        "cl_date": "20. August 2026",
        "cl_subject": "Werkstudent KI, Stellen-ID 7959, im Team Unternehmensweite IT-Loesungen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim, mit praktischer Erfahrung an der Schnittstelle von Large Language Models, RAG Systemen und regulierten Datenumgebungen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B und Qwen2.5 14B mit voller EN und DE Unterstuetzung gebaut und in einem Cloud Data Projekt eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run entwickelt, die vollstaendig unbeaufsichtigt laeuft. Sicher in Python, SQL, LangGraph, Streamlit, BigQuery und Airflow.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI unter der Stellen-ID 7959 im Team Unternehmensweite IT-Loesungen am Standort Dortmund. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich besonders die Verbindung aus Wissens und Dokumentenmanagement, digitalem Arbeitsplatz und der Rolle von Amprion in der Energiewende, weil ich in den letzten Monaten genau an der Schnittstelle von RAG, LLM Tooling und ehrlich validierbaren KI Pipelines gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Der LanguageAgent zentralisiert Sprache und Ausgabesteuerung, ein JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports, so dass ein Wissensmanagement Assistent belastbar iteriert werden kann. Genau dieses Muster laesst sich direkt auf Amprions Wissens und Dokumentenmanagement uebertragen, damit ein AI Assistent auf internen Dokumenten die Antworten liefert, die die Fachbereiche wirklich brauchen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung und Deduplizierung ueber Window Functions in ein relationales Modell gehaertet und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit CatBoost MultiQuantile und asymmetrischen 80 Prozent Vorhersageintervallen geliefert, mit einem 3 Pass Outlier System und einer rollenden z-score Kontrolle, die einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff freilegte.",
            "Ich arbeite sicher in Python, SQL, LangGraph, Streamlit, BigQuery und Airflow sowie in den ueblichen Cloud Plattformen AWS und GCP. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Team vollstaendig auf Deutsch moeglich bleibt. Als Werkstudent kann ich in Dortmund im Rahmen des Werkstudentenmodells einsteigen. Gerne bespreche ich meinen Beitrag zum Team Unternehmensweite IT-Loesungen in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Ed. Zueblin AG, Stuttgart
    # Werkstudent:in (m/w/d) Business Intelligence & Data Analytics
    # StepStone, posted about 1 week ago. Teilzeit / Werkstudent
    # Stack noted: Qlik Sense, Power BI, Datenqualitaet, Datenkonsistenz.
    # Studiengaenge: Bauingenieurwesen, BWL Analytics, Wirtschaftsinformatik,
    # Business Analytics, Data Science, Informatik. DE track.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-m-w-d-Business-Intelligence-Data-Analytics-Stuttgart-Ed-Zueblin-AG--14395739-inline.html
    {
        "folder": "Ed Zueblin Stuttgart Werkstudent BI Data Analytics",
        "company": "Ed. Zueblin AG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Analytics Pipelines und Dashboards | Python + SQL + BigQuery + Tableau",
        "role_strip": "Werkstudent Business Intelligence and Data Analytics",
        "cl_date": "20. August 2026",
        "cl_subject": "Werkstudent Business Intelligence and Data Analytics am Standort Stuttgart",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenpipelines, interaktiven Dashboards und automatisierten BI Loesungen. Ich habe eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit einem 5 seitigen Looker Studio Dashboard geliefert, eine interaktive Tableau Dashboard Loesung mit Set Actions und dynamischen Y Achsen gebaut und die Datenqualitaet in einer eRay GmbH Zeitreihen Pipeline mit einem 3 Pass Outlier System, sensor Ausschluessen und z-score Kontrolle sichergestellt. Sicher in Python, SQL, dbt, BigQuery, Tableau, Looker Studio und Power BI Grundlagen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Business Intelligence and Data Analytics am Standort Stuttgart bei der Ed. Zueblin AG. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die Kombination aus Dashboard Entwicklung in Qlik Sense und Power BI, der Validierung und Strukturierung realer Datenbestaende und der engen Zusammenarbeit mit einem Data Analyst und einer Digitalisierungsbeauftragten, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, die aus rohen Signalen tatsaechlich nutzbare Berichte machen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung, Deduplizierung ueber Window Functions und Genre Normalisierung in ein relationales Modell gehaertet und die Ergebnisse in einem 5 seitigen Looker Studio Dashboard aufbereitet, das konkrete Business Fragen zu Genre ROI, Wachstum internationaler Titel und Timing beantwortet. In meinem Fast Food Tableau Projekt habe ich einen dynamischen Warenkorb mit Set Actions gebaut, mit dem Endnutzer Datenpunkte auswaehlen und die 3 zentralen Makros Kalorien, Fett und Protein fuer eine simulierte Mahlzeit sofort aufsummieren koennen, und eine parametergesteuerte Y Achse ueber ein CASE Statement, die 2 Ziele Muskelaufbau und Gewichtsverlust ohne Dashboard Neuladen abdeckt. Genau dieses Verstaendnis fuer Endnutzer Interaktion laesst sich direkt auf Qlik Sense und Power BI Reports fuer Bauingenieurwesen uebertragen.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren geliefert und die September Evaluation mit einem 3 Pass Outlier System belastbar gemacht, indem der pH Bereich von 0 bis 14 auf 7,0 bis 9,0 verengt, Oct und Nov Caps von 15,0 bei Chlorophyll a und 50,0 bei Truebung gesetzt, ein rollender z-score bei z groesser 2,5 ueber 48 Stunden angewandt und 5 spaerliche Sensoren plus 3 zeitgleiche Proxies bewusst ausgeschlossen wurden, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff und 0,81 bei pH freilegte. Das Muster Datenqualitaet vor Modell und Datenkonsistenz vor Dashboard ist genau das, was die Ausschreibung unter Validierung, Bereinigung und Strukturierung von Datenbestaenden beschreibt.",
            "Ich arbeite sicher in Python, SQL, dbt, BigQuery, Tableau und Looker Studio, arbeite mich zuegig in Qlik Sense und Power BI ein und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics und AWS Academy Cloud Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Kommunikation im Team vollstaendig auf Deutsch moeglich bleibt. Als Werkstudent kann ich in Stuttgart einsteigen. Gerne bespreche ich meinen Beitrag zum BI und Data Analytics Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. PwC Deutschland
    # Werkstudent (m/w/d) AI Adoption & Enablement
    # LinkedIn, Saarland region. DE track (posting title carries w/m/d marker,
    # PwC AI Enablement portfolio content confirmed in German and English on
    # pwc.de/en/data-and-ai/ai-enablement.html). Focus areas: Change and
    # Adoption for AI, People Upskilling, AI Governance, Data and AI tools.
    # Apply: https://de.linkedin.com/jobs/view/werkstudent-ai-adoption-enablement-w-m-d-at-pwc-deutschland-4454990009
    {
        "folder": "PwC Deutschland Werkstudent AI Adoption Enablement",
        "company": "PwC Deutschland",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | GenAI Enablement und RAG Evaluation | Python + LangGraph + LLM as Judge",
        "role_strip": "Werkstudent AI Adoption and Enablement",
        "cl_date": "20. August 2026",
        "cl_subject": "Werkstudent AI Adoption and Enablement",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Large Language Models, ehrlicher AI Evaluation und regulierten Entscheidungssystemen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B und Qwen2.5 14B mit voller EN und DE Unterstuetzung gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt hat. Sicher in Python, SQL, LangGraph, Streamlit, scikit-learn und GenAI Tooling sowie in der Uebersetzung von Modellergebnissen in tatsaechlich angenommene Produkte.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Adoption and Enablement bei PwC Deutschland. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die Kombination aus Change and Adoption for AI, People Upskilling und AI Governance, weil ich in den letzten Monaten genau an der Frage gearbeitet habe, wie ein KI System nicht nur technisch funktioniert, sondern im Alltag auch tatsaechlich angenommen wird und ehrlich messbar bleibt.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber eine hybride BM25 plus Dense Retrieval Pipeline in Englisch und Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Genau dieses Muster laesst sich direkt auf die Frage uebertragen, wie eine Copilot oder Agentic Change Rollout Kampagne belastbar KPI getrieben statt anekdotisch geplant und gesteuert wird.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben, mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent gefallen bei einer stabilen Accuracy von 75 Prozent, und das Modell laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer und einer Unit Test Suite mit 100 Prozent Branch Coverage. Genau diese Verbindung aus Modell, Governance und Nutzererlebnis ist das, was AI Enablement in einer regulierten Umgebung braucht.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph und den ueblichen Cloud Plattformen AWS und GCP und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Kommunikation im Team vollstaendig auf Deutsch moeglich bleibt. Als Werkstudent kann ich in einem hybriden Modell einsteigen. Gerne bespreche ich meinen Beitrag zum AI Adoption and Enablement Team in einem persoenlichen Gespraech.",
        ],
    },
]
