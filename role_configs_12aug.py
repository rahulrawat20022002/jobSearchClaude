"""Role configurations for the 12 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 3 rows in status
'drafted' at run start (the three roles from the 11 August 2026 run: 1&1
Versatel Duesseldorf, SCHOTT AG Mainz, HDI AG Hannover). CSV in agreement.
3 < 8, so under the 28 July 2026 yield based reset the normal top 3 to 5
cut applies. This run ships 5 roles.

Platform mix per 28 July 2026 target weighting (LinkedIn 2, career pages
1 to 2, StepStone 1, Xing 1, Indeed 0 to 1):
  - Career pages: 3 (BMW, Mercedes-Benz, SAP)
  - LinkedIn: 1 (Commerzbank)
  - StepStone: 1 (ARRK Engineering)
  - Xing: 0 this run
  - Indeed: 0 this run
Balanced away from StepStone-only 11 August run. LinkedIn slightly under
weight because most Werkstudent LinkedIn snippets returned aggregator
stubs and were dropped rather than shipped with unverifiable bodies.

Freshness order per 12 July 2026 priority rule (freshness first, then role
type Masterarbeit boost, then Best for overlap), within the single Germany
tier:
  1. Commerzbank Frankfurt Praktikant Big Data & Advanced Analytics AI, 1 day, Praktikum, DE
  2. BMW München Abschlussarbeit KI-Agenten Produktionsplanung Hochvoltspeicher, few days, Masterarbeit, DE
  3. SAP Walldorf Working Student Engagement Lead AI Vision Cases, ~2 weeks, Werkstudent, EN
  4. ARRK Engineering München Werkstudent Machine Learning Automated Driving, ~1 week, Werkstudent, DE
  5. Mercedes-Benz AG Sindelfingen Masterarbeit Learning Dexterous Robot Manipulation, ~3 weeks, Masterarbeit, DE

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Commerzbank posting body written in German -> DE track
  2. BMW Abschlussarbeit posting body written in German -> DE track
  3. SAP Working Student posting body written in English, requires fluent
     English AND German. English body wins -> EN track
  4. ARRK Engineering posting body written in German -> DE track
  5. Mercedes-Benz Masterarbeit posting body written in German -> DE track

Dedup check: all five company plus role combinations verified absent from
applied-log.csv and Notion.
  - SAP is in the log for other Working Student roles but not this
    Engagement Lead AI Vision Cases role, allowed under the 'different
    roles at the same company' rule.
  - BMW Group is in the log for other Master Thesis roles but not this
    KI-Agenten Produktionsplanung Hochvoltspeicher role.
  - Mercedes-Benz AG is in the log for other roles but not this Robot
    Manipulation Masterarbeit.
  - Commerzbank and ARRK Engineering are new companies.
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


CONFIGS_12AUG = [
    # 1. Commerzbank AG Frankfurt
    # Praktikant*in im Bereich Big Data & Advanced Analytics - Projektcontrolling Artificial Intelligence
    # LinkedIn, 1 day old, Praktikum, DE track
    # Start 01.10.2026, 2349,10 EUR / month, Frankfurt am Main
    # Apply: https://de.linkedin.com/jobs/view/praktikant-in-im-bereich-big-data-advanced-analytics-projektcontrolling-artificial-intelligence-at-commerzbank-ag-4449819273
    {
        "folder": "Commerzbank Frankfurt Praktikant Big Data Advanced Analytics Projektcontrolling AI",
        "company": "Commerzbank AG",
        "lang": "de",
        "role_strip": "Praktikant Big Data und Advanced Analytics, Projektcontrolling AI",
        "cl_date": "12. August 2026",
        "cl_subject": "Praktikum Big Data und Advanced Analytics, Projektcontrolling AI in Frankfurt",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Big Data, Advanced Analytics und regulierten Finanzumgebungen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut und in CreditIQ ein Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt hat. Sicher in Python, SQL, scikit-learn und im Zusammenspiel von KI Modellen mit Reporting und Controlling.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Praktikum im Bereich Big Data und Advanced Analytics mit Fokus auf das Projektcontrolling des AI Programms am Standort Frankfurt am Main ab dem 1. Oktober 2026. Die Konsolidierung von Budgets, Kosten und Wertbeitraegen eines KI Programms und die Aufbereitung dieser Finanzinformationen fuer Steuerung und Reporting deckt sich sehr gut mit der Arbeit an regulierten datengetriebenen Systemen, die ich in den letzten Monaten gemacht habe.",
            "In CreditIQ habe ich unter EU AI Act und AGG ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, bei einer Unit Test Branch Coverage von 100 Prozent, plus eine SHAP getriebene Subgruppenanalyse ueber ein Alter mal Geschlecht Threshold Raster. Das gesamte Vorgehen ist in einem GDPR Article 22 und EU AI Act Article 14 konformen regulatorischen Report dokumentiert, der die Fairness Accuracy Abwaegung als bewusste und regulatorisch verteidigbare Entscheidung ausweist.",
            "In meinem Multi Agent RAG Projekt habe ich ein hybrides BM25 plus Dense Retrieval System zu einer mehrsprachigen EN und DE Pipeline erweitert und einen LLM as Judge JudgeAgent implementiert, der Antworten auf 5 Dimensionen bewertet. Der Judge Qwen2.5 14B laeuft bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B, damit Self Preference Bias eliminiert wird, plus ein EvalAgent, der 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports liefert. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden.",
            "Ich arbeite sicher in Python, SQL und mit dem typischen Data Science Stack Pandas, NumPy, scikit-learn und PyTorch, plus Tableau und Looker Studio fuer Reporting. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann zum 1. Oktober 2026 in Frankfurt starten. Gerne bespreche ich meinen Beitrag zu Ihrem Big Data und Advanced Analytics Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. BMW Group München
    # Abschlussarbeit Entwicklung von KI-Agenten für die Produktionsplanung von Hochvoltspeichern (w/m/x)
    # BMW Group career page, few days old, Masterarbeit, DE track
    # Apply: https://www.bmwgroup.jobs/de/de/jobfinder/job-description-copy.162388.html
    {
        "folder": "BMW Muenchen Abschlussarbeit KI-Agenten Produktionsplanung Hochvoltspeicher",
        "company": "BMW Group",
        "lang": "de",
        "role_strip": "Abschlussarbeit KI-Agenten fuer die Produktionsplanung von Hochvoltspeichern",
        "cl_date": "12. August 2026",
        "cl_subject": "Abschlussarbeit KI-Agenten fuer die Produktionsplanung von Hochvoltspeichern",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau von Multi Agenten KI Systemen und produktionsnahen Datenpipelines. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut, das ueber einen LanguageAgent, JudgeAgent und EvalAgent orchestriert wird, und bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen fuer Umweltindikatoren geliefert. Sicher in Python, scikit-learn, LangGraph und in der Einbindung von Large Language Models.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Abschlussarbeit zur Entwicklung von KI Agenten fuer die Produktionsplanung von Hochvoltspeichern im neuen BMW Group Werk in Irlbach-Strass am Standort Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich das Thema besonders, weil Agentic AI in der Produktionsplanung genau der Anwendungsfall ist, an dem ich in den letzten Monaten praktisch gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein orchestriertes Agentensystem in LangGraph gebaut, das aus einem LanguageAgent, einem JudgeAgent und einem EvalAgent besteht. Der LanguageAgent zentralisiert Sprach Erkennung mit einem Confidence Floor und propagiert die Ausgabesprache an jeden nachgelagerten Agenten. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 und laeuft bewusst auf einem anderen lokalen Modell Qwen2.5 14B als der Generator Mistral 7B, damit Self Preference Bias eliminiert wird. Das gleiche Muster aus spezialisierten Agenten, harten Failure Modi und JSON strukturierten Ausgaben laesst sich direkt auf die Produktionsplanung uebertragen, wo unterschiedliche Agenten fuer Materialplanung, Kapazitaetsplanung und Ausfallbehandlung orchestriert werden koennen.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden. Ein Orchestrator mit Gate Checks, oekologischen Clips und einer Velocity Clamp macht die Pipeline auditierbar, ein Muster, das auf produktionsnahe Prognosen von Hochvoltspeicher Zellen sehr gut passt. In meinem Real Time Flight Tracking Projekt habe ich zusaetzlich Python Collectors auf einer Live API mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt und das Gesamtsystem mit Apache Airflow auf GCS und Dataproc alle 15 Minuten unbeaufsichtigt orchestriert.",
            "Ich arbeite sicher in Python, LangGraph, scikit-learn und PyTorch und in der Einbindung von Large Language Models. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann fuer die Abschlussarbeit nach Muenchen umziehen oder pendeln. Gerne bespreche ich meinen Beitrag zum Aufbau des neuen Werks in einem persoenlichen Gespraech.",
        ],
    },

    # 3. SAP Walldorf
    # Working Student (f/m/d) - Engagement Lead to support and drive our AI Vision Cases
    # SAP career page, ~2 weeks old, Werkstudent, EN track
    # Apply: https://jobs.sap.com/job/Walldorf-Working-Student-%28fmd%29-Engagement-Lead-to-support-and-drive-our-AI-Vision-Cases-69190/1379472733
    {
        "folder": "SAP Walldorf Working Student Engagement Lead AI Vision Cases",
        "company": "SAP",
        "lang": "en",
        "role_strip": "Working Student, Engagement Lead for AI Vision Cases",
        "cl_date": "12 August 2026",
        "cl_subject": "Working Student, Engagement Lead for AI Vision Cases in Walldorf",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience in AI systems, LLM integration, and evaluation harnesses. I built a multi agent RAG system with an LLM as Judge evaluation running locally on Ollama with Mistral 7B and Qwen2.5 14B, and delivered a recursive time series pipeline for four water quality indicators at eRay GmbH using CatBoost MultiQuantile with 80 percent prediction intervals. Comfortable across Python, SQL, scikit-learn, LangGraph, and stakeholder communication.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position as Engagement Lead to support and drive AI Vision Cases at SAP in Walldorf. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of driving AI use cases end to end, coordinating across engineering and business stakeholders, and getting hands on with modern LLM tooling maps very closely to what I have been doing in the last several months.",
            "In my Multi Agent RAG project I extended an English only BM25 plus dense hybrid retrieval system over a 14 document policy corpus into a full multilingual EN and DE pipeline by migrating embeddings and retrieval to a paraphrase multilingual MiniLM L12 v2 shared vector space, so a German query retrieves English sources and is answered in German end to end. I implemented a JudgeAgent that scores answers on 5 dimensions using JSON mode at temperature 0, and eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B, plus an EvalAgent computing 5 retrieval metrics and 4 generation metrics aggregated per language into JSON and Markdown reports. The same evaluation harness pattern would let a Vision Cases team keep an honest read on whether a use case is actually improving.",
            "In CreditIQ I lifted the Disparate Impact ratio from a failing 0.79 to a compliant 0.88 under the EU AI Act and AGG 80 percent fairness bar, brought the false negative rate down from 44 percent to 16.7 percent while accuracy held at 75 percent, and shipped the model as a Streamlit decision support tool with a plain language LLM generated explanation, backed by unit tests at 100 percent branch coverage and a full regulatory write up. At eRay GmbH I delivered a recursive time series pipeline for four water quality indicators and chose CatBoost Multi Quantile regression with asymmetric 80 percent prediction intervals as the shipped model.",
            "I work comfortably in Python, SQL, scikit-learn, PyTorch and LangGraph and have hands on experience with LLM integration. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Walldorf or Munich in a hybrid setup and would welcome the chance to discuss how I could contribute to your AI Vision Cases team.",
        ],
    },

    # 4. ARRK Engineering GmbH München
    # Werkstudent (m/w/d) – Machine Learning Automated Driving
    # StepStone, fresh (~1 week), Werkstudent, DE track
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-m-w-d-Machine-Learning-Automated-Driving-Muenchen-ARRK-Engineering-GmbH--13946464-inline.html
    {
        "folder": "ARRK Engineering Muenchen Werkstudent Machine Learning Automated Driving",
        "company": "ARRK Engineering GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Machine Learning Automated Driving",
        "cl_date": "12. August 2026",
        "cl_subject": "Werkstudent Machine Learning Automated Driving in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau und Benchmarking von Machine Learning und Deep Learning Modellen sowie in der Verarbeitung grosser Sensor- und Zeitreihen Datensaetze. Ich habe bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen fuer Umweltindikatoren geliefert und ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut. Sicher in Python, PyTorch, scikit-learn und im sauberen Umgang mit heterogenen Datenquellen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Machine Learning Automated Driving am Standort Muenchen Unterschleissheim. Die Ausschreibung, Unterstuetzung bei der Entwicklung und Implementierung von Machine Learning Modellen fuer autonome Fahrsysteme und die enge Zusammenarbeit mit Softwareentwicklern und Systemingenieuren, deckt sich sehr gut mit dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert und sechs Modelle Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet direkt verglichen. Ich habe mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden und mit einem 3 Pass Outlier System, einem Orchestrator mit Gate Checks und oekologischen Clips die Pipeline gegen Sensordriften abgesichert. Das gleiche disziplinierte Modell Benchmarking mit klarer Metrik pro Ziel laesst sich direkt auf ML Modelle fuer Sensor- und Steuersignale im autonomen Fahren uebertragen.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning und dbt Modellierung ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt und ueber Apache Airflow auf GCS und Dataproc alle 15 Minuten unbeaufsichtigt orchestriert. Zusaetzlich habe ich in meinem Multi Agent RAG Projekt einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen bewertet, der Judge Qwen2.5 14B laeuft bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B, damit Self Preference Bias eliminiert wird.",
            "Ich arbeite sicher in Python, PyTorch und scikit-learn und dokumentiere Ergebnisse und Vorgehen fuer nachgelagerte Code Reviews. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Als Werkstudent kann ich 20 Stunden pro Woche hybrid aus Muenchen Unterschleissheim und Home Office einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Automated Driving Team in einem persoenlichen Gespraech.",
        ],
    },

    # 5. Mercedes-Benz AG Sindelfingen
    # Student*in für Masterarbeit: Learning Dexterous Robot Manipulation from Human Demonstrations
    # Mercedes-Benz career page, ~3 weeks old but still open with Oct 2026 start, Masterarbeit, DE track
    # Location: Mercedes-Benz Plant Sindelfingen (contact at Böblingen office)
    # Apply: https://jobs.mercedes-benz.com/en/studentin-fur-masterarbeit-learning-dexterous-robot-manipulation-from-human-demonstrations-231010-mer00046d1
    {
        "folder": "Mercedes-Benz Sindelfingen Masterarbeit Learning Dexterous Robot Manipulation",
        "company": "Mercedes-Benz AG",
        "lang": "de",
        "role_strip": "Masterarbeit Learning Dexterous Robot Manipulation from Human Demonstrations",
        "cl_date": "12. August 2026",
        "cl_subject": "Masterarbeit Learning Dexterous Robot Manipulation from Human Demonstrations",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau, Benchmarking und der wissenschaftlich sauberen Evaluation von Machine Learning Systemen. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation ueber Ollama mit Mistral 7B und Qwen2.5 14B gebaut, das Antworten auf 5 Dimensionen bewertet, und bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen geliefert. Sicher in Python, PyTorch, Linux und in der Ableitung nachvollziehbarer Ergebnisse aus experimentellen Daten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit im Team AI Research Physical AI zum Thema Learning Dexterous Robot Manipulation from Human Demonstrations am Mercedes-Benz Werk Sindelfingen mit Startdatum 1. Oktober 2026. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich besonders der Zusammenhang zwischen Demonstrationsdaten, Teleoperationsverfahren und der Generalisierungsfaehigkeit moderner Robot Learning Systeme, weil ich in meinen bisherigen Projekten wiederholt die Bruecke zwischen Datenqualitaet, Modellwahl und ehrlicher Evaluation geschlagen habe.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet direkt verglichen und mich fuer CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden. Die September Evaluation wurde belastbar gemacht mit einem 3 Pass Outlier System, dem Ausschluss von 5 spaerlichen Sensoren plus 3 zeitgleichen Proxies und einer rollenden z-score Kontrolle, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff und 0,81 bei pH freilegte. Genau diese disziplinierte Untersuchung des Einflusses von Datenqualitaet auf die Modellleistung ist in Ihrer Arbeit gefragt.",
            "In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Zusaetzlich habe ich einen EvalAgent gebaut, der 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports liefert. Diese Systematik im Aufbau von Evaluations- und Benchmarking Rahmen kann ich direkt in ein Benchmark fuer Imitation Learning Baselines und Vision Language Action Fine Tuning einbringen.",
            "Ich arbeite sicher in Python, PyTorch und Linux und habe erste Erfahrung mit Deep Learning Frameworks aus meiner Bachelorarbeit zur Diabetes Praediktion und aus dem Multi Agent RAG Projekt. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann fuer die Masterarbeit ab dem 1. Oktober 2026 in Sindelfingen einsteigen und den Standort gut aus Mannheim erreichen. Gerne bespreche ich meinen Beitrag zum Team Physical AI in einem persoenlichen Gespraech.",
        ],
    },
]
