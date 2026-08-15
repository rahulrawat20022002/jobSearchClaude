"""Role configurations for the 18 July 2026 run (top 10).

Imports base project bank and building blocks from role_configs.py.
The main role_configs.CONFIGS pointer aliases this module's CONFIGS_18JUL.
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
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_18JUL = [
    # 1. CeramTec — Werkstudent Digitale Transformation Data Analytics Application (Plochingen)
    {
        "folder": "CeramTec Werkstudent Data Analytics Application",
        "company": "CeramTec GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Data Analytics Application",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Digitale Transformation, Data Analytics Application in Plochingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Data Analytics, Dashboarding und Cloud Pipelines auf produktionsnahen Daten. Ich habe eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerter Analytik umgesetzt und eine Random Forest gestützte Business Intelligence Studie zu wirtschaftlichen Auswirkungen globaler Klimaereignisse veröffentlicht. Sicher in Python, SQL, Dashboarding Tools und klarer Stakeholder Kommunikation, bin ich die richtige Verstärkung für die digitale Transformation im Bereich Data Analytics Application bei CeramTec in Plochingen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Digitale Transformation, Data Analytics Application am Standort Plochingen. Die Ausschreibung, Unterstützung bei Rollout und kontinuierlicher Verbesserung von Data Analytics Anwendungen, Übersetzung von Business KPIs in strukturierte Reports und Dashboards sowie enge Abstimmung mit IT und Fachbereichen für datengetriebene Entscheidungen, deckt sich genau mit dem, was ich im letzten Jahr in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator umgesetzt, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. In meinem Fast Food Nährwert Analyzer und Meal Simulator habe ich ein zweistufiges Tableau Dashboard gebaut, eine Executive Makro Sicht kombiniert mit einer granularen Detail Sicht, mit Set Actions und parameter gesteuerten Feldern, so dass Nicht Techniker die Daten selbst explorieren können. Beides spiegelt genau die business nahe Analytik wider, die CeramTec skaliert.",
            "In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt und die Ergebnisse in visuellen Reports kommuniziert, die auch ein nicht technisches Publikum direkt umsetzen kann. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit strengen Anti Leakage Regeln und einem Orchestrator mit Gate Checks geliefert, was den Blick für verlässliche Analytik auf unsauberen Rohdaten schärft.",
            "Zur Sprache: mein aktuelles Deutschniveau ist B1 in Bearbeitung, ich arbeite aktiv weiter daran, in Python und SQL bin ich sicher und ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations und AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr Team ab der ersten Woche bei Dashboard Rollouts, KPI Definitionen und Dokumentation.",
        ],
    },

    # 2. CeramTec — Werkstudent Digitale Transformation Computer Vision (Plochingen)
    {
        "folder": "CeramTec Werkstudent Computer Vision",
        "company": "CeramTec GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Computer Vision",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Digitale Transformation, Computer Vision in Plochingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning und bildnaher Datenpipeline Arbeit, von LLM Systemen über Echtzeit Anreicherung bis hin zu strenger Modellbewertung. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Entscheidungs Router auf Llama 3.1 8b via Groq und HuggingFace MiniLM L6 v2 Embeddings geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act umgesetzt und eine Echtzeit Pipeline auf Google Cloud betrieben, die Flugpositionen alle 30 Sekunden gegen vier Datenquellen anreichert. Sicher in Python, PyTorch nahen Workflows, scikit learn und strukturierter Evaluation, bin ich die richtige Verstärkung für die Computer Vision Projekte bei CeramTec in Plochingen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Digitale Transformation, Computer Vision am Standort Plochingen. Die Ausschreibung, Unterstützung von Computer Vision Anwendungsfällen in Produktions und Qualitätsprozessen, Prototyping von Modellen sowie Zusammenarbeit mit IT und Engineering, um Vision gestützte Analytik in den Alltag zu bringen, passt direkt zu dem, was ich in den letzten Monaten gebaut habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore mit lokaler Persistenz. Das gibt mir ein starkes Gefühl für Modellintegration und Embeddings, die auch in Computer Vision Pipelines tragend sind. In CreditIQ habe ich eine strenge Machine Learning Evaluation aufgesetzt, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, die Genauigkeit stabil bei 75 Prozent gehalten und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet, alle 30 Sekunden Positionen gegen Flughafen, Flugzeug und Wetterdaten angereichert und das Ganze mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten aktualisieren. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit Anti Leakage Regeln und Quantil Regression Vorhersageintervallen umgesetzt, das zeigt, dass ich strukturierte und ehrliche ML Arbeit auf realen Daten liefere.",
            "Ich bin sicher in Python, arbeite komfortabel in PyTorch nahen Workflows und scikit learn und bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering sowie AWS Academy Cloud Foundations mit. Mein Deutschniveau ist B1 in Bearbeitung. Sehr gerne starte ich zeitnah und unterstütze Ihr Computer Vision Team bei Prototypen und Rollout Arbeit.",
        ],
    },

    # 3. Dräger — Praktikum / Abschlussarbeit CV/ML (Lübeck) — Master Thesis track
    {
        "folder": "Draeger Abschlussarbeit Computer Vision ML",
        "company": "Draeger",
        "lang": "de",
        "role_strip": "Masterarbeit Student",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Abschlussarbeit, Software Programmierung Computer Vision und Machine Learning in Lübeck",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning und vision naher Pipeline Arbeit, von LLM Systemen über strenge Klassifikator Evaluation bis hin zu realer Zeitreihen Prognose. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Entscheidungs Router auf Llama 3.1 8b via Groq geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act und DSGVO umgesetzt und bei eRay GmbH eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren mit Anti Leakage Garantien betrieben. Sicher in Python, PyTorch nahen Workflows und wissenschaftlicher Evaluation, bin ich die richtige Verstärkung für eine Masterarbeit im Bereich Software Programmierung, Computer Vision und Machine Learning bei Draeger.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für ein Praktikum oder eine Abschlussarbeit im Bereich Technology Development mit Schwerpunkt auf Software Programmierung, Computer Vision und Machine Learning bei Draeger in Lübeck. Die Ausschreibung, Mitarbeit an Forschung und Entwicklung rund um Machine Vision und Machine Learning Software Komponenten in einem medizin und sicherheitskritischen Umfeld, deckt sich stark mit dem, was ich in diesem Jahr in der Praxis geliefert habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ChromaDB Vektor Persistenz und HuggingFace MiniLM L6 v2 Embeddings. Der end to end Aufbau hat mich in Foundation Model Integration, Prompt Engineering und iteratives Debugging eines ML Systems geführt. In CreditIQ habe ich eine strenge ML Evaluation aufgesetzt, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, die Genauigkeit stabil bei 75 Prozent gehalten und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage sowie einer vollständigen regulatorischen Dokumentation abgesichert, dieses Denken überträgt sich direkt auf Draegers sicherheitskritische Domäne.",
            "Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline zur Prognose von vier Wasserqualitätsindikatoren für einen deutschen See aufgebaut, sechs Modelle direkt verglichen, strenge Anti Leakage Regeln erzwungen und ehrlich berichtet, was die Daten hergeben und was nicht. In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet und Positionen alle 30 Sekunden gegen vier Quellen angereichert. Zusammen zeigen sie, dass ich mich in unsaubere Daten einarbeite, Modelle ehrlich benchmarke und verlässliche Pipelines unter realen Randbedingungen liefere.",
            "Ich bin sicher in Python, komfortabel in PyTorch nahen Workflows und bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering sowie AWS Academy Cloud Foundations mit. Mein Deutschniveau ist B1 in Bearbeitung. Sehr gerne stimme ich den konkreten Thesis Rahmen mit meiner SRH Professorin oder meinem SRH Professor ab und richte den Computer Vision Anwendungsfall mit Ihrem Technology Development Team gemeinsam aus.",
        ],
    },

    # 4. ATRIVIO — Bachelor / Masterarbeit (Kempten Allgäu) — send-time optimization for mail2many
    {
        "folder": "ATRIVIO Masterarbeit",
        "company": "ATRIVIO GmbH",
        "lang": "de",
        "role_strip": "Masterarbeit Student",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Masterarbeit, KI gestützte Zeitpunktoptimierung für mail2many bei ATRIVIO",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning, LLM Systemen und Datenpipelines auf realen Nutzerdaten. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Decision Making Router auf Llama 3.1 8b via Groq geliefert, eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit BigQuery ML Klassifikator umgesetzt und bei eRay GmbH eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren mit strengen Anti Leakage Regeln betrieben. Sicher in Python, pandas, scikit learn, SQL, statistischer Evaluation und A/B nahen Testdesigns, bin ich die richtige Verstärkung für eine Masterarbeit zur KI gestützten Zeitpunktoptimierung im mail2many System von ATRIVIO.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für die Masterarbeit bei ATRIVIO in Kempten mit dem Ziel, mithilfe von KI Methoden einen empfängerindividuellen optimalen Versandzeitpunkt für mail2many Kampagnen zu bestimmen und dessen Wirkung auf Öffnungs und Klickraten belastbar zu messen. Die Ausschreibung deckt sich sehr genau mit meinem Profil, historische Versand und Interaktionsdaten auszuwerten, Muster im Nutzerverhalten zu identifizieren, ein Modell zur Vorhersage des optimalen Zeitpunkts zu bauen und ein A/B basiertes Selbstlernverfahren zur kontinuierlichen Verbesserung zu entwerfen.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline aufgebaut, sechs Modelle direkt verglichen, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und mit CatBoost Multi Quantil Regression asymmetrische 80 Prozent Vorhersageintervalle für Entscheidungen unter Unsicherheit geliefert. Ich habe strenge Anti Leakage Regeln erzwungen, fehlende Winter Messwerte mit MICE Imputation rekonstruiert und die Pipeline in einen Orchestrator mit Gate Checks eingebettet. Genau diese Disziplin trage ich in die Modellierung individueller Versandfenster hinein, damit die Optimierung nicht am Kaltstart Problem oder an verzerrten Zeitstempeln scheitert.",
            "In CreditIQ habe ich eine strenge statistische Evaluation aufgesetzt, SHAP getriebene Subgruppenanalyse gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert, inklusive DSGVO Diskussion und Human in the Loop Argumentation. Das entspricht direkt Ihrem Punkt zu KPI Definition, statistisch belastbarem Nachweis und Datenschutzanforderungen. In meinem Hybriden RAG Orchestrator habe ich mit Llama 3.1 8b via Groq, LangChain und einem eigenen Router iteratives Debugging und Feedback getriebene Verbesserung eines ML Systems durchgezogen, das Denkmuster überträgt sich auf ein A/B basiertes Selbstlernverfahren.",
            "Ich bin sicher in Python inklusive pandas, scikit learn und PyTorch nahen Workflows, komfortabel in SQL und JavaScript nahen Sprachen und bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations sowie Google Data Analytics Foundations mit. Mein Deutschniveau ist B1 in Bearbeitung Richtung B2. Sehr gerne stimme ich den Rahmen der Arbeit mit Ihrem Team und meiner SRH Professorin oder meinem SRH Professor ab und arbeite von Mannheim aus überwiegend remote mit regelmäßigen Präsenztagen in Kempten.",
        ],
    },

    # 5. RSG Group — Werkstudent:in Data & Analytics 20h/Woche (Berlin)
    {
        "folder": "RSG Group Werkstudent Data Analytics",
        "company": "RSG Group GmbH",
        "lang": "en",
        "role_strip": "Data and Analytics Werkstudent",
        "cl_date": "18 July 2026",
        "cl_subject": "Working Student, Data and Analytics 20 hours per week",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on analytics, dashboarding, and cloud pipeline work on real business data. I have shipped a fully automated Bronze to Silver to Gold BigQuery medallion pipeline with a BigQuery ML classifier and a five page Looker Studio dashboard, an interactive Tableau dashboard with dynamic Set Actions and parameter driven analytics, and a Random Forest driven business intelligence study on the economic impact of global events. Comfortable in Python, SQL, dashboarding, and clear reporting, I am the right fit for a 20 hour Werkstudent Data and Analytics role at the RSG Group head office in Berlin.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_MOVIE_EN, P_TABLEAU_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_SAS, CERT_GOOGLE, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Werkstudent:in Data and Analytics role at RSG Group head office in Berlin, 20 hours per week. The brief on supporting business decision making through data analytics, building and maintaining dashboards, structuring reports for different stakeholders, and iterating pragmatically with the business teams matches exactly the work I have been shipping.",
            "In my Movie Analytics and ML Pipeline on GCP I built an end to end Bronze to Silver to Gold BigQuery medallion architecture with schema enforcement, deduplication via window functions, and a leakage free BigQuery ML classifier, then delivered a five page Looker Studio dashboard for concrete business questions like ROI by category and season timing. In my Fast Food Nutritional Analyzer and Meal Simulator I built an interactive two tier Tableau dashboard with dynamic Set Actions and parameter driven analytics, designed for non technical users to explore data directly.",
            "In my Economic Impact Analysis of Global Climate Events I translated raw event data into structured Business Intelligence with Random Forest models and statistical modelling, communicated in visual reports for non technical stakeholders. At eRay GmbH I delivered a recursive time series pipeline with strict anti leakage rules, which is the same discipline needed to keep sales and operations dashboards trustworthy over time.",
            "I am fluent in English, comfortable in Python and SQL, my current German level is B1 in progress, and I hold the SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations, and AWS Academy Cloud Foundations certificates. I would be glad to work 20 hours per week and support your team from the head office in Berlin.",
        ],
    },

    # 6. SAP — Master Thesis Student Supply Chain Management Data Science on Agentic AI (Garching)
    {
        "folder": "SAP Master Thesis SCM Data Science Agentic AI",
        "company": "SAP",
        "lang": "en",
        "role_strip": "Master Thesis Student",
        "cl_date": "18 July 2026",
        "cl_subject": "Master Thesis, Supply Chain Management Data Science on Agentic AI",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning, generative AI, and cloud pipeline work built around LLMs, decision agents, and rigorous evaluation. I have shipped a modular Retrieval Augmented Generation system with a custom decision making agentic router on Llama 3.1 8b via Groq, a fairness by design classification system covering EU AI Act and GDPR, and a fully automated BigQuery medallion pipeline with a leakage free BigQuery ML classifier. Comfortable in Python, LangChain, embeddings, and structured evaluation, I am the right fit for a Master Thesis in Supply Chain Management Data Science on Agentic AI at SAP.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_SAS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis Student role in Supply Chain Management Data Science on Agentic AI with SAP in Garching bei Muenchen. The brief on researching and prototyping agentic AI approaches for Supply Chain use cases, combining data science with LLM based agents, and evaluating the trade offs between existing tools and custom pipelines maps directly to how I already build.",
            "My Hybrid RAG Orchestrator is a working agentic AI system with a custom decision making router that classifies user intent into three execution paths, local knowledge retrieval, external web search, or direct conversational logic, using Llama 3.1 8b via Groq for inference and LangChain for orchestration. It uses ChromaDB with local persistence and HuggingFace MiniLM L6 v2 embeddings for semantic retrieval, and a stateful MemoryAgent for multi turn coherence, exactly the shape of agent design SAP is exploring for SCM.",
            "In my Movie Analytics and ML Pipeline on GCP I built a Bronze to Silver to Gold BigQuery medallion architecture with a leakage free BigQuery ML classifier and a five page Looker Studio dashboard. In CreditIQ I lifted the Disparate Impact ratio from 0.79 to 0.88 with rigorous evaluation and backed the pipeline with unit tests at 100 percent branch coverage. That combination of solid data engineering and honest evaluation carries directly into Supply Chain forecasting and agentic decision support.",
            "I am proficient in Python and SQL, comfortable with LLM tooling and cloud environments, and hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and SAS Certified Specialist Visual Business Analytics certificates. I would be glad to shape the thesis with my SRH professor and align on the Supply Chain scope with your Garching team.",
        ],
    },

    # 7. MVV Energie — Werkstudent Digital Empowerment GenAI and Analytics (Mannheim)
    {
        "folder": "MVV Energie Werkstudent GenAI Analytics",
        "company": "MVV Energie",
        "lang": "de",
        "role_strip": "Werkstudent GenAI und Analytics",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Digital Empowerment, GenAI und Analytics in Mannheim",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Generative AI und Analytics, von LLM Systemen über Cloud Pipelines bis hin zu business nahen Dashboards. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Entscheidungs Router auf Llama 3.1 8b via Groq geliefert, eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit BigQuery ML Klassifikator und fünfseitigem Looker Studio Dashboard umgesetzt sowie ein Fairness by Design Klassifikationssystem nach EU AI Act und DSGVO gebaut. Sicher in Python, SQL, LLM Tooling und klarer Stakeholder Kommunikation, bin ich die richtige Verstärkung für MVVs Digital Empowerment Initiativen in GenAI und Analytics am Standort Mannheim.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Digital Empowerment, Digital Initiatives GenAI und Analytics bei MVV Energie in Mannheim. Ich lebe selbst in Mannheim und freue mich über die lokale Nähe. Die Ausschreibung, Unterstützung von GenAI und Analytics Initiativen, Übersetzung von Business Fragen in konkrete Daten oder LLM Anwendungsfälle sowie Begleitung der Teams bei der Adoption neuer KI Werkzeuge, deckt sich genau mit dem, was ich in diesem Jahr gebaut habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges Generative AI System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausführungspfade klassifiziert, lokale Wissensrecherche, externe Websuche oder direkte konversationelle Logik, umgesetzt mit Llama 3.1 8b via Groq und LangChain. Der Aufbau hat mich in Prompt Engineering, Embeddings und iteratives Debugging einer LLM Pipeline geführt, und genau dieses Denken skaliert MVV in seine digitalen Initiativen hinein.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement und Deduplikation per Window Functions gebaut und ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen ausgeliefert. In CreditIQ habe ich ein Entscheidungsunterstützungs UI mit einer in einfacher Sprache generierten LLM Erklärung für jede Empfehlung entworfen, das trifft direkt Ihr Interesse, KI in Geschäftsprozesse einzubetten.",
            "Ich bin sicher in Python und SQL, mein Deutschniveau ist B1 in Bearbeitung, und ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, Google Data Analytics Foundations und AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr Team lokal in Mannheim und die Digital Empowerment Initiativen ab der ersten Woche.",
        ],
    },

    # 8. Debeka — Werkstudent Data Intelligence Center DWH/BI (Koblenz)
    {
        "folder": "Debeka Werkstudent Data Intelligence Center DWH BI",
        "company": "Debeka",
        "lang": "de",
        "role_strip": "Werkstudent Data Intelligence Center",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Data Intelligence Center, DWH und BI in Koblenz",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Data Warehouse, BI und Cloud Analytics auf produktionsnahen Daten. Ich habe eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit BigQuery ML Klassifikator und fünfseitigem Looker Studio Dashboard geliefert, eine PySpark und dbt gestützte Echtzeit Flugverfolgungs Pipeline auf Google Cloud betrieben und ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerter Analytik umgesetzt. Sicher in SQL, Python, dbt und Dashboarding Tools, bin ich die richtige Verstärkung für das Data Intelligence Center von Debeka in Koblenz.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_FLIGHT_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent im Data Intelligence Center mit Schwerpunkt DWH und BI bei der Debeka in Koblenz. Die Ausschreibung, Unterstützung der Data Warehouse und Business Intelligence Schicht, Aufbau und Pflege von Reports und Dashboards sowie enge Zusammenarbeit mit den Fachbereichen für strukturierte Analytik, deckt sich genau mit dem, was ich im letzten Jahr geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine end to end Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement, sicherem Type Casting, Deduplikation per Window Functions und Genre Normalisierung in ein relationales Modell umgesetzt und ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen geliefert. In meiner Echtzeit Flugverfolgungs Pipeline habe ich eine PySpark und dbt Pipeline auf Google Cloud betrieben, orchestriert mit Apache Airflow und automatischer Aktualisierung alle 15 Minuten, das ist genau die DWH Refresh und Modellierungs Disziplin, mit der Ihr Team arbeitet.",
            "In meinem Fast Food Nährwert Analyzer und Meal Simulator habe ich ein zweistufiges Tableau Dashboard gebaut, mit Executive Makro Sicht und granularer Detail Sicht, mit Set Actions und parameter gesteuerten Feldern für nicht technische Stakeholder. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit strengen Anti Leakage Regeln und Gate Checks umgesetzt, was den Blick für verlässliche Analytik auf unsauberen Rohdaten schärft.",
            "Ich bin sicher in SQL, Python und dbt, mein Deutschniveau ist B1 in Bearbeitung, und ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations und AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr Data Intelligence Center bei DWH und BI Rollouts ab der ersten Woche.",
        ],
    },

    # 9. 1KOMMA5 — Werkstudent Quality Control Analyst Waermepumpe (Home Office)
    {
        "folder": "1KOMMA5 Werkstudent Quality Control Analyst Waermepumpe",
        "company": "1KOMMA5",
        "lang": "de",
        "role_strip": "Werkstudent Quality Control Analyst",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Quality Control Analyst Wärmepumpe, Home Office",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Qualitätsanalytik und Zeitreihen Datenarbeit, von rekursiver Prognose über Echtzeit Anreicherung bis hin zu Business Intelligence. Ich habe bei eRay GmbH eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren mit Anti Leakage Garantien geliefert, eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard umgesetzt und eine Random Forest gestützte Studie zur Übersetzung roher Ereignisdaten in strukturierte Business Insights veröffentlicht. Sicher in Python, SQL und diszipliniertem Datenqualitätsdenken, bin ich die richtige Verstärkung für eine Werkstudentenrolle als Quality Control Analyst mit Fokus auf Wärmepumpen Flottendaten bei 1KOMMA5.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_CLIMATE_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_GOOGLE_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Quality Control Analyst mit Fokus auf Wärmepumpen Daten bei 1KOMMA5, aus dem Home Office. Die Ausschreibung, Analyse von Flotten und Installationsdaten, frühes Erkennen von Qualitätsproblemen und Übersetzung der Ergebnisse in klare Reports für Operations und Produkt Teams, passt direkt zu dem, was ich in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See aufgebaut, sechs Modelle direkt verglichen und CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle genutzt. Ich habe strenge Anti Leakage Regeln erzwungen, fehlende Winter Messwerte mit MICE Imputation rekonstruiert und die gesamte Pipeline in einen Orchestrator mit Gate Checks und ökologischen Grenzen eingebettet. Genau diese Disziplin braucht man, um Qualitätssignale von Wärmepumpen über Zeit vertrauenswürdig zu halten.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine end to end Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement und Deduplikation per Window Functions gebaut, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest Modellen rohe Ereignisdaten in klare, business relevante Signale zu Dauer und Schwere übersetzt und die Ergebnisse in Reports kommuniziert, mit denen nicht technische Stakeholder direkt arbeiten können.",
            "Ich bin sicher in Python und SQL, mein Deutschniveau ist B1 in Bearbeitung, und ich bringe die Zertifikate Google Data Analytics Foundations, AWS Academy Cloud Foundations sowie SAS Certified Specialist Visual Business Analytics mit. Sehr gerne arbeite ich vollständig remote aus Mannheim und unterstütze Ihr Quality Control Team ab der ersten Woche.",
        ],
    },

    # 10. JOST-Werke — Werkstudent Industrial AI & Process Innovation (Neu-Isenburg)
    {
        "folder": "JOST-Werke Werkstudent Industrial AI",
        "company": "JOST-Werke Deutschland GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Industrial AI und Process Innovation",
        "cl_date": "18. Juli 2026",
        "cl_subject": "Werkstudent Industrial AI und Process Innovation in Neu-Isenburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning, LLM Systemen und Cloud Pipelines auf realen industrienahen Daten. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Entscheidungs Router auf Llama 3.1 8b via Groq geliefert, eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit BigQuery ML Klassifikator gebaut und ein Fairness by Design Klassifikationssystem mit strenger Evaluation und Unit Tests bei 100 Prozent Branch Coverage abgesichert. Sicher in Python, SQL, LLM Tooling und prozessorientiertem Denken, bin ich die richtige Verstärkung für eine Werkstudentenrolle Industrial AI und Process Innovation bei JOST-Werke.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Industrial AI und Process Innovation bei JOST-Werke in Neu-Isenburg. Die Ausschreibung, Unterstützung von KI Anwendungsfällen in industriellen Prozessen, Prototyping von Modellen und kleinen Werkzeugen sowie Begleitung der Fachbereiche bei der Adoption von KI im Tagesgeschäft, deckt sich direkt mit dem, was ich in diesem Jahr gebaut habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um einen ChromaDB Vektorstore und einen zustandsbehafteten MemoryAgent. Der end to end Aufbau hat mich in Foundation Model Integration und Prompt Engineering geführt, und genau diese Form der Prozessautomatisierung wollen Sie in industrielle Workflows tragen. In CreditIQ habe ich eine strenge ML Evaluation über verschiedene Klassifikatoren aufgesetzt, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine automatisierte Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement und Deduplikation per Window Functions gebaut, abgesichert mit einem Least Privilege Service Account und Secret Manager, und ein fünfseitiges Looker Studio Dashboard für Entscheider ausgeliefert. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit strengen Anti Leakage Regeln und Gate Checks umgesetzt, dieses Denken lässt sich direkt auf industrielle Daten und Prozessinnovation übertragen.",
            "Ich bin sicher in Python und SQL, mein Deutschniveau ist B1 in Bearbeitung, und ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations sowie Google Data Analytics Foundations mit. Sehr gerne unterstütze ich Ihr Team Industrial AI und Process Innovation bei Prototypen und Rollout Arbeit.",
        ],
    },
]
