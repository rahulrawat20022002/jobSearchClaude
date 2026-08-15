"""Role configurations for the 23 July 2026 run (top 5, backlog soft cap).

Backlog gate: Notion showed 10 drafted rows on 23 July 2026 (matches CSV).
Under the 11 July 2026 backlog gate rule that is an exact 10 soft signal,
so this run is capped at the top 5 newly scored roles instead of the top 10.

Platform quota per 21 July 2026 rule for a top 5 run:
  target: 1 to 2 roles per platform, all four platforms should appear when
  supply allows. This run:
    Xing 1, LinkedIn 4, Indeed 0, StepStone 0, career page counted separate.
  Indeed and StepStone yielded no fresh clean matches this run after
  filtering, and the shortfall redistributed to Xing then LinkedIn per the
  strict priority in the rule. Noted plainly in the digest transparency
  block.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. Mediaplus Muenchen              DE (posting body in German on Xing)
  2. Knauf Deutschland Muenchen      EN (posting body in English on LinkedIn)
  3. Valeo Bietigheim Bissingen      EN (posting body in English on LinkedIn)
  4. Fraunhofer IIS Erlangen         EN (posting title and body in English)
  5. CHECK24 Vergleichsportal Muenchen  EN (posting title in English)

Freshness ordering per 12 July 2026 priority rule:
  1. Valeo               20 July, 3 days ago
  2. Mediaplus           19 July, 4 days ago
  3. Knauf Deutschland   17 July, 6 days ago
  4. CHECK24             16 July, 7 days ago
  5. Fraunhofer IIS      9 July, 14 days ago
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


CONFIGS_23JUL = [
    # 1. Valeo Bietigheim Bissingen — Working Student for Algorithm Research
    # and Development on Radar Systems for Autonomous Driving
    # (LinkedIn, 20 July 2026, Werkstudent, EN)
    {
        "folder": "Valeo Working Student Radar Systems Autonomous Driving",
        "company": "Valeo",
        "lang": "en",
        "role_strip": "Working Student, Radar Systems Algorithm Research and Development",
        "cl_date": "23 July 2026",
        "cl_subject": "Working Student for Algorithm Research and Development on Radar Systems for Autonomous Driving",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on time series signal processing, algorithm evaluation, and rigorous machine learning benchmarking on real sensor data. I have shipped a recursive time series pipeline at eRay GmbH that benchmarked six models head to head on lake sensor data with strict anti leakage rules and asymmetric 80 percent prediction intervals, a fairness by design classification system with SHAP driven subgroup analysis and unit tests at 100 percent branch coverage, and a Random Forest driven study translating raw event data into calibrated business relevant risk signals. Proficient in Python and comfortable in signal oriented data analysis, I am the right fit for radar signal processing algorithm research and machine learning concept evaluation at Valeo.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on Algorithm Research and Development on Radar Systems for Autonomous Driving at Valeo in Bietigheim Bissingen. The brief on developing radar signal processing algorithm modules, researching and testing the developed algorithms, analysing data logs, presenting results, and evaluating machine learning concepts maps directly to the sensor data and algorithm evaluation work I have been shipping over the past year.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen on real lake sensor data, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty. I enforced strict anti leakage rules across the pipeline and surfaced the honest finding that some indicators are physically predictable while others are not without live optical sensors. That is exactly the signal driven, honest algorithm benchmarking mindset a radar systems team needs.",
            "In CreditIQ I built rigorous evaluation harnesses with SHAP driven subgroup analysis and standard metrics including ROC AUC, cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. In my Real Time Flight Tracking Data Pipeline I collected live sensor positions every 30 seconds and enriched them against four data sources, orchestrated with Apache Airflow, refreshing across more than 128 thousand records. That combination of algorithm evaluation and sensor pipeline work is the right base for radar algorithm research.",
            "I am comfortable in Matlab and confident in Python, have a hands on mindset, and speak English fluently with German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I would be glad to align the exact scope with Julia Mittelmaier and the R and D team, and I am open to on site work at Bietigheim Bissingen.",
        ],
    },

    # 2. Mediaplus Muenchen — Werkstudent (all genders) Data Engineering
    # (Xing, 19 July 2026, Werkstudent, DE)
    {
        "folder": "Mediaplus Werkstudent Data Engineering",
        "company": "Mediaplus",
        "lang": "de",
        "role_strip": "Werkstudent Data Engineering",
        "cl_date": "23. Juli 2026",
        "cl_subject": "Werkstudent Data Engineering in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Datenpipelines, Cloud ETL und BI Reporting. Ich habe eine Echtzeit Google Cloud Pipeline betrieben, die alle 30 Sekunden Live Flugpositionen ueber Deutschland gegen Flughafen, Flugzeug und Wetterdaten anreichert und ueber 128 tausend Datensaetze verarbeitet, eine vollstaendig automatisierte BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert und ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt. Sicher in Python, PySpark, SQL, dbt, Apache Airflow und modernen Cloud Umgebungen, bin ich die richtige Verstaerkung fuer das Data und Technology Team bei Mediaplus.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Engineering bei Mediaplus in Muenchen. Die Ausschreibung, die Mitarbeit an smarten Datenloesungen und technologischer Exzellenz in einem dynamischen Data und Technology Team, das mit datengetriebenen Loesungen die Zukunft der Medien und Marketinglandschaft gestaltet, entspricht direkt den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich alle 30 Sekunden Live Positionen von der OpenSky Network API gesammelt und mit PySpark auf Google Cloud gegen vier Quellen aus Flughafen, Flugzeug und Wetterdaten angereichert, ueber 128 tausend Datensaetze sauber verarbeitet und mit dbt in analysebereite Tabellen ueberfuehrt. Apache Airflow orchestriert das Gesamtsystem, so dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. Diese Kombination aus Streaming Ingestion, Cloud ETL und robuster Orchestrierung ist genau die Denke, die ein modernes Media Data Team braucht.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit schemakonformer Datenaufbereitung, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator gebaut, ergaenzt durch ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen zu Genre ROI, Wachstum fremdsprachiger Filme und Release Saison Timing. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und Anti Leakage Regeln geliefert. Das ist die ETL und Reporting Grundlage, die Media Data Mesh und Media Planning brauchen.",
            "Ich arbeite sicher in Python, PySpark, SQL, dbt, Airflow und BI Werkzeugen, kenne Cloud Umgebungen wie GCP und AWS und spreche Deutsch aktuell B1 in Bearbeitung, Englisch fliessend. Ich bringe die Zertifikate AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics und Google Data Analytics Foundations mit. Sehr gerne unterstuetze ich Ihr Team ab sofort und stelle mich in einem persoenlichen Gespraech vor.",
        ],
    },

    # 3. Knauf Deutschland Muenchen — Working Student AI Training and Enablement
    # (LinkedIn, 17 July 2026, Werkstudent, EN)
    {
        "folder": "Knauf Deutschland Working Student AI Training Enablement",
        "company": "Knauf Deutschland",
        "lang": "en",
        "role_strip": "Working Student, AI Training and Enablement",
        "cl_date": "23 July 2026",
        "cl_subject": "Working Student AI Training and Enablement",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on generative AI system building, EU AI Act aware model design, and clear communication of complex technical topics to non technical audiences. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain, a fairness by design credit scoring system documented against EU AI Act and GDPR with a plain language LLM generated explanation for finance managers, and a Random Forest driven climate risk study translated into visual reports for non technical stakeholders. Fluent in English and confident in PowerPoint and design tools, I am the right fit for building AI literacy content and rolling out training at Knauf Digital.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on AI Training and Enablement at Knauf Digital in Munich. The brief on creating engaging training content for AI concepts, developing the AI literacy curriculum from generative AI basics to responsible use, translating EU AI Act literacy requirements into clear learning content, and rolling out courses through the LMS aligns directly with the applied AI and communication work I have been shipping over the past year.",
            "My Hybrid RAG Orchestrator is a working generative AI system that classifies user intent into three execution paths, local knowledge retrieval, external web search, and direct conversational logic, built on Llama 3.1 8b via Groq, LangChain orchestration, HuggingFace MiniLM L6 v2 embeddings, and a persistent ChromaDB vector store, shipped as a Streamlit interface. It gives me the concrete grounding to explain generative AI basics, RAG, embeddings, and internal LLM tools like KARL to a non technical audience without hand waving.",
            "In CreditIQ I lifted the Disparate Impact ratio from a failing 0.79 to a compliant 0.88 against the EU AI Act and AGG 80 percent fairness threshold, diagnosed a hidden intersectional bias through SHAP driven subgroup analysis, and shipped a Streamlit decision support tool with a plain language LLM generated explanation for finance managers, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14. That means I can translate EU AI Act literacy requirements into concrete, honest examples that non technical audiences actually understand.",
            "I am fluent in English, structured, independent, and detail oriented, and I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I am confident in PowerPoint, comfortable with design and video tools, and quick to pick up LMS platforms like Docebo. I would be glad to align the exact scope with the AI Training and Enablement team at Knauf Digital and start soon.",
        ],
    },

    # 4. CHECK24 Vergleichsportal Muenchen — Working Student Data Science
    # Computer Vision / IdentityCheck (LinkedIn, 16 July 2026, Werkstudent, EN)
    {
        "folder": "CHECK24 Vergleichsportal Working Student Data Science Computer Vision IdentityCheck",
        "company": "CHECK24 Vergleichsportal GmbH",
        "lang": "en",
        "role_strip": "Working Student, Data Science and Computer Vision",
        "cl_date": "23 July 2026",
        "cl_subject": "Working Student Data Science Computer Vision IdentityCheck",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning benchmarking, honest evaluation on imbalanced datasets, and end to end ML delivery on real data. I have shipped a fairness by design classification system with SHAP driven subgroup analysis, unit tests at 100 percent branch coverage, and rigorous EU AI Act aligned evaluation, a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain, and a bachelor thesis benchmarking six classifiers on a real clinical dataset with 10 fold cross validation and ROC AUC as the honest headline metric for an imbalanced target. Proficient in Python, scikit learn, and standard ML frameworks, I am the right fit for a Working Student position on Data Science and Computer Vision in the IdentityCheck team at CHECK24.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_SAS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on Data Science and Computer Vision in the IdentityCheck team at CHECK24 Vergleichsportal in Munich. The brief on building data driven identity verification with machine learning and computer vision maps directly to the honest ML evaluation and end to end delivery work I have been shipping over the past year.",
            "In CreditIQ I built a full end to end classification system with rigorous SHAP driven subgroup analysis, lifted the Disparate Impact ratio from a failing 0.79 to a compliant 0.88 against the EU AI Act and AGG 80 percent threshold, cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. That mindset, treating identity related classifications as high stakes decisions that require honest evaluation and defensible trade offs, transfers directly to IdentityCheck work.",
            "My Diabetes Prediction bachelor thesis benchmarked six classifiers on a real clinical dataset with 10 fold cross validation, caught biologically impossible zero values the original authors had overlooked, applied IQR based outlier removal and proper imputation, and picked ROC AUC over accuracy for a 65 to 35 imbalanced dataset. My Hybrid RAG Orchestrator adds hands on generative AI experience with a custom decision making router on Llama 3.1 8b via Groq, LangChain orchestration, and a ChromaDB vector store. That is the right blend of classical ML rigour and modern AI systems for CHECK24 IdentityCheck.",
            "I am proficient in Python, scikit learn, and standard ML frameworks, comfortable with computer vision fundamentals, and I speak English fluently with German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and SAS Certified Specialist Visual Business Analytics certificates. I would be glad to align the exact scope with the IdentityCheck team and start soon at 20 hours per week.",
        ],
    },

    # 5. Fraunhofer IIS Erlangen — Working Student Machine Learning for Audio
    # Compression (all genders) (LinkedIn plus career page, 9 July 2026,
    # Werkstudent, EN)
    {
        "folder": "Fraunhofer IIS Working Student Machine Learning Audio Compression",
        "company": "Fraunhofer-Institut fuer Integrierte Schaltungen IIS",
        "lang": "en",
        "role_strip": "Working Student, Machine Learning for Audio Compression",
        "cl_date": "23 July 2026",
        "cl_subject": "Working Student Machine Learning for Audio Compression",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on deep learning framework work, rigorous machine learning benchmarking on real signal data, and end to end ML delivery. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain, HuggingFace MiniLM L6 v2 embeddings, and a persistent ChromaDB vector store, a recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules and asymmetric prediction intervals, and a fairness by design classification system with SHAP driven analysis and unit tests at 100 percent branch coverage. Proficient in Python and comfortable with deep learning frameworks, I am the right fit for a Working Student position on Machine Learning for Audio Compression at Fraunhofer IIS.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_SAS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on Machine Learning for Audio Compression at Fraunhofer IIS in Erlangen. The brief on applied machine learning research inside a leading audio and multimedia institute aligns directly with the deep learning framework work, rigorous ML benchmarking, and end to end delivery I have been shipping over the past year.",
            "My Hybrid RAG Orchestrator is a working deep learning system that classifies user intent into three execution paths, built on Llama 3.1 8b via Groq, LangChain orchestration, HuggingFace MiniLM L6 v2 embeddings, and a persistent ChromaDB vector store, shipped as a Streamlit interface with end to end ownership. That gives me concrete hands on experience with modern neural architectures, embeddings, and inference tooling, which is directly transferable to audio embedding and neural codec research.",
            "At eRay GmbH I built an end to end recursive time series pipeline benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, using CatBoost multi quantile regression for asymmetric 80 percent prediction intervals and enforcing strict anti leakage rules. In CreditIQ I built a full evaluation harness with SHAP driven analysis, cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. My Diabetes Prediction bachelor thesis benchmarked six classifiers with 10 fold cross validation and picked ROC AUC over accuracy for an imbalanced dataset. That is the honest, leakage aware evaluation discipline audio compression research needs.",
            "I am proficient in Python and comfortable with deep learning frameworks like PyTorch, familiar with signal oriented data, and fluent in English with German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and SAS Certified Specialist Visual Business Analytics certificates. I would be glad to align the exact scope with the Audio Coding for Communication team and start on the schedule that fits Fraunhofer IIS.",
        ],
    },
]
