"""Role configurations for the 8 August 2026 job search run.

Backlog gate: Notion showed 0 drafted rows at run start on 8 August 2026 after
CSV to Notion reconciliation (15 CSV drafted rows were stale and synced back
to their real Notion status; SAP Walldorf drafted row was drift and backfilled
to Notion in this run). 0 drafted rows triggers the normal top 3 to 5 cut per
the 28 July 2026 yield-based reset. This run ships 4 roles, capped by quality
and platform reachability rather than by rule.

Platform mix this run: StepStone 3, SAP Career Page 1, LinkedIn 0, Xing 0,
Indeed 0. LinkedIn and Xing were thin under WebSearch since the aggregators
mostly returned category pages rather than fresh individual listings, so the
LinkedIn 2 quota from the 28 July rule is documented in the digest transparency
block as an unreachable shortfall rather than silently absorbed.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. Mercedes-Benz AG KI-Cloud-Plattformen (Sindelfingen) DE (body German on StepStone, confirmed via web_fetch)
  2. Hirschmann Automation Agentic Pentesting  (Neckartenzlingen) DE (title and body German on StepStone)
  3. Liebherr-Aerospace Lindenberg Data Science and KI (Lindenberg im Allgaeu) DE (German title on StepStone)
  4. SAP CSAI AI Developer (Walldorf) EN (SAP jobs.sap.com English career page)

Freshness ordering per 12 July 2026 priority rule
(freshness first, then role type Master Thesis > Werkstudent > Praktikum,
then Best for overlap, all within the single Germany tier):
  1. Mercedes-Benz AG KI-Cloud-Plattformen  1 day ago,  Master Thesis (fresh + thesis boost)
  2. Hirschmann Automation Agentic Pentesting  2 days ago, Master Thesis
  3. Liebherr-Aerospace Data Science and KI    1 week ago, Master Thesis
  4. SAP CSAI AI Developer                     Werkstudent, English track
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA,
    CERT_AWS,
    CERT_SAS,
    CERT_GOOGLE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_CREDITIQ_EN,
    P_FLIGHT_EN,
    P_MOVIE_EN,
    P_TABLEAU_EN,
    P_CLIMATE_EN,
    P_HADOOP_EN,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_08AUG = [
    # 1. Mercedes-Benz AG Sindelfingen
    # Student*in fuer Masterarbeit: KI-Cloud-Plattformen fuer intelligentes Fahrzeugtesting
    # StepStone, 7 August 2026, Master Thesis, DE track
    # Apply: https://www.stepstone.de/stellenangebote--Studentin-fuer-Masterarbeit-KI-Cloud-Plattformen-fuer-intelligentes-Fahrzeugtesting-Sindelfingen-Mercedes-Benz-AG--14317081-inline.html
    {
        "folder": "Mercedes-Benz AG Masterarbeit KI-Cloud-Plattformen Fahrzeugtesting Sindelfingen",
        "company": "Mercedes-Benz AG",
        "lang": "de",
        "role_strip": "Masterarbeit KI Cloud Plattformen fuer intelligentes Fahrzeugtesting",
        "cl_date": "8. August 2026",
        "cl_subject": "Masterarbeit KI Cloud Plattformen fuer intelligentes Fahrzeugtesting in Sindelfingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in cloudbasierten Machine Learning Pipelines, KI Anomalieerkennung und praediktiver Modellierung. Ich habe eine end to end rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und asymmetrischen 80 Prozent Vorhersageintervallen bei eRay GmbH geliefert, ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt und eine cloud native Batch Pipeline auf GCP mit BigQuery ML gebaut. Sicher in Python, scikit learn, CatBoost, BigQuery, dbt, Airflow und API basierten KI Diensten, mit klarem Blick fuer Anti Leakage, Governance und automatisierte Berichterstellung.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_NVIDIA_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit KI Cloud Plattformen fuer intelligentes Fahrzeugtesting am Standort Sindelfingen, Stellennummer MER00045VE. Die Ausschreibung, die Konzeption einer cloudbasierten Big Data Anwendung zur Testauswertung, die Entwicklung von KI Algorithmen zur automatisierten Auswertung, automatisierte Berichterstellung mit Muster und Anomalieerkennung sowie praediktive Modelle fuer e-Drive Tests, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten gebaut und dokumentiert habe.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen, mich fuer CatBoost Multi Quantil Regression entschieden und asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung ausgeliefert. Ich habe strenge Anti Leakage Regeln durchgesetzt und die Pipeline mit einem Orchestrator mit Gate Checks umschlossen, der bei fehlgeschlagener Imputation stoppt statt schlechte Daten weiterfliessen zu lassen. Genau diese Erfahrung mit ML basierten Modellen fuer Anomalie und praediktive Analytik bringe ich in Ihr Fahrzeugtesting ein.",
            "In meiner cloud nativen Movie Analytics Pipeline habe ich mit BigQuery, Cloud Run, GCS und Cloud Scheduler eine vollautomatisierte Medallion Architektur von Bronze ueber Silber bis Gold auf GCP gebaut, einen BigQuery ML Klassifikator mit leckagefreier Vor Release Feature Trennung trainiert und die Ausgabe ueber ein Looker Studio Dashboard und ein Gold Layer Aggregat ausgeliefert. In CreditIQ habe ich den Disparate Impact von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert, alles nach EU AI Act und GDPR Article 22 dokumentiert.",
            "Ich arbeite sicher in Python, Git und mit API basierten KI Diensten, dokumentiere Methoden und Ergebnisse fuer den Wissenstransfer im Team und kann komplexe Big Data Fragestellungen strukturiert in Proofs of Concept ueberfuehren. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die AWS Academy Cloud Foundations, NVIDIA Building LLM Applications With Prompt Engineering und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech mit Ihrem Team in Sindelfingen.",
        ],
    },

    # 2. Hirschmann Automation and Control GmbH Neckartenzlingen
    # Masterarbeit Agentic Pentesting: Entwicklung und Evaluation eines KI-Agenten
    # StepStone, 2 days ago, Master Thesis, DE track
    # Apply: https://www.stepstone.de/stellenangebote--Masterarbeit-zum-Thema-Agentic-Pentesting-Entwicklung-und-Evaluation-eines-KI-Agenten-zur-Automatisierung-von-Pentest-Workflows-m-w-d-Neckartenzlingen-Hirschmann-Automation-and-Control-GmbH--14372911-inline.html
    {
        "folder": "Hirschmann Automation Masterarbeit Agentic Pentesting KI Agent Neckartenzlingen",
        "company": "Hirschmann Automation and Control GmbH",
        "lang": "de",
        "role_strip": "Masterarbeit Agentic Pentesting und KI Agenten fuer Pentest Workflows",
        "cl_date": "8. August 2026",
        "cl_subject": "Masterarbeit Agentic Pentesting: Entwicklung und Evaluation eines KI Agenten zur Automatisierung von Pentest Workflows in Neckartenzlingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in KI Agenten, Retrieval Augmented Generation und LLM Orchestrierung. Ich habe einen Hybrid RAG Orchestrator mit agentischem Routing ueber Llama 3.1 8b via Groq und LangChain gebaut, ein Fairness by Design Credit Scoring System mit ehrlicher Evaluation nach EU AI Act geliefert und eine end to end Zeitreihen Pipeline bei eRay GmbH mit Gate Checks und Governance Regeln umgesetzt. Sicher in Python, LangChain, Git und API basierten LLM Diensten, mit klarem Blick fuer Evaluation, Guardrails und Nachvollziehbarkeit agentischer Workflows.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit Agentic Pentesting bei Hirschmann Automation and Control in Neckartenzlingen. Die Ausschreibung, die Entwicklung und Evaluation eines KI Agenten zur Automatisierung von Pentest Workflows, deckt sich sehr genau mit den Themen, an denen ich in den letzten Monaten gearbeitet habe.",
            "In meinem Hybrid RAG Orchestrator habe ich einen eigenen Decision Making Router auf Basis von Llama 3.1 8b via Groq und LangChain umgesetzt, der Nutzerintent in drei Ausfuehrungspfade klassifiziert, lokale Wissensrecherche, externe Websuche oder direkte konversationelle Logik. Ein zustandsbehafteter MemoryAgent haelt Mehrturn Kontext ueber ChromaDB und HuggingFace Embeddings, und das System laeuft als deployter Streamlit Prototyp end to end. Genau diese Erfahrung mit Agent Definition, Routing, Guardrails und Wissenstransfer bringe ich in die Entwicklung Ihres Pentest Agenten ein.",
            "In CreditIQ habe ich eine Fairness by Design Pipeline geliefert, den Disparate Impact von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert. Bei eRay GmbH habe ich sechs Modelle direkt verglichen, strenge Anti Leakage Regeln durchgesetzt und einen Orchestrator mit Gate Checks gebaut, der bei fehlgeschlagener Imputation stoppt statt schlechte Daten weiterfliessen zu lassen. Meine Bachelorarbeit vergleicht sechs Klassifikatoren mit 10 facher Kreuzvalidierung und wurde als IEEE Paper mit ehrlicher Limitations Sektion verfasst.",
            "Ich arbeite sicher in Python, Git und mit API basierten LLM Diensten wie OpenAI und Groq, dokumentiere Methoden und Ergebnisse fuer den Wissenstransfer im Team und kann komplexe Problemstellungen strukturiert in Proofs of Concept ueberfuehren. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech mit Ihrem Team in Neckartenzlingen.",
        ],
    },

    # 3. Liebherr-Aerospace Lindenberg GmbH Lindenberg im Allgaeu
    # Abschlussarbeit Masterarbeit im Bereich Data Science und Kuenstliche Intelligenz
    # StepStone, 1 week ago, Master Thesis, DE track
    # Apply: https://www.stepstone.de/stellenangebote--Abschlussarbeit-Masterarbeit-im-Bereich-Data-Science-Kuenstliche-Intelligenz-Lindenberg-im-Allgaeu-Liebherr-Aerospace-Lindenberg-GmbH--14332119-inline.html
    {
        "folder": "Liebherr-Aerospace Lindenberg Masterarbeit Data Science KI",
        "company": "Liebherr-Aerospace Lindenberg GmbH",
        "lang": "de",
        "role_strip": "Masterarbeit Data Science und Kuenstliche Intelligenz",
        "cl_date": "8. August 2026",
        "cl_subject": "Abschlussarbeit Masterarbeit im Bereich Data Science und Kuenstliche Intelligenz in Lindenberg im Allgaeu",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Machine Learning Pipelines, Modellvergleich und robuster Bewertung. Ich habe eine rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und asymmetrischen 80 Prozent Vorhersageintervallen bei eRay GmbH geliefert, ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt und eine end to end Cloud Pipeline auf GCP mit BigQuery ML fuer Analytik und Vorhersage gebaut. Sicher in Python, scikit learn, CatBoost, LightGBM, XGBoost, BigQuery ML und PyTorch, mit klarem Blick fuer Simulation, Anti Leakage und ehrliche Modellauswertung.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Abschlussarbeit Masterarbeit im Bereich Data Science und Kuenstliche Intelligenz bei Liebherr-Aerospace Lindenberg. Die Ausschreibung, die Anwendung von Machine Learning und KI Methoden auf Luftfahrt und Produktionsdaten sowie die Entwicklung belastbarer Datenpipelines, deckt sich sehr genau mit den Themen, an denen ich in den letzten Monaten gearbeitet habe.",
            "Bei eRay GmbH habe ich waehrend einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule Heidelberg eine rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, sechs Modelle direkt verglichen, mich fuer CatBoost Multi Quantil Regression entschieden und asymmetrische 80 Prozent Vorhersageintervalle als Entscheidungsunterstuetzung ausgeliefert. Ich habe strenge Anti Leakage Regeln durchgesetzt, fehlende Winter Messwerte mit MICE Imputation rekonstruiert und die Pipeline mit einem Orchestrator mit Gate Checks umschlossen, der bei fehlgeschlagener Imputation stoppt statt schlechte Daten weiterfliessen zu lassen.",
            "In CreditIQ habe ich eine Fairness by Design Pipeline geliefert, den Disparate Impact von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert. In meiner cloud nativen Movie Analytics Pipeline habe ich mit BigQuery, Cloud Run und Cloud Scheduler eine vollautomatisierte Medallion Architektur auf GCP gebaut und einen BigQuery ML Klassifikator mit leckagefreier Vor Release Feature Trennung trainiert. Meine Bachelorarbeit vergleicht sechs Klassifikatoren mit 10 facher Kreuzvalidierung und wurde als IEEE Paper mit ehrlicher Limitations Sektion verfasst.",
            "Ich arbeite sicher in Python, Git und mit API basierten KI Diensten, dokumentiere Methoden und Ergebnisse fuer den Wissenstransfer im Team und kann komplexe Problemstellungen strukturiert in Proofs of Concept ueberfuehren. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech mit Ihrem Team in Lindenberg im Allgaeu.",
        ],
    },

    # 4. SAP CSAI Walldorf
    # Working Student (f/m/d) CSAI AI Developer
    # SAP Career Page (jobs.sap.com), Werkstudent, EN track
    # Apply: https://jobs.sap.com/job/Walldorf-Working-Student-(fmd)-CSAI-AI-Developer-69190/1406299533/
    {
        "folder": "SAP Working Student CSAI AI Developer Walldorf",
        "company": "SAP",
        "lang": "en",
        "role_strip": "Working Student CSAI AI Developer",
        "cl_date": "8 August 2026",
        "cl_subject": "Working Student CSAI AI Developer in Walldorf",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim with hands on practice in agentic LLM systems, Retrieval Augmented Generation and end to end machine learning pipelines. I built a Hybrid RAG Orchestrator on top of Llama 3.1 8b via Groq and LangChain with a custom routing agent, delivered a Fairness by Design credit scoring system aligned with the EU AI Act and shipped a recursive time series pipeline at eRay GmbH with gate checks and governance rules. Comfortable in Python, LangChain, Git and API based LLM services, with a clear eye for evaluation, guardrails and traceable agent behaviour.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student CSAI AI Developer role in Walldorf. The posting, contributing to AI developer tooling and prototypes for the Customer Support and AI group at SAP, aligns closely with the systems I have been building and shipping over the past months.",
            "In my Hybrid RAG Orchestrator I built a custom decision making router on top of Llama 3.1 8b via Groq and LangChain that classifies user intent into three execution paths, local knowledge retrieval over ChromaDB and HuggingFace MiniLM embeddings, external web search or direct conversational logic. A stateful MemoryAgent keeps multi turn context intact and the whole system ships as a deployed Streamlit prototype. That is the same shape of work SAP is asking for on the CSAI side, agentic LLM prototypes that hold up beyond a demo.",
            "In CreditIQ I delivered a Fairness by Design pipeline that raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88, brought the false negative rate down from 44 percent to 16.7 percent while accuracy held at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up. At eRay GmbH I benchmarked six models head to head, enforced strict anti leakage rules and wrapped the recursive pipeline in a governance orchestrator with gate checks so a failed imputation halts the run rather than corrupting weeks of downstream predictions.",
            "I work confidently in Python, Git and API based LLM services such as OpenAI and Groq, document methods and results for team hand off and can move complex problems into shippable proofs of concept. English is my working language and my German level is B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics Foundations certificates and was recognised as a Finalist at Graduate Level in the USAII Global AI Hackathon 2026. I would appreciate the chance to discuss how I could contribute to the CSAI team in Walldorf.",
        ],
    },
]
