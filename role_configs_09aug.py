"""Role configurations for the 9 August 2026 job search run.

Backlog gate: Notion showed 5 drafted rows at run start on 9 August 2026 (all
from the 4 August and 8 August runs). 5 drafted rows is under the 8 drafted
soft cap of the 28 July 2026 yield-based reset, so the normal top 3 to 5 cut
applies. This run ships 4 roles, capped by the pool of clean fresh candidates
in reachable sources (StepStone was the only aggregator that returned deeply
detailed body content this run; LinkedIn, Xing, Indeed and Glassdoor returned
mostly aggregator category pages under WebSearch).

Platform mix this run: StepStone 4, LinkedIn 0, Xing 0, Indeed 0, career page 0.
This is heavier on StepStone than the 28 July 2026 weighting (LinkedIn 2,
career pages 1 to 2, StepStone 1, Xing 1, Indeed 0 to 1). LinkedIn 2 and
career page 1 to 2 shortfalls are documented in the digest transparency block
rather than silently absorbed.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. Mercedes-Benz AG Berlin Vans Werkstudent Data Engineering Datenanalyse KI DE (body German on StepStone, confirmed via web_fetch)
  2. Waldemar Link Norderstedt Werkstudent Scientific Affairs KI-Innovation DE (body German on StepStone)
  3. tk accelis Materials Essen Werkstudent Data Scientist Controlling Power BI DE (body German on StepStone)
  4. WISAG Munich Werkstudent Data Scientist DE (body German on StepStone)

Freshness ordering per 12 July 2026 priority rule
(freshness first, then role type Master Thesis > Werkstudent > Praktikum,
then Best for overlap, all within the single Germany tier):
  1. Mercedes-Benz Berlin Vans        22 hours old, Werkstudent, DE (freshest)
  2. Waldemar Link Norderstedt         2 days old,  Werkstudent, DE
  3. tk accelis Essen                  3 days old,  Werkstudent, DE
  4. WISAG Munich                      3 days old,  Werkstudent, DE

Company concentration note: two other fresh Mercedes-Benz roles were passed
over (Boeblingen Masterarbeit Dexterous Robot Manipulation, Sindelfingen
Masterarbeit Agentic AI CarIT Security) to keep company concentration inside
one Mercedes-Benz role per run. Both remain on the watchlist in the digest.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_MOVIE_DE,
    P_FLIGHT_DE,
    P_CREDITIQ_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
    P_RAG_DE,
)


CONFIGS_09AUG = [
    # 1. Mercedes-Benz AG Berlin Vans
    # Werkstudent*in Data Engineering, Datenanalyse und KI im Bereich Steuerung und Geschaeftsentwicklung Mercedes-Benz Vans
    # StepStone, 22 hours ago, Werkstudent, DE track
    # Stack: Databricks, SQL, Python, PySpark, Delta Lake, Power BI, DAX, Git, AI/BI Genie
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudentin-Data-Engineering-Datenanalyse-und-Kuenstliche-Intelligenz-im-Bereich-Steuerung-und-Geschaeftsentwicklung-Mercedes-Benz-Vans-Berlin-Mercedes-Benz-AG--14320385-inline.html
    {
        "folder": "Mercedes-Benz AG Berlin Vans Werkstudent Data Engineering Datenanalyse KI",
        "company": "Mercedes-Benz AG",
        "lang": "de",
        "role_strip": "Werkstudent Data Engineering, Datenanalyse und KI Mercedes-Benz Vans",
        "cl_date": "9. August 2026",
        "cl_subject": "Werkstudent*in Data Engineering, Datenanalyse und Kuenstliche Intelligenz Mercedes-Benz Vans in Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Data Engineering, Datenanalyse und KI Anwendungen. Ich habe eine cloud native Batch Pipeline auf GCP mit BigQuery ML und Looker Studio gebaut und bei eRay GmbH eine end to end Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen geliefert. Sicher in Python, SQL, PySpark und BI Werkzeugen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Engineering, Datenanalyse und Kuenstliche Intelligenz im Bereich Steuerung und Geschaeftsentwicklung Mercedes-Benz Vans am Standort Berlin, Stellennummer MER0004691. Die Ausschreibung, die Weiterentwicklung der MARS Daten und Analytics Plattform mit Databricks, SQL, Python, PySpark, Delta Lake und Power BI, Anbindung neuer Datenquellen, Aufbau von Datenmodellen sowie Weiterentwicklung bestehender KI Anwendungen bis hin zu Databricks AI/BI Genie Spaces, deckt sich sehr genau mit dem, was ich in den letzten Monaten gebaut und ausgeliefert habe.",
            "In meinem Movie Analytics Projekt auf Google Cloud habe ich eine vollstaendig automatisierte Batch Pipeline mit Bronze Silber Gold Medallion Architektur in BigQuery auf Cloud Run gebaut, einen leckagefrei evaluierten BigQuery ML Klassifikator trainiert und die Ergebnisse ueber ein fuenfseitiges Looker Studio Dashboard mit Gold Aggregaten ausgeliefert. In der Echtzeit Flugverfolgungs Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, das Ganze mit Apache Airflow auf GCS und Dataproc alle 15 Minuten unbeaufsichtigt orchestriert.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen, mich fuer CatBoost Multi Quantil Regression entschieden und asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung ausgeliefert. Die Pipeline wurde mit einem Orchestrator mit Gate Checks und oekologischen Grenzen umschlossen, sodass eine fehlgeschlagene Imputation den Lauf stoppt statt Wochen nachgelagerter Vorhersagen zu beschaedigen. In CreditIQ habe ich den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt.",
            "Ich arbeite sicher in Python, SQL, PySpark, Git und mit modernen KI Diensten und habe die AWS Academy Cloud Foundations, die NVIDIA Building LLM Applications und Google Data Analytics Zertifikate abgelegt. Ich wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ab September 2026 kann ich als Werkstudent 20 Stunden pro Woche in Berlin oder remote bei Mercedes-Benz Vans einsteigen. Gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Waldemar Link GmbH & Co. KG Norderstedt bei Hamburg
    # Werkstudent Scientific Affairs & KI-Innovation (m/w/d)
    # StepStone, 2 days ago, Werkstudent, DE track
    # Stack: KI/AI Anwendungen (Copilot, Claude), Datenanalyse, digitale Prozesse, Recherche, Dashboards
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Scientific-Affairs-KI-Innovation-m-w-d-Norderstedt-Waldemar-Link-GmbH-Co-KG--14315325-inline.html
    {
        "folder": "Waldemar Link Norderstedt Werkstudent Scientific Affairs KI-Innovation",
        "company": "Waldemar Link GmbH und Co. KG",
        "lang": "de",
        "role_strip": "Werkstudent Scientific Affairs und KI-Innovation",
        "cl_date": "9. August 2026",
        "cl_subject": "Werkstudent Scientific Affairs und KI-Innovation in Norderstedt",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Multi Agent KI Systemen und Retrieval Augmented Generation. Ich habe ein Multi Agent RAG Policy Analysesystem mit LLM as Judge Evaluation und lokalem Betrieb ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut und bei eRay GmbH eine end to end Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen geliefert. Sicher in Python, LangGraph, spaCy und dem Aufbau mehrsprachiger Pipelines und AI Evaluation Harnesses.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Scientific Affairs und KI-Innovation am Standort Norderstedt. Die Ausschreibung, die Einfuehrung und Weiterentwicklung von KI Anwendungen wie Microsoft Copilot und Claude, Unterstuetzung bei der Analyse wissenschaftlicher und regulatorischer Daten, Aufbau von Wissensdatenbanken, digitalen Assistenten und intelligenten Suchloesungen sowie Recherche und Bewertung wissenschaftlicher Publikationen und Normen, deckt sich sehr genau mit den KI und Datenanalyse Themen, die ich in den letzten Monaten gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein hybrides BM25 plus Dense Retrieval System ueber einen 14 Dokumente Policy Korpus zu einer mehrsprachigen EN und DE Pipeline erweitert, indem Embeddings und Retrieval auf paraphrase multilingual MiniLM L12 v2 in einem gemeinsamen Vektorraum migriert wurden, sodass eine deutsche Anfrage englische Quellen abruft und auf Deutsch beantwortet wird. Ich habe einen LLM as Judge JudgeAgent implementiert, der Antworten auf 5 Dimensionen mit 1 bis 5 bewertet, dabei laeuft der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B, damit Self Preference Bias eliminiert wird, plus einen EvalAgent, der 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports liefert. Dieselbe Denkweise, KI Systeme mit belastbarer Wissensbasis, klaren Guardrails und auditierbarer Evaluation aufzubauen, will ich in Ihr Scientific Affairs Team einbringen.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet direkt verglichen und mich fuer CatBoost Multi Quantil Regression entschieden, die asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung lieferte. Strenge Anti Leakage Regeln und ein Orchestrator mit Gate Checks halten die Pipeline auditierbar, was gut zu Ihrer regulierten Medizintechnik Umgebung passt. In CreditIQ habe ich unter EU AI Act und AGG den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, bei einer Unit Test Branch Coverage von 100 Prozent.",
            "Ich arbeite sicher in Python, LangChain und mit modernen KI Diensten wie Copilot, ChatGPT und Claude, dokumentiere Methoden und Ergebnisse fuer den internen Wissenstransfer und kann eigene Themen strukturiert vorantreiben. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist aktuell B1 in Bearbeitung Richtung B2, Englisch spreche ich fliessend. Gerne bespreche ich meinen Beitrag zu Ihrem Scientific Affairs Team in einem persoenlichen Gespraech in Norderstedt.",
        ],
    },

    # 3. tk accelis Materials GmbH Essen
    # Werkstudent:in Data Scientist im Controlling / Power BI (m/w/d)
    # StepStone, 3 days ago, Werkstudent, DE track
    # Stack: SAP Data Warehouse, Power BI, Excel, MS Office, MS Access
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-Data-Scientist-im-Controlling-Power-BI-m-w-d-Essen-tk-accelis-Materials-GmbH--14374182-inline.html
    {
        "folder": "tk accelis Essen Werkstudent Data Scientist Controlling Power BI",
        "company": "tk accelis Materials GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Data Scientist im Controlling und Power BI",
        "cl_date": "9. August 2026",
        "cl_subject": "Werkstudent:in Data Scientist im Controlling und Power BI in Essen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Datenanalyse, Reporting und Dashboardbau. Ich habe eine cloud native Batch Pipeline auf GCP mit BigQuery ML und einem 5 seitigen Looker Studio Dashboard gebaut und ein 2 stufiges Tableau Dashboard mit dynamischem Warenkorb und parameter gesteuerter Analytik veroeffentlicht. Sicher in Python, SQL, Excel und Power BI.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Scientist im Controlling und Power BI am Standort Essen. Die Ausschreibung, technische Unterstuetzung bei Monats und Jahresabschluessen, Umwandlung von Daten in aussagekraeftige Analysen, Aufbereitung von Daten aus verschiedenen Quellen im SAP Data Warehouse Umfeld sowie die Weiterentwicklung von Dashboards und datenbasierten Informationssystemen in Power BI, deckt sich sehr genau mit den Reporting und Analytics Themen, die ich in den letzten Monaten praktisch umgesetzt habe.",
            "In meinem Movie Analytics Projekt auf Google Cloud habe ich eine vollstaendig automatisierte Batch Pipeline mit Bronze Silber Gold Medallion Architektur in BigQuery aufgebaut, dabei Schema Enforcement, sichere Type Casts, Deduplikation per Window Functions und Genre Normalisierung durchgesetzt und ueber ein fuenfseitiges Looker Studio Dashboard Fragen zu Genre ROI, Wachstum fremdsprachiger Filme und Release Saison Timing beantwortet. In meinem Fast Food Tableau Dashboard habe ich mit Set Actions einen dynamischen Warenkorb gebaut, mit parameter gesteuerter Analytik einen dynamischen Y Achsen Wechsel per CASE Statement umgesetzt und komplexe IF THEN Calculated Fields fuer Trap Item Flagging geschrieben.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet direkt verglichen und mich fuer CatBoost Multi Quantil Regression entschieden, die asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung lieferte. Strenge Anti Leakage Regeln und ein Orchestrator mit Gate Checks halten die Pipeline auditierbar, was gut zu Reporting Zyklen im Controlling passt.",
            "Ich arbeite sicher in Python, SQL, Excel und Power BI und habe die SAS Visual Business Analytics, Google Data Analytics Foundations und AWS Academy Cloud Foundations Zertifikate abgelegt. Ich wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche in Essen oder remote einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team am ruhr tech kampus in einem persoenlichen Gespraech.",
        ],
    },

    # 4. WISAG Airport Service Holding AG Muenchen und Freising
    # Werkstudent (m/w/d) Data Scientist
    # StepStone, 3 days ago, Werkstudent, DE track
    # Stack: Qlik, Excel, BI Reports, Datenanalyse fuer Aviation
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-m-w-d-Data-Scientist-Muenchen-Freising-WISAG-Airport-Service-Holding-AG--14372634-inline.html
    {
        "folder": "WISAG Muenchen Werkstudent Data Scientist Aviation",
        "company": "WISAG Airport Service Holding AG",
        "lang": "de",
        "role_strip": "Werkstudent Data Scientist am Flughafen Muenchen",
        "cl_date": "9. August 2026",
        "cl_subject": "Werkstudent Data Scientist am Flughafen Muenchen, Kennziffer 420548",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Datenauswertung, BI Reporting und Vertragsdaten Analyse. Ich habe eine end to end Echtzeit Pipeline fuer ueber 128 tausend Live Flugpositionen ueber Deutschland auf Google Cloud betrieben und ein interaktives Tableau Dashboard mit parameter gesteuerter Analytik veroeffentlicht. Sicher in Python, SQL, Excel und BI Werkzeugen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Scientist am Flughafen Muenchen, Kennziffer 420548. Die Ausschreibung, Erstellung neuer Reports im Business Intelligence System Qlik, Erkennen von Datenmustern in Qlik Reports, Zuarbeit fuer die Faktura, Validierung der Datenqualitaet von zugelieferten Daten unserer Subunternehmer und der Aufbau von Excel Reports, deckt sich sehr gut mit den BI und Datenqualitaetsthemen, die ich in den letzten Monaten in eigenen Projekten praktisch umgesetzt habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline fuer die SRH Heidelberg habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, den naechstgelegenen Flughafen pro Flugzeug mit PySpark berechnet und das Gesamtsystem mit Apache Airflow auf GCS und Dataproc alle 15 Minuten unbeaufsichtigt orchestriert, mit einer Tableau Analytics Oberflaeche, die den Effekt Luftverkehr sinkt bei Starkregen um Faktor 4,4 an Drehkreuzen wie Frankfurt und Muenchen sichtbar machte. Dieselbe Denkweise, Datenmuster in operativen Aviation Daten zu erkennen, will ich am Standort Muenchen einbringen.",
            "In meinem Fast Food Tableau Dashboard habe ich mit Set Actions einen dynamischen Warenkorb gebaut, mit parameter gesteuerter Analytik einen dynamischen Y Achsen Wechsel per CASE Statement umgesetzt und komplexe IF THEN Calculated Fields fuer Trap Item Flagging geschrieben. Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden.",
            "Ich arbeite sicher in Python, SQL, Excel und Tableau und habe die SAS Visual Business Analytics, Google Data Analytics Foundations und AWS Academy Cloud Foundations Zertifikate abgelegt. Die Luftverkehrsbranche fasziniert mich seit meiner Flugtracking Pipeline. Ich wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche am Standort Muenchen und im Homeoffice einsteigen. Gerne bespreche ich meinen Beitrag im persoenlichen Gespraech.",
        ],
    },
]
