"""Role configurations for the 16 August 2026 scheduled run.

Backlog gate check per 14 July 2026 status-of-truth rule: Notion data source
fd974369-40b2-48c5-b660-d15256c88f52 returned 8 rows in status 'drafted' at run
start (Retorio, AssetMetrix GmbH, Phoenix Contact, BSH Home Appliances Group,
viadee Unternehmensberatung AG, BMW Muenchen Data Science KI Tool
Qualitaetsanalyse, KfW Bankengruppe Frankfurt IT Data Science KI, Allianz
Insurance Muenchen Data Science). CSV in agreement, no drift.

Per 28 July 2026 yield-based reset rule, 8 drafted = cap at top 3 (soft cap
zone). This run drafts exactly 3.

Reconciliation step per 11 July 2026 rule: CSV and Notion fully in sync at run
start; no drift detected.

Platform mix per 28 July 2026 yield weighting for a top 3 cut: career pages 2
(Siemens jobs portal x2), company careers 1 (Deloitte job.deloitte.com).
LinkedIn/Xing 0 this run (well-covered yesterday). Indeed 0.

Freshness order per 12 July 2026 rule (freshness first, then role type, then
Best-for overlap):
  1. Siemens Energy Werkstudent KI-basierte Optimierungsinitiativen (Job 295654)
     -- fresh listing on jobs.siemens-energy.com, DE posting, LLM + Python focus.
  2. Siemens AG Werkstudent Data Science im operativen Service (Job 503634)
     -- fresh listing on jobs.siemens.com, DE posting, applied Data Science.
  3. Deloitte Werkstudent/Praktikant Digital und AI Analytics (Job 49258)
     -- listed on job.deloitte.com, DE posting, Frankfurt/Stuttgart.

Language track per 20 July 2026 rule: all three postings are DE track (posting
title and body in German).

Dedup check against applied-log.csv and Notion:
  - Siemens Energy: NEW employer, no prior rows in the log.
  - Siemens AG: prior applied row is "Working Student AI Digital Products and
    Process Automation Finance and MA" -- distinct role.
  - Deloitte: NEW employer, no prior rows in the log.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_GOOGLE_DE,
    CERT_SAS_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_16AUG = [
    # 1. Siemens Energy -- Werkstudent (w/m/d) KI-basierte Optimierungsinitiativen
    # jobs.siemens-energy.com, Germany, DE track, Werkstudent
    # Apply: https://jobs.siemens-energy.com/en_US/CareersMarketplace/FolderDetail/Werkstudent-w-m-d-KI-basierte-Optimierungsinitiativen/295654
    {
        "folder": "Siemens Energy Werkstudent KI-basierte Optimierungsinitiativen",
        "company": "Siemens Energy",
        "lang": "de",
        "role_strip": "Werkstudent KI-basierte Optimierungsinitiativen",
        "cl_date": "16. August 2026",
        "cl_subject": "Werkstudent KI-basierte Optimierungsinitiativen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von LLM Werkzeugen, Multi Agent Systemen und Machine Learning Pipelines. Ich habe ein Multi Agent RAG System mit LangGraph, Ollama Mistral 7B und Qwen2.5 14B mit belastbarer LLM as Judge Evaluation ueber 5 Dimensionen gebaut und bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile fuer 4 Umweltindikatoren geliefert. Sicher in Python, SQL, LangGraph, scikit-learn, CatBoost, GCP und AWS.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI-basierte Optimierungsinitiativen bei Siemens Energy. Die Kombination aus angewandter KI, Large Language Models und operativer Prozessoptimierung entspricht genau dem, was ich in den letzten Monaten praktisch gebaut und ausgewertet habe.",
            "In meinem Multi Agent RAG Projekt habe ich mit LangGraph ein orchestriertes Agentensystem entwickelt, das Antworten in Englisch oder Deutsch end to end liefert und ueber einen JudgeAgent auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet wird. Self Preference Bias habe ich eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft, und ein EvalAgent berechnet 5 Retrieval Metriken sowie 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Genau dieses Muster laesst sich auf KI Werkzeuge fuer Optimierungsinitiativen in einem Energieumfeld uebertragen, wo Modelausgaben pruefbar und regulator tauglich sein muessen.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System gebaut, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent bei stabiler Accuracy von 75 Prozent gesenkt. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren geliefert und CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen als Shipped Modell gewaehlt, wobei ich die September Evaluation mit einem 3 Pass Outlier System belastbar gemacht habe.",
            "Ich arbeite sicher in Python, SQL, LangGraph, scikit-learn und CatBoost sowie in AWS und GCP fuer die Cloud Ebene. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann als Werkstudent mit 15 bis 20 Stunden pro Woche einsteigen. Gerne bespreche ich meinen Beitrag zu Ihren KI-basierten Optimierungsinitiativen in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Siemens AG -- Werkstudent (w/m/d) Data Science im operativen Service
    # jobs.siemens.com, Germany, DE track, Werkstudent
    # Apply: https://jobs.siemens.com/en_US/externaljobs/JobDetail/503634
    {
        "folder": "Siemens AG Werkstudent Data Science operativer Service",
        "company": "Siemens AG",
        "lang": "de",
        "role_strip": "Werkstudent Data Science im operativen Service",
        "cl_date": "16. August 2026",
        "cl_subject": "Werkstudent Data Science im operativen Service",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Machine Learning Pipelines, Zeitreihen Modellen und Data Engineering Loesungen fuer operative Umgebungen. Ich habe bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile fuer 4 Umweltindikatoren geliefert und in einem Real-Time Flight Tracking Projekt eine Cloud Pipeline auf GCP mit PySpark, dbt und Airflow ueber 128.000 Flugdatensaetze aufgebaut. Sicher in Python, SQL, scikit-learn, CatBoost, PySpark, BigQuery und Airflow.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_NVIDIA_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science im operativen Service bei Siemens AG. Die Kombination aus angewandter Datenanalyse, Machine Learning fuer Service Prozesse und der Uebersetzung von Modellergebnissen in operative Entscheidungen entspricht genau dem, was ich in den letzten Monaten praktisch geliefert habe.",
            "Bei eRay GmbH habe ich in einer 6 monatigen Kooperation mit der SRH Heidelberg eine end to end rekursive Zeitreihen Pipeline ueber 4 Wasserqualitaets Indikatoren gebaut, dabei 6 Kandidaten Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet gebenchmarkt und mich fuer CatBoost MultiQuantile bei alpha 0,05, 0,5 und 0,85 mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden. Die September Evaluation habe ich mit einem 3 Pass Outlier System belastbar gemacht und einen ehrlichen R Quadrat von 0,86 auf dissolved oxygen und 0,81 auf pH ausgewiesen. Genau dieses Muster, Modellauswahl mit Benchmarking und pruefbare Evaluation, laesst sich direkt auf operative Service Daten uebertragen.",
            "Im Real-Time Flight Tracking Projekt habe ich Python Kollektoren gebaut, die die OpenSky Network API alle 30 Sekunden abfragen, und mit PySpark auf Google Cloud eine Bereinigung ueber vier Quellen Flugzeuge, Flughaefen, Wetter und Aircraft Details durchgefuehrt, was zu einem sauberen Joined Table ueber 128 Tausend Datensaetze fuehrte. Mit dbt habe ich die Datenmodellierung uebernommen, Apache Airflow orchestriert das gesamte System auf GCS und Dataproc, und Tableau mit TabPy Statistiken hat die Analyse Oberflaeche geliefert. Diese Erfahrung mit einer produktiven, orchestrierten Data Pipeline passt direkt zu Service Analytics bei Siemens.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, CatBoost, PySpark und Airflow sowie in AWS und GCP fuer die Cloud Ebene. Ich habe die AWS Academy Cloud Foundations, NVIDIA Building LLM Applications With Prompt Engineering und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann als Werkstudent mit 15 bis 20 Stunden pro Woche einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Data Science Team im operativen Service in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Deloitte -- Praktikant / Werkstudent Digital und AI Analytics
    # job.deloitte.com, Frankfurt / Stuttgart, DE track, Werkstudent / Praktikant
    # Apply: https://job.deloitte.com/job-werkstudent-praktikant-im-bereich-digital-und-ai-analytics-mwd-_49258
    {
        "folder": "Deloitte Werkstudent Praktikant Digital AI Analytics",
        "company": "Deloitte",
        "lang": "de",
        "role_strip": "Werkstudent oder Praktikant im Bereich Digital und AI Analytics",
        "cl_date": "16. August 2026",
        "cl_subject": "Werkstudent oder Praktikant Digital und AI Analytics",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Analytics Loesungen, Business Intelligence Dashboards und KI Werkzeugen fuer regulierte und wirtschaftsnahe Fragestellungen. Ich habe in CreditIQ ein Kredit Scoring System unter EU AI Act Konformitaet gebaut, ein Multi Agent RAG System fuer Policy Analyse mit LLM as Judge Evaluation entwickelt und interaktive Tableau Dashboards mit dynamischer Warenkorb Simulation ausgeliefert. Sicher in Python, SQL, scikit-learn, LangGraph, Tableau, Power BI und Looker Studio.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_NVIDIA_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudenten oder Praktikanten Position im Bereich Digital und AI Analytics bei Deloitte. Die Kombination aus Datenanalyse, KI gestuetzten Werkzeugen und der Beratungsnahen Uebersetzung von Modellergebnissen in umsetzbare Entscheidungen entspricht genau dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent bei stabiler Accuracy von 75 Prozent gefallen, und das System laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung, gestuetzt durch Unit Tests bei 100 Prozent Branch Coverage und einer vollstaendigen regulatorischen Dokumentation zu GDPR Artikel 22 und EU AI Act Artikel 14. Genau diese regulatorik nahe Herangehensweise passt zu Deloitte Beratungsprojekten in Financial Services und Risk Analytics.",
            "In einem interaktiven Fast Food Nutritional Tableau Dashboard habe ich mit Set Actions eine dynamische Warenkorb Simulation aufgebaut, in der Endnutzer Punkte im Scatter Plot auswaehlen und die 3 zentralen Makros Kalorien, Fett und Protein fuer eine simulierte Mahlzeit direkt aggregieren. Mit parameter gesteuerten Analysen habe ich eine dynamische Y Achse implementiert, die per CASE Anweisung an ein benutzergesteuertes Ziel Parameter gebunden ist, so dass sich Muskelaufbau und Gewichtsverlust ohne Dashboard Reload umschalten lassen. Ein Is It A Trap Flag markiert taeuschende Trap Items automatisch. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit CatBoost Multi Quantil Regression und asymmetrischen 80 Prozent Vorhersageintervallen geliefert.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph, Tableau, Power BI und Looker Studio. Ich habe die SAS Visual Business Analytics, NVIDIA Building LLM Applications With Prompt Engineering und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann als Werkstudent mit 15 bis 20 Stunden pro Woche oder als Praktikant in einem Pflichtpraktikum einsteigen und stehe fuer die Standorte Frankfurt am Main oder Stuttgart zur Verfuegung. Gerne bespreche ich meinen Beitrag zum Digital und AI Analytics Team von Deloitte in einem persoenlichen Gespraech.",
        ],
    },
]
