"""Role configurations for the 27 July 2026 job search run (top 5, soft backlog cap).

Backlog gate: Notion showed exactly 10 drafted rows at run start on 27 July 2026
(all 10 from the 26 July 2026 run still awaiting Rah's manual apply flip).
CSV also matched Notion 1 to 1 during reconciliation, no drift rows to backfill.
Exactly 10 drafted rows triggers the SOFT backlog cap from the 11 July 2026 rule,
so this run is capped at the top 5 newly scored roles instead of the top 10.

Platform quota per 21 July 2026 rule for a top 5 run under soft cap
(quota is 1 to 2 per platform, all four platforms must appear at least once):
  This run: Indeed 2, StepStone 1, Xing 1, LinkedIn 1, career page 0.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. Mercedes-Benz Tech Innovation Berlin (Agentic AI)   DE (body German on StepStone)
  2. Fraunhofer IIS Dresden (Simulation und ML Robotik)  DE (body German on Fraunhofer/bebee)
  3. STIHL Waiblingen (Data Analytics und ML)            DE (body German on jobs.stihl.com)
  4. YOONA Ventures Berlin (AI Working Student)          EN (body English on yoona.ai career)
  5. Deutsche Telekom MMS Dresden (AI Product Builder)   DE (body German on Indeed listing)

Freshness ordering per 12 July 2026 priority rule
(freshness first, then role type Master Thesis > Werkstudent > Praktikum,
then Best for overlap, all within the single Germany tier):
  1. Mercedes-Benz Tech Innovation      26 July, 1 day ago,  Werkstudent (Agentic AI, GenAI)
  2. Fraunhofer IIS Dresden             26 July, 15 hours,   Praktikum/Abschlussarbeit (thesis boost)
  3. STIHL Waiblingen                   24 July, 3 days ago, Mandatory Praktikum
  4. YOONA Ventures Berlin              23 July, 4 days ago, Werkstudent (GenAI, LLM, CV)
  5. Deutsche Telekom MMS Dresden       22 July, 5 days ago, Werkstudent (KI Produkt)
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


CONFIGS_27JUL = [
    # 1. Mercedes-Benz Tech Innovation — Berlin
    # Werkstudent Agentic AI & Multi-Agent-Systeme (d/m/w/x)
    # (StepStone, 26 July 2026, Werkstudent, DE track)
    {
        "folder": "Mercedes-Benz Tech Innovation Werkstudent Agentic AI Multi-Agent-Systeme Berlin",
        "company": "Mercedes-Benz Tech Innovation",
        "lang": "de",
        "role_strip": "Werkstudent Agentic AI und Multi Agent Systeme",
        "cl_date": "27. Juli 2026",
        "cl_subject": "Werkstudent Agentic AI und Multi Agent Systeme in Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in KI Agenten, Retrieval Augmented Generation und LLM Orchestrierung. Ich habe einen Hybrid RAG Orchestrator mit agentischem Routing ueber Llama 3.1 8b via Groq und LangChain gebaut, ein Fairness by Design Credit Scoring System nach EU AI Act geliefert und eine end to end Zeitreihen Pipeline bei eRay GmbH mit Gate Checks und Governance Regeln umgesetzt. Sicher in Python, LangChain, Git und API basierten KI Diensten, mit klarem Blick fuer Evaluation, Guardrails und Nachvollziehbarkeit agentischer Workflows.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Stelle als Werkstudent Agentic AI und Multi Agent Systeme bei Mercedes-Benz Tech Innovation in Berlin, Stellennummer V000077236. Die Ausschreibung, die Mitentwicklung von KI Agenten, die Weiterentwicklung von Governance Prozessen fuer Multi Agent Systeme und die experimentelle Evaluation von KI Modellen und Workflow Varianten, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten gebaut und dokumentiert habe.",
            "In meinem Hybrid RAG Orchestrator habe ich einen eigenen Decision Making Router auf Basis von Llama 3.1 8b via Groq und LangChain umgesetzt, der Nutzerintent in drei Ausfuehrungspfade klassifiziert, lokale Wissensrecherche, externe Websuche oder direkte konversationelle Logik. Ein zustandsbehafteter MemoryAgent haelt Mehrturn Kontext ueber ChromaDB und HuggingFace Embeddings, und das System laeuft als deployter Streamlit Prototyp end to end. Genau diese Erfahrung mit Agent Definition, Routing, Guardrails und Wissenstransfer bringe ich in Ihre agentischen Workflows ein.",
            "In CreditIQ habe ich eine Fairness by Design Pipeline geliefert, den Disparate Impact von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert. Bei eRay GmbH habe ich sechs Modelle direkt verglichen, strenge Anti Leakage Regeln durchgesetzt und einen Orchestrator mit Gate Checks gebaut, der bei fehlgeschlagener Imputation stoppt statt schlechte Daten weiterfliessen zu lassen. Meine Bachelorarbeit vergleicht sechs Klassifikatoren mit 10 facher Kreuzvalidierung und wurde als IEEE Paper mit ehrlicher Limitations Sektion verfasst.",
            "Ich arbeite sicher in Python, Git und mit API basierten KI Diensten wie OpenAI und Groq, dokumentiere Methoden und Ergebnisse fuer den Wissenstransfer im Team und kann komplexe Problemstellungen strukturiert in Proofs of Concept ueberfuehren. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech mit Ihrem Team in Berlin.",
        ],
    },

    # 2. Fraunhofer-Institut fuer Integrierte Schaltungen IIS — Dresden
    # Praktikant*in / Abschlussarbeit — Simulation und Machine Learning in der Robotik
    # (Xing, 26 July 2026, Master Thesis, DE track)
    {
        "folder": "Fraunhofer IIS Praktikant Abschlussarbeit Simulation ML Robotik Dresden",
        "company": "Fraunhofer-Institut fuer Integrierte Schaltungen IIS",
        "lang": "de",
        "role_strip": "Praktikum und Abschlussarbeit Simulation und Machine Learning in der Robotik",
        "cl_date": "27. Juli 2026",
        "cl_subject": "Praktikum oder Abschlussarbeit Simulation und Machine Learning in der Robotik in Dresden",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Machine Learning Pipelines, Modellvergleich und robuster Bewertung. Ich habe eine rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und asymmetrischen 80 Prozent Vorhersageintervallen bei eRay GmbH geliefert, ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt und einen Hybrid RAG Orchestrator mit agentischem Routing ueber Python und LangChain gebaut. Sicher in Python, scikit learn, CatBoost, LightGBM, XGBoost und PyTorch, mit klarem Blick fuer Simulation, Anti Leakage und ehrliche Modellauswertung.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Stelle als Praktikantin oder Abschlussarbeit im Bereich Simulation und Machine Learning in der Robotik am Fraunhofer-Institut fuer Integrierte Schaltungen IIS in Dresden. Die Ausschreibung, die Programmierung von Roboterarmen und der Einsatz von Machine Learning Modellen in Simulation und auf realer Hardware fuer automatisierte Fertigung unter Unsicherheiten in Lage und Geometrie der Werkstuecke, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline aufgebaut, die vier Wasserqualitaetsindikatoren prognostiziert, und dabei sechs Modelle direkt verglichen. Fuer asymmetrische 80 Prozent Vorhersageintervalle habe ich CatBoost Multi Quantil Regression eingesetzt und strenge Anti Leakage Regeln durchgesetzt, was zu der ehrlichen Erkenntnis gefuehrt hat, welche Indikatoren physikalisch prognostizierbar sind und welche nicht. Diese Herangehensweise, Modell und Realitaet transparent gegeneinander zu halten, ist die gleiche, die auch die Uebertragung vom Simulator auf reale Roboter Hardware traegt.",
            "In CreditIQ habe ich eine Fairness by Design Pipeline geliefert und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, bei stabiler Genauigkeit von 75 Prozent. Meine Echtzeit Flugverfolgungs Pipeline verarbeitet mit PySpark, dbt und Apache Airflow auf Google Cloud ueber 128 tausend Datensaetze aus vier Quellen und aktualisiert sich alle 15 Minuten automatisch. Meine Bachelorarbeit vergleicht sechs Klassifikatoren mit 10 facher Kreuzvalidierung, waehlt ROC AUC statt Genauigkeit auf einem unausgeglichenen Datensatz und wurde als IEEE Paper mit ehrlicher Limitations Sektion verfasst.",
            "Ich arbeite sicher in Python und im wissenschaftlichen Stack aus scikit learn, CatBoost, LightGBM, XGBoost und PyTorch, kann selbststaendig wissenschaftlich arbeiten und dokumentiere jede Entscheidung nachvollziehbar. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 ausgezeichnet. Sehr gerne bespreche ich die konkrete Themenstellung mit Ihrem Team am Standort Dresden in einem persoenlichen Gespraech.",
        ],
    },

    # 3. STIHL — Waiblingen
    # Praktikum Data Analytics und Machine Learning fuer Produktnutzungsdaten
    # (LinkedIn / STIHL careers, 24 July 2026, Mandatory Praktikum, DE track)
    {
        "folder": "STIHL Praktikum Data Analytics ML Produktnutzungsdaten Waiblingen",
        "company": "ANDREAS STIHL AG und Co. KG",
        "lang": "de",
        "role_strip": "Praktikum Data Analytics und Machine Learning fuer Produktnutzungsdaten",
        "cl_date": "27. Juli 2026",
        "cl_subject": "Praktikum Data Analytics und Machine Learning fuer Produktnutzungsdaten in Waiblingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Machine Learning auf realen Sensor und Prozessdaten. Ich habe eine rekursive Zeitreihen Pipeline bei eRay GmbH geliefert, die vier Umweltindikatoren prognostiziert und sechs Modelle direkt vergleicht, eine end to end Batch Pipeline mit BigQuery ML Klassifikator und Bronze Silver Gold Medallion Architektur gebaut und einen Hybrid RAG Orchestrator mit agentischem Routing entwickelt. Sicher in Python, scikit learn, Databricks nahen Tools und AI Agenten, mit klarem Blick fuer Mustererkennung, Klassifikation und statistische Auswertung auf Messdaten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Praktikum Data Analytics und Machine Learning fuer Produktnutzungsdaten bei ANDREAS STIHL AG und Co. KG in Waiblingen, Stellenreferenz 57923. Die Ausschreibung, die Auswertung von Messdaten zur Charakterisierung von Anwendungsprofilen einzelner Maschinen, Maschinengruppen und Flotten sowie die Entwicklung von Machine Learning Modellen fuer Mustererkennung, Klassifikation und statistische Analyse, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline aufgebaut, die vier Wasserqualitaetsindikatoren prognostiziert und sechs Modelle direkt vergleicht, darunter Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet. Fuer asymmetrische Vorhersageintervalle habe ich CatBoost Multi Quantil Regression eingesetzt und strenge Anti Leakage Regeln durchgesetzt, was zu einer ehrlichen Bewertung gefuehrt hat, welche Signale physikalisch prognostizierbar sind. Diese Herangehensweise an rauschbehaftete Sensordaten passt direkt zu STIHL Testdaten aus Geraeten im Feld.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich einen BigQuery ML Klassifikator trainiert, der vor Kinostart vorhersagt, ob ein Film ein Hit wird, mit bewusst getrennten Feature Tabellen fuer eine leakage freie Evaluation. Meine Echtzeit Flugverfolgungs Pipeline sammelt alle 30 Sekunden Live Positionen und reichert diese ueber vier Quellen an, insgesamt ueber 128 tausend Datensaetze. Meinen Hybrid RAG Orchestrator habe ich um eine agentische Routing Schicht ergaenzt, die Antworten je nach Nutzerintent an lokale Vektorsuche, Websuche oder direkte LLM Ausgabe uebergibt, ein Muster, das direkt auf AI Agenten fuer die Analyse von Messdaten uebertragbar ist.",
            "Ich arbeite sicher in Python und mit Machine Learning Bibliotheken wie scikit learn, LightGBM, XGBoost und CatBoost, dokumentiere Analyseansaetze und Ergebnisse fuer eine nachvollziehbare Weiterentwicklung der Datenanalyseprozesse und arbeite gerne im Team. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 ausgezeichnet. Sehr gerne bespreche ich meinen Beitrag in einem persoenlichen Gespraech mit Ihrem Team in Waiblingen.",
        ],
    },

    # 4. YOONA Ventures GmbH — Berlin
    # AI Working Student (Werkstudent) Project-Based
    # (Indeed / yoona.ai career page, 23 July 2026, Werkstudent, EN track)
    {
        "folder": "YOONA Ventures AI Working Student Werkstudent Berlin",
        "company": "YOONA Ventures GmbH",
        "lang": "en",
        "role_strip": "AI Working Student",
        "cl_date": "27 July 2026",
        "cl_subject": "AI Working Student, Werkstudent, in Berlin",
        "profile": "Master student in Data Science and Analytics at SRH Heidelberg based in Mannheim with hands on delivery of generative AI, large language model applications, and computer vision leaning pipelines. I built a Hybrid RAG Orchestrator with agentic routing over Llama 3.1 8b via Groq and LangChain, delivered a fairness by design credit scoring system under the EU AI Act, and ran an end to end recursive time series pipeline at eRay GmbH with strict anti leakage rules. Confident in Python, LangChain, ChromaDB, HuggingFace embeddings, scikit learn, and data scraping with Selenium and BeautifulSoup.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_HADOOP_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the AI Working Student role at YOONA Ventures GmbH in Berlin. The posting, supporting the development and maintenance of generative AI models, building intelligent agent scripts, working on computer vision tasks, and getting hands dirty with data scraping and analysis, maps directly onto the work I have shipped over the last months across large language models, multimodal AI, and real world applications.",
            "In my Hybrid RAG Orchestrator I built a custom decision making router on Llama 3.1 8b via Groq and LangChain that classifies user intent into three execution paths, local knowledge retrieval over PDF and vector data, external web search, or direct conversational logic. A stateful MemoryAgent keeps multi turn context intact over ChromaDB with local persistence and HuggingFace MiniLM L6 v2 embeddings, and the system runs as a deployed Streamlit prototype end to end. This is exactly the kind of intelligent agent script and multimodal AI plumbing you describe.",
            "In CreditIQ I raised the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88 and cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, using AIF360 and SHAP driven subgroup analysis. My Hadoop based crawling platform runs a decoupled Selenium and BeautifulSoup pipeline across dynamic paginated e commerce results, saving raw HTML for safety and decoding sponsored tracking URLs into clean product links before ingesting to HDFS, which mirrors the data scraping and analysis piece of your role. My bachelor thesis compares six classifiers with 10 fold cross validation on a clinical dataset, choosing ROC AUC over accuracy on an imbalanced dataset and writing findings up as an IEEE style paper.",
            "I work confidently in Python and the modern generative AI stack of LangChain, LLM APIs, ChromaDB, and HuggingFace embeddings, and I document methods and results so a small team can extend them. My German level is B1 in progress, my English is fluent, and I am based in Mannheim, available for hybrid work with regular Berlin days. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates, and I was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I would be glad to discuss a concrete first project with your team in a call.",
        ],
    },

    # 5. Deutsche Telekom MMS GmbH — Dresden
    # Werkstudent AI Product Builder / KI-gestuetzte Produktentwicklung (m/w/d)
    # (Indeed, 22 July 2026, Werkstudent, DE track)
    {
        "folder": "Deutsche Telekom MMS Werkstudent AI Product Builder Dresden",
        "company": "Deutsche Telekom MMS GmbH",
        "lang": "de",
        "role_strip": "Werkstudent AI Product Builder und KI gestuetzte Produktentwicklung",
        "cl_date": "27. Juli 2026",
        "cl_subject": "Werkstudent AI Product Builder und KI gestuetzte Produktentwicklung in Dresden",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in KI gestuetzter Produktentwicklung, Retrieval Augmented Generation und cloud nativen Datenprodukten. Ich habe einen Hybrid RAG Orchestrator mit agentischem Routing ueber Llama 3.1 8b via Groq und LangChain gebaut, ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt und eine automatisierte BigQuery Medallion Pipeline mit BigQuery ML Klassifikator und Looker Studio Dashboard geliefert. Sicher in Python, LangChain, ChromaDB, GCP und Streamlit, mit klarem Blick fuer Prototyp, Nutzererfahrung und produktreife Integration.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Stelle als Werkstudent AI Product Builder und KI gestuetzte Produktentwicklung bei der Deutsche Telekom MMS GmbH in Dresden. Die Ausschreibung, die Entwicklung KI gestuetzter Produktideen und deren Ueberfuehrung in nutzbare Prototypen und Produkte, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meinem Hybrid RAG Orchestrator habe ich einen eigenen Decision Making Router auf Basis von Llama 3.1 8b via Groq und LangChain umgesetzt, der Nutzerintent in drei Ausfuehrungspfade klassifiziert. Ein zustandsbehafteter MemoryAgent haelt Mehrturn Kontext ueber ChromaDB und HuggingFace Embeddings, und das System laeuft als deployter Streamlit Prototyp end to end. Genau dieses Muster, eine Idee mit LLM und Vektor Retrieval in ein interaktives Produkt zu ueberfuehren, ist der Kern der AI Product Builder Rolle.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine Bronze Silver Gold Medallion Architektur in BigQuery gebaut, einen BigQuery ML Klassifikator vor Kinostart trainiert und alles per Cloud Scheduler automatisiert, mit einem fuenfseitigen Looker Studio Dashboard fuer konkrete Business Fragen. In CreditIQ habe ich die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, den Disparate Impact von 0,79 auf 0,88 gehoben und ein Streamlit Entscheidungsunterstuetzungs Tool mit LLM Erklaerung ausgeliefert, das Human in the Loop nach EU AI Act Artikel 14 respektiert. Bei eRay GmbH habe ich mit sechs Modellen im Wettbewerb, strengen Anti Leakage Regeln und Gate Checks gezeigt, dass ein KI Produkt nur so gut ist wie seine Bewertung.",
            "Ich arbeite sicher in Python, LangChain, ChromaDB, GCP und Streamlit, kann von einer offenen Produktidee ueber Prototyp bis zur Auslieferung selbststaendig durchgehen und dokumentiere Entscheidungen nachvollziehbar. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 ausgezeichnet. Sehr gerne bespreche ich eine konkrete Produktidee in einem persoenlichen Gespraech mit Ihrem Team in Dresden.",
        ],
    },
]
