"""Role configurations for the 11 August 2026 job search run.

Backlog gate check: Notion returned 0 rows in status 'drafted' at run start
(all 9 previously-drafted rows from the 4/8/9 August runs have been flipped
by Rah to applied or rejected). Notion is the source of truth per 14 July
2026 rule. CSV was reconciled to match. 0 drafted rows is under the 8-row
soft cap of the 28 July 2026 yield-based reset, so normal top 3 to 5 cut
applies. This run ships 3 roles, capped by supply of clean fresh candidates
in reachable sources this run.

Platform mix this run: StepStone 3, LinkedIn 0, Xing 0, Indeed 0, career page 0.
This is StepStone-only, heavier than the 28 July 2026 weighting. Multiple
LinkedIn URLs (ABB Mannheim x2) and career pages resolved to expired postings
during URL verification, so they were dropped rather than shipped with
broken apply links. This gap is documented in the digest transparency block.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. SCHOTT AG Mainz WerkstudentIn Data Science, Machine Learning und AI: DE (body German on StepStone)
  2. 1&1 Versatel Duesseldorf Werkstudent Data Science und AI: DE (body German on StepStone)
  3. HDI AG Hannover Werkstudent Data Engineering und Analytics im Aktuariat: DE (body German on StepStone)

Freshness ordering per 12 July 2026 priority rule
(freshness first, then role type, then Best for overlap, all within the
single Germany tier):
  1. 1&1 Versatel Duesseldorf   21 hours old, Werkstudent, DE (freshest)
  2. SCHOTT AG Mainz             1 day old,   Werkstudent, DE
  3. HDI AG Hannover             ~17 days old, Werkstudent, DE
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


CONFIGS_11AUG = [
    # 1. 1&1 Versatel Duesseldorf
    # Werkstudent Data Science & AI (w/m/d)
    # StepStone, 21 hours ago, Werkstudent, DE track
    # Stack: Python, LLM Integration (GPT), Machine Learning, EDA, Data Visualization
    # Apply: https://www.stepstone.de/stellenangebote--werkstudent-data-science-ai-w-m-d-duesseldorf-11-versatel-gmbh--13850187-inline.html
    {
        "folder": "1und1 Versatel Duesseldorf Werkstudent Data Science AI",
        "company": "1&1 Versatel GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Data Science und AI",
        "cl_date": "11. August 2026",
        "cl_subject": "Werkstudent Data Science und AI in Duesseldorf",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Python, Machine Learning und LLM Integration. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation und lokalem Betrieb ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut sowie bei eRay GmbH eine end to end Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen geliefert. Sicher im Data Science Stack Python, SQL, scikit-learn und in der Einbindung von Large Language Models.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science und AI am Standort Duesseldorf. Die Ausschreibung, Aufbereiten komplexer Datensaetze und explorative Datenanalysen, Unterstuetzung bei der Entwicklung, dem Training und der Evaluierung von ML Modellen mit Python sowie das Experimentieren mit der Einbindung von Large Language Models wie GPT in eine bestehende Infrastruktur, deckt sich sehr genau mit dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein hybrides BM25 plus Dense Retrieval System ueber einen 14 Dokumente Policy Korpus zu einer mehrsprachigen EN und DE Pipeline erweitert, indem Embeddings und Retrieval auf paraphrase multilingual MiniLM L12 v2 in einem gemeinsamen Vektorraum migriert wurden. Ich habe einen LLM as Judge JudgeAgent implementiert, der Antworten auf 5 Dimensionen mit 1 bis 5 bewertet, dabei laeuft der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B, damit Self Preference Bias eliminiert wird, plus einen EvalAgent, der 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports liefert.",
            "In CreditIQ habe ich unter EU AI Act und AGG den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, bei einer Unit Test Branch Coverage von 100 Prozent. Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden.",
            "Ich arbeite sicher in Python und mit dem typischen Data Science Stack Pandas, NumPy, scikit-learn und PyTorch und dokumentiere Python Code fuer nachgelagerte Code Reviews. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche in Duesseldorf oder remote einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. SCHOTT AG Mainz
    # WerkstudentIn Data Science, Machine Learning & AI (m/w/d)*
    # StepStone, 1 day ago, Werkstudent, DE track
    # Stack: Data Science, Machine Learning, AI, Materialdaten und Produktionsdaten Analyse
    # Apply: https://www.stepstone.de/stellenangebote--WerkstudentIn-Data-Science-Machine-Learning-AI-m-w-d-Mainz-SCHOTT-AG--14385051-inline.html
    {
        "folder": "SCHOTT AG Mainz Werkstudent Data Science Machine Learning AI",
        "company": "SCHOTT AG",
        "lang": "de",
        "role_strip": "Werkstudent Data Science, Machine Learning und AI",
        "cl_date": "11. August 2026",
        "cl_subject": "Werkstudent Data Science, Machine Learning und AI in Mainz",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning, KI Anwendungen und Datenanalyse fuer produktionsnahe Fragestellungen. Ich habe bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen fuer Umweltindikatoren geliefert und ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama Mistral 7B und Qwen2.5 14B gebaut. Sicher in Python, SQL, scikit-learn und modernen ML und LLM Werkzeugen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science, Machine Learning und AI am Standort Mainz. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich SCHOTT als forschungsstarker Spezialglas Konzern besonders, weil dort datengetriebene Modelle direkt an realen Prozess und Materialdaten arbeiten. Die Ausschreibung passt sehr gut zu den ML und AI Themen, die ich in den letzten Monaten praktisch umgesetzt habe.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet direkt verglichen und mich fuer CatBoost Multi Quantil Regression entschieden, die asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung lieferte. Strenge Anti Leakage Regeln und ein Orchestrator mit Gate Checks halten die Pipeline auditierbar, ein Muster, das sich sehr gut auf Produktions und Materialdaten uebertragen laesst.",
            "In meinem Multi Agent RAG Projekt habe ich ein hybrides BM25 plus Dense Retrieval System zu einer mehrsprachigen EN und DE Pipeline erweitert und einen LLM as Judge JudgeAgent implementiert, der Antworten auf 5 Dimensionen bewertet, dabei laeuft der Judge bewusst auf einem anderen lokalen Modell als der Generator. In CreditIQ habe ich den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, bei einer Unit Test Branch Coverage von 100 Prozent.",
            "Ich arbeite sicher in Python, scikit-learn, PyTorch und mit modernen LLM Diensten und dokumentiere Methoden und Ergebnisse fuer den fachuebergreifenden Wissenstransfer. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche in Mainz einsteigen, der Standort ist gut aus Mannheim erreichbar. Gerne bespreche ich meinen Beitrag zu Ihrem Data Science Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. HDI AG Hannover
    # Werkstudent:in Data Engineering und Analytics im Aktuariat (m/w/d)
    # StepStone, ~17 days ago but application deadline 20 September 2026
    # Stack: Datenpipelines, Datenanalysen, Ad-hoc Auswertungen, interne Anwendungen
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-Data-Engineering-und-Analytics-im-Aktuariat-Hannover-HDI-AG--14302128-inline.html
    {
        "folder": "HDI AG Hannover Werkstudent Data Engineering Analytics Aktuariat",
        "company": "HDI AG",
        "lang": "de",
        "role_strip": "Werkstudent Data Engineering und Analytics im Aktuariat",
        "cl_date": "11. August 2026",
        "cl_subject": "Werkstudent Data Engineering und Analytics im Aktuariat in Hannover",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenpipelines, Analytik und BI Reporting. Ich habe eine end to end Cloud Batch Pipeline auf GCP mit BigQuery Medallion Architektur und Looker Studio gebaut sowie eine Echtzeit Flugverfolgungs Pipeline mit PySpark, dbt und Apache Airflow ueber 128 tausend Datensaetze orchestriert. Sicher in Python, SQL, PySpark und im Aufbau reproduzierbarer Datenpipelines.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_GOOGLE_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Engineering und Analytics im Aktuariat am Standort Hannover. Die Ausschreibung, Mitarbeit bei der Weiterentwicklung und Optimierung von Datenpipelines sowie internen Anwendungen und Durchfuehrung von Datenanalysen und Ad-hoc Auswertungen, deckt sich sehr genau mit dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline fuer die SRH Heidelberg habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, den naechstgelegenen Flughafen pro Flugzeug mit PySpark berechnet und das Gesamtsystem mit Apache Airflow auf GCS und Dataproc alle 15 Minuten unbeaufsichtigt orchestriert. In meinem Movie Analytics Projekt auf Google Cloud habe ich eine vollstaendig automatisierte Batch Pipeline mit Bronze Silber Gold Medallion Architektur in BigQuery aufgebaut, Schema Enforcement, sichere Type Casts, Deduplikation per Window Functions und Genre Normalisierung durchgesetzt und ueber ein fuenfseitiges Looker Studio Dashboard Fragen zu Genre ROI und Release Saison Timing beantwortet.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden. Ein Orchestrator mit Gate Checks und oekologischen Grenzen macht die Pipeline auditierbar, was gut zu den Reporting Zyklen im Aktuariat und zur regulierten Versicherungsumgebung passt.",
            "Ich arbeite sicher in Python, SQL und PySpark und habe die AWS Academy Cloud Foundations, Google Data Analytics Foundations und SAS Visual Business Analytics Zertifikate abgelegt. Ich wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche in Hannover oder remote einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Aktuariats Team in einem persoenlichen Gespraech.",
        ],
    },
]
