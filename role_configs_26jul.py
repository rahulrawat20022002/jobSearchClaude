"""Role configurations for the 26 July 2026 job search run (top 10).

Backlog gate: Notion showed 0 drafted rows on 26 July 2026 (all previously
drafted rows have been flipped to applied, rejected, shortlisted, or Not
listed Anymore). CSV also synced to Notion in the reconciliation step at
the start of this run, so 15 stale drafted rows in the CSV were flipped
to their true Notion status. Under 10 drafted rows means the normal top 10
cut applies per the 11 July 2026 rule.

Platform quota per 21 July 2026 rule for a top 10 run:
  target: 2 to 3 roles per platform, all four platforms should appear.
  This run:
    Indeed 2, StepStone 3, Xing 2, LinkedIn 3, career page counted separate.

Language track per role, per the 20 July 2026 language match hard rule
(posting body language IS the deliverable language):
  1. Freudenberg Weinheim         DE (posting body in German on StepStone)
  2. Airbus Hamburg               EN (posting body in English on Workday)
  3. TK Elevator Duesseldorf      EN (posting body in English on TK career page)
  4. ROSEN Group Lingen           DE (posting body in German on Xing)
  5. Siemens Healthineers Forchheim  EN (posting body in English on LinkedIn)
  6. Avelios Medical Muenchen     EN (posting body in English on LinkedIn)
  7. SAP Garching bei Muenchen    EN (posting body in English on SAP career page)
  8. 1&1 Mobilfunk Duesseldorf    DE (posting body in German on StepStone/Xing)
  9. PMMG Group Muenchen          DE (posting body in German on Indeed)
 10. GEA Hilge Bodenheim          DE (posting body in German on Indeed)

Freshness ordering per 12 July 2026 priority rule
(freshness first, then role type Master Thesis > Werkstudent > Praktikum,
then Best for overlap, all within the single Germany tier):
  1. Freudenberg          24 July, 2 days ago, Master Thesis
  2. Airbus Hamburg       23 July, 3 days ago, Master Thesis
  3. TK Elevator          23 July, 3 days ago, Werkstudent
  4. ROSEN Group          22 July, 4 days ago, Master Thesis
  5. Siemens Healthineers 22 July, 4 days ago, Werkstudent
  6. Avelios Medical      22 July, 4 days ago, Werkstudent
  7. SAP                  22 July, 4 days ago, Werkstudent
  8. 1&1 Mobilfunk        20 July, 6 days ago, Werkstudent
  9. PMMG Group           mid July, Werkstudent
 10. GEA Hilge            mid July, Werkstudent
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


CONFIGS_26JUL = [
    # 1. Freudenberg Technology Innovation SE & Co. KG — Weinheim
    # Masterarbeit im Bereich Data Science / Machine Learning im Spritzguss
    # (StepStone, 24 July 2026, Master Thesis, DE track)
    {
        "folder": "Freudenberg Masterarbeit Data Science Machine Learning Spritzguss",
        "company": "Freudenberg Technology Innovation",
        "lang": "de",
        "role_strip": "Masterarbeit Data Science und Machine Learning im Spritzguss",
        "cl_date": "26. Juli 2026",
        "cl_subject": "Masterarbeit im Bereich Data Science und Machine Learning im Spritzguss in Weinheim",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg in Mannheim, mit Praxis im Aufbau produktionsnaher Machine Learning Pipelines auf realen Sensor und Prozessdaten. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline geliefert, die vier Wasserqualitaetsindikatoren prognostiziert und sechs Modelle direkt vergleicht, mit CatBoost Multi Quantil Regression fuer 80 Prozent Vorhersageintervalle. Sicher in Python, scikit learn, CatBoost, LightGBM, XGBoost und Prophet, mit klarem Blick fuer Datenqualitaet, Anti Leakage und robuste Modellbewertung.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit im Bereich Data Science und Machine Learning im Spritzguss bei Freudenberg Technology Innovation in Weinheim. Die Ausschreibung, die Auswertung umfangreicher Prozess und Maschinendaten aus dem Spritzguss mit Data Science und Machine Learning Methoden zur Verbesserung von Qualitaet und Effizienz, deckt sich sehr genau mit den Themen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline aufgebaut, die vier Wasserqualitaetsindikatoren, Chlorophyll a, Truebung, pH und geloester Sauerstoff prognostiziert, und dabei sechs Modelle direkt verglichen, darunter Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet. Fuer asymmetrische 80 Prozent Vorhersageintervalle habe ich CatBoost Multi Quantil Regression eingesetzt und strenge Anti Leakage Regeln durchgesetzt, was zu der ehrlichen Erkenntnis gefuehrt hat, welche Indikatoren physikalisch prognostizierbar sind und welche nicht. Genau dieser leakage bewusste und ehrliche Umgang mit Prozessdaten ist es, was fuer Spritzguss Maschinendaten den Unterschied macht.",
            "In CreditIQ habe ich ein Fairness by Design System entwickelt, den Disparate Impact Wert von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert. In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark, dbt und Apache Airflow auf Google Cloud ueber 128 tausend Datensaetze aus vier Quellen sauber verarbeitet und alle 15 Minuten automatisch aktualisiert. Meine Bachelorarbeit vergleicht sechs Klassifikatoren mit 10 facher Kreuzvalidierung, ROC AUC statt Genauigkeit auf einem unausgeglichenen Datensatz, und wurde als IEEE Paper mit ehrlicher Limitations Sektion verfasst.",
            "Ich arbeite sicher in Python und im wissenschaftlichen Stack aus scikit learn, CatBoost, LightGBM, XGBoost und Prophet, kann selbststaendig wissenschaftlich arbeiten und dokumentiere jede Entscheidung nachvollziehbar. Mein aktuelles Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations Zertifikate. Sehr gerne bespreche ich die konkrete Themenstellung mit Ihrem Team in Weinheim in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Airbus Operations GmbH — Hamburg
    # Master Thesis (d/f/m) within AI Suitability Evaluation for Modelica Physical Models
    # (Xing / Workday, 23 July 2026 fresh, Master Thesis, EN track)
    {
        "folder": "Airbus Hamburg Masterarbeit AI Suitability Modelica Physical Models",
        "company": "Airbus",
        "lang": "en",
        "role_strip": "Master Thesis, AI Suitability Evaluation for Modelica Physical Models",
        "cl_date": "26 July 2026",
        "cl_subject": "Master Thesis on AI Suitability Evaluation for Modelica Physical Models in Hamburg",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on evaluation of open weight and closed source large language models, honest benchmarking of alternative models on real data, and end to end machine learning delivery. I have shipped a modular Retrieval Augmented Generation system on Llama 3.1 8b via Groq with a custom decision making router, a fairness by design credit scoring system with SHAP driven subgroup analysis and full regulatory documentation, and a recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules. Proficient in Python and comfortable with LLM APIs, prompt engineering, and structured evaluation harnesses, I am the right fit for the Master Thesis on AI Suitability Evaluation for Modelica Physical Models at Airbus Hamburg.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis position on AI Suitability Evaluation for Modelica Physical Models at Airbus in Hamburg. The brief on evaluating the broad feasibility, accuracy, and engineering suitability of local open weights Large Language Models for physical modelling in Modelica, and on comparing the results against reference implementations, maps directly to the LLM system building and honest ML benchmarking work I have been shipping over the past year.",
            "My Hybrid RAG Orchestrator is a working LLM system that classifies user intent into three execution paths, local knowledge retrieval, external web search, and direct conversational logic, built on Llama 3.1 8b via Groq, LangChain orchestration, a persistent ChromaDB vector store with HuggingFace MiniLM L6 v2 embeddings, and a stateful memory agent shipped behind a Streamlit interface. That gives me the concrete grounding in open weight LLM behaviour, prompt design, and end to end LLM engineering that this thesis needs.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators and benchmarked six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, using CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty. I enforced strict anti leakage rules across the pipeline and surfaced the honest finding that some indicators are physically predictable while others are not. That mindset carries directly into evaluating whether a local LLM is genuinely suitable for engineering physics modelling or is merely producing plausible looking outputs.",
            "In CreditIQ I built rigorous evaluation harnesses with SHAP driven subgroup analysis, cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. My bachelor thesis compares six classifiers on a clinical dataset with 10 fold cross validation, chooses ROC AUC over accuracy on an imbalanced dataset, and is written up as an IEEE style paper with a candid limitations section. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I would be glad to discuss the exact Modelica reference set and evaluation criteria with the Hamburg team.",
        ],
    },

    # 3. TK Elevator GmbH — Duesseldorf
    # Working Student (d/f/m) Data Analytics
    # (StepStone / TK career page, 23 July 2026 fresh, Werkstudent, EN track)
    {
        "folder": "TK Elevator Working Student Data Analytics Duesseldorf",
        "company": "TK Elevator",
        "lang": "en",
        "role_strip": "Working Student, Data Analytics",
        "cl_date": "26 July 2026",
        "cl_subject": "Working Student Data Analytics in Duesseldorf",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on SQL, Python, dashboarding, and end to end data analytics delivery on real operational data. I have shipped a fully automated BigQuery medallion pipeline feeding a five page Looker Studio dashboard for concrete business questions, an interactive two tier Tableau dashboard with dynamic Set Actions and parameter driven analytics on a colour blind safe palette, and a real time cloud pipeline processing more than 128 thousand records on Google Cloud with dbt and Apache Airflow. Proficient in SQL and Python with practical BI experience, I am the right fit for a dynamic, multicultural Data Analytics working student role at TK Elevator in Duesseldorf.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_MOVIE_EN, P_TABLEAU_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_SAS, CERT_GOOGLE, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position in Data Analytics at TK Elevator in Duesseldorf. The brief on joining a dynamic, digitally addicted, multicultural team to set up a data analytics practice, with SQL as a must and Python as a nice to have, aligns directly with the end to end analytics work I have been shipping over the past year.",
            "In my Movie Analytics and ML Pipeline on GCP I engineered a fully automated Bronze to Silver to Gold BigQuery medallion architecture with schema enforcement, safe type casting, deduplication via window functions, and genre normalisation into a relational model, then delivered a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing. I also trained a leakage free BigQuery ML classifier that predicts whether a film will be a hit before release, using only pre release signals. That is directly the SQL heavy analytics engineering a mature elevator data platform benefits from.",
            "In my Fast Food Nutritional Analyzer and Meal Simulator I built a two tier Tableau dashboard combining an executive macro view with a granular food finder, using Set Actions, parameter driven Y axes, and complex IF THEN calculated fields, on a colour blind safe dark mode palette to reduce time to insight for a non technical audience. In my Real Time Flight Tracking Data Pipeline I processed live positions every 30 seconds against four sources of airport, aircraft, and weather data, using PySpark and dbt on Google Cloud with Apache Airflow refreshing every 15 minutes, over more than 128 thousand records. That is the same instrumentation and dashboarding mindset an elevator fleet analytics team needs.",
            "I am comfortable in SQL and Python, familiar with BI and cloud analytics stacks, and I speak English fluently with German at B1 in progress. I hold the SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations, and AWS Academy Cloud Foundations certificates. I would be glad to align the exact analytics practice scope with the TK Elevator team in Duesseldorf and start soon.",
        ],
    },

    # 4. ROSEN Group — Lingen
    # Masterarbeit (m/w/d) im Bereich Process Mining
    # (Xing, 22 July 2026, Master Thesis, DE track)
    {
        "folder": "ROSEN Group Masterarbeit Process Mining Lingen",
        "company": "ROSEN Group",
        "lang": "de",
        "role_strip": "Masterarbeit im Bereich Process Mining",
        "cl_date": "26. Juli 2026",
        "cl_subject": "Masterarbeit im Bereich Process Mining in Lingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau end to end Datenpipelines, Machine Learning auf Prozessdaten und BI Reporting. Ich habe eine vollstaendig automatisierte Bronze Silver Gold Medallion Pipeline in BigQuery mit einem leakage freien BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt, eine Echtzeit Cloud Pipeline mit PySpark, dbt und Apache Airflow ueber mehr als 128 tausend Datensaetze betrieben und ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken ausgeliefert. Sicher in Python, SQL und mit analytischem und konzeptionellem Blick fuer betriebliche Prozessdaten, bin ich die richtige Verstaerkung fuer die Masterarbeit im Process Mining bei ROSEN in Lingen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit im Bereich Process Mining bei der ROSEN Gruppe in Lingen. Ihre Ausschreibung, die Bearbeitung aktueller Fragestellungen im Process Mining in einem internationalen Unternehmensumfeld, komplexe Betriebsdaten in umsetzbare Erkenntnisse fuer Prozesstransparenz und Effizienzsteigerungen zu ueberfuehren, entspricht direkt den Themen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit Schema Enforcement, sicherem Type Casting, Deduplikation per Window Functions und Genre Normalisierung in ein relationales Modell, ergaenzt durch einen leakage freien BigQuery ML Klassifikator und ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen. Diese Architektur uebertraegt sich direkt auf Betriebsdaten und Prozesskennzahlen im Process Mining Kontext.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud rohe Daten sauber verarbeitet, mit dbt in analysebereite Tabellen ueberfuehrt und mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren, mit ueber 128 tausend Datensaetzen aus vier Quellen. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen umgesetzt, strengen Anti Leakage Regeln und einem Orchestrator mit Gate Checks. Beides ist die Basis fuer belastbares Event Log Mining und Prozessvorhersage.",
            "Ich arbeite sicher in Python, SQL, Cloud Datenpipelines und BI Werkzeugen wie Tableau und Looker Studio, bringe Teamfaehigkeit, analytischen Blick und selbststaendiges Arbeiten mit, und mein aktuelles Deutschniveau ist B1 in Bearbeitung, Englisch fliessend. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Foundations Zertifikate. Sehr gerne bespreche ich das konkrete Thema und die Rahmenbedingungen mit Ihrem Team in Lingen in einem persoenlichen Gespraech.",
        ],
    },

    # 5. Siemens Healthineers — Forchheim
    # Working Student (f/m/d) Data Science & AI for X-Ray Technology
    # (LinkedIn, 22 July 2026, Werkstudent 15h/week, EN track)
    {
        "folder": "Siemens Healthineers Working Student Data Science AI X-Ray Forchheim",
        "company": "Siemens Healthineers",
        "lang": "en",
        "role_strip": "Working Student, Data Science and AI for X-Ray Technology",
        "cl_date": "26 July 2026",
        "cl_subject": "Working Student Data Science and AI for X-Ray Technology in Forchheim",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on Python machine learning, deep learning benchmarking on unstructured data, and honest evaluation of models on imbalanced healthcare datasets. I have shipped a fairness by design credit scoring system on real data with SHAP driven subgroup analysis, an end to end recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules, and a bachelor thesis comparing six classifiers on a clinical dataset with 10 fold cross validation, choosing ROC AUC over accuracy for a 65 to 35 imbalanced target. Proficient in Python, scikit learn, and modern ML frameworks, I am the right fit for a Working Student position on Data Science and AI for X-Ray Technology at Siemens Healthineers in Forchheim.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on Data Science and AI for X-Ray Technology at Siemens Healthineers in Forchheim. The brief on supporting the development and evaluation of AI based methods for analysing unstructured data such as images of technical components, working hands on in Python, and exploring and applying deep learning models, aligns directly with the Python ML delivery and honest model evaluation work I have been shipping over the past year.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators on real sensor data, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty. I enforced strict anti leakage rules and surfaced the honest finding that some indicators are physically predictable while others are not without live optical sensors. That leakage aware, evaluation first mindset carries directly into X-Ray image and technical component analysis, where honest evaluation is the difference between a model that ships and one that fails silently.",
            "In CreditIQ I lifted the model's Disparate Impact ratio from 0.79 to 0.88, cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and backed the pipeline with unit tests at 100 percent branch coverage. My bachelor thesis compares six classifiers on a 768 patient clinical dataset with 10 fold cross validation, catches biologically impossible zero values that the original authors had overlooked, and chooses ROC AUC over accuracy on a 65 to 35 imbalanced target to avoid a misleadingly rosy accuracy figure. That is exactly the disciplined, healthcare adjacent evaluation Siemens Healthineers needs.",
            "I am proficient in Python and scikit learn, comfortable with deep learning frameworks, and I speak English fluently with German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I am available for the fixed term 15 hours per week Working Student position and would be glad to align the exact scope with the X-Ray Technology team in Forchheim.",
        ],
    },

    # 6. Avelios Medical GmbH — Muenchen
    # Working Student Machine Learning (all genders)
    # (LinkedIn, 22 July 2026, Werkstudent, EN track)
    {
        "folder": "Avelios Medical Working Student Machine Learning Muenchen",
        "company": "Avelios Medical",
        "lang": "en",
        "role_strip": "Working Student, Machine Learning",
        "cl_date": "26 July 2026",
        "cl_subject": "Working Student Machine Learning in Munich",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning integration into real clinical and operational data, honest evaluation on imbalanced datasets, and end to end delivery of intelligent systems. I have shipped a bachelor thesis comparing six classifiers on a real clinical dataset with 10 fold cross validation, catching biologically impossible values and choosing ROC AUC over accuracy on an imbalanced target, an end to end recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules, and a fairness by design classification system with SHAP driven subgroup analysis and 100 percent branch coverage unit tests. Proficient in Python, scikit learn, and modern ML frameworks, I am the right fit for a Working Student Machine Learning position supporting Avelios' mission to unlock clinical data for better patient care.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student Machine Learning position at Avelios Medical in Munich. The brief on supporting the integration of intelligent systems into real world clinical environments, in service of the mission to unlock clinical data for seamless healthcare operations and better patient care, aligns directly with the ML delivery on real healthcare adjacent data I have been shipping over the past year.",
            "My bachelor thesis is a leakage aware machine learning study on a real 768 patient clinical dataset, benchmarking six classifiers with 10 fold cross validation and per model confusion matrices. I caught biologically impossible zero values that the original authors had overlooked, applied IQR based outlier removal and proper imputation, and chose ROC AUC over accuracy on a 65 to 35 imbalanced target to avoid a misleadingly rosy accuracy figure. I wrote it up as an IEEE style paper with an honest limitations section. That is the same clinical data mindset Avelios' modular hospital information system needs.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators on real sensor data, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression for asymmetric 80 percent prediction intervals. In CreditIQ I lifted the Disparate Impact ratio from 0.79 to 0.88, cut the false negative rate from 44 percent to 16.7 percent, and backed the pipeline with unit tests at 100 percent branch coverage plus a full regulatory write up on EU AI Act and GDPR. That combination of honest ML evaluation and compliance ready delivery is the right base for real clinical integration.",
            "I am proficient in Python and scikit learn, comfortable with modern ML frameworks, and I speak English fluently with German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I would be glad to align the exact scope with the Avelios team in Munich.",
        ],
    },

    # 7. SAP — Garching bei Muenchen
    # Working Student (f/m/d) AI Engineering for Business Applications
    # (LinkedIn / SAP career page, 22 July 2026, Werkstudent, EN track)
    {
        "folder": "SAP Working Student AI Engineering Business Applications Garching",
        "company": "SAP",
        "lang": "en",
        "role_strip": "Working Student, AI Engineering for Business Applications",
        "cl_date": "26 July 2026",
        "cl_subject": "Working Student AI Engineering for Business Applications in Garching bei Muenchen",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on large language model application building, prompt engineering, and cloud backend delivery. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq, LangChain orchestration, ChromaDB, and a stateful memory agent behind a Streamlit interface, a fairness by design credit scoring tool with a plain language LLM generated explanation for finance managers, and a fully automated Bronze to Silver to Gold BigQuery medallion pipeline with BigQuery ML classifier on Google Cloud. Proficient in Python, LangChain, LLM APIs, and cloud platforms, I am the right fit for a Working Student position on AI Engineering for Business Applications in the Cloud ERP Finance Product Services team at SAP.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Working Student position on AI Engineering for Business Applications at SAP in Garching bei Muenchen. The brief on joining the Cloud ERP Finance Product Services team to design and build AI powered applications, from chatbots to automated document and planning analysis, deploying them to the cloud and continuously improving them from real feedback, maps directly to the LLM system building and cloud pipeline work I have been shipping over the past year.",
            "My Hybrid RAG Orchestrator is a working generative AI application that classifies user intent into three execution paths, local knowledge retrieval, external web search, and direct conversational logic, built on Llama 3.1 8b via Groq, LangChain orchestration, a persistent ChromaDB vector store with HuggingFace MiniLM L6 v2 embeddings, and a stateful memory agent shipped behind a Streamlit interface. That is a concrete end to end example of designing and shipping an LLM powered application that mirrors what your team builds internally.",
            "In CreditIQ I shipped a Streamlit decision support tool that gives finance managers a recommendation plus a plain language LLM generated explanation, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14, and backed the pipeline with unit tests at 100 percent branch coverage. In my Movie Analytics and ML Pipeline on GCP I built a fully automated Cloud Scheduler triggered Bronze to Silver to Gold BigQuery medallion architecture with a leakage free BigQuery ML classifier, secured by a least privilege service account and Secret Manager. That is the exact combination of enterprise ready cloud engineering and AI service delivery that SAP Cloud ERP Finance needs.",
            "I am proficient in Python, LangChain, LLM APIs, and comfortable with cloud platforms including GCP and AWS. I speak English fluently and German at B1 in progress. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I would be glad to align the exact scope with the Cloud ERP Finance Product Services team in Garching and start soon.",
        ],
    },

    # 8. 1&1 Mobilfunk GmbH — Duesseldorf
    # Werkstudent (w/m/d) AI & Data Automation - Mobilfunk Rollout
    # (StepStone / Xing, 20 July 2026, Werkstudent, DE track)
    {
        "folder": "1und1 Mobilfunk Werkstudent AI Data Automation Mobilfunk Rollout Duesseldorf",
        "company": "1&1 Mobilfunk",
        "lang": "de",
        "role_strip": "Werkstudent AI und Data Automation Mobilfunk Rollout",
        "cl_date": "26. Juli 2026",
        "cl_subject": "Werkstudent AI und Data Automation Mobilfunk Rollout in Duesseldorf",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Datenpipelines, Cloud ETL, Automatisierung und BI Reporting. Ich habe eine vollstaendig automatisierte BigQuery Medallion Pipeline mit einem leakage freien BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt, eine Echtzeit Cloud Pipeline mit PySpark, dbt und Apache Airflow ueber mehr als 128 tausend Datensaetze betrieben und ein interaktives Tableau Dashboard mit dynamischen Set Actions ausgeliefert. Sicher in Python, SQL, Cloud und BI Werkzeugen und mit Freude an Automatisierung, bin ich die richtige Verstaerkung fuer AI und Data Automation im Mobilfunk Rollout bei 1&1 in Duesseldorf.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent AI und Data Automation im Mobilfunk Rollout bei 1&1 Mobilfunk in Duesseldorf. Ihre Ausschreibung, die Mitarbeit an datengetriebener Automatisierung und Reporting im Rollout Umfeld, mit erster Erfahrung in Python, Power Automate oder vergleichbaren Automatisierungsloesungen, entspricht direkt den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich alle 30 Sekunden Live Positionen ueber Deutschland von einer offenen API gesammelt und mit PySpark auf Google Cloud gegen vier Quellen aus Flughafen, Flugzeug und Wetterdaten angereichert, ueber 128 tausend Datensaetze sauber verarbeitet und mit dbt in analysebereite Tabellen ueberfuehrt. Apache Airflow orchestriert das Gesamtsystem, so dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. Diese Kombination aus Ingestion, Cloud ETL und robuster Orchestrierung ist genau der Blick, den ein Rollout Daten Team braucht.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit Deduplikation per Window Functions, einem leakage freien BigQuery ML Klassifikator und einem fuenfseitigen Looker Studio Dashboard fuer konkrete Business Fragen. Mein Fast Food Meal Simulator ist ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken auf einer farbenblind sicheren Palette. Das sind die Reporting und Dashboarding Grundlagen, die im Rollout Monitoring genau gebraucht werden.",
            "Ich arbeite sicher in Python, SQL, Cloud Umgebungen wie GCP und AWS, sowie BI Werkzeugen wie Tableau und Looker Studio, mit ersten Erfahrungen in Automatisierungsansaetzen und einem klaren Blick fuer wiederholbare, robuste Ablaeufe. Mein aktuelles Deutschniveau ist B1 in Bearbeitung, Englisch fliessend. Ich bringe die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics und Google Data Analytics Foundations Zertifikate mit. Sehr gerne stelle ich mich in einem persoenlichen Gespraech vor und unterstuetze Ihr Team ab sofort.",
        ],
    },

    # 9. PMMG Group GmbH — Muenchen
    # Werkstudent Process & Data Science (w/m/d)
    # (Indeed / LinkedIn, mid July 2026, Werkstudent, DE track)
    {
        "folder": "PMMG Group Werkstudent Process Data Science Muenchen",
        "company": "PMMG Group",
        "lang": "de",
        "role_strip": "Werkstudent Process und Data Science",
        "cl_date": "26. Juli 2026",
        "cl_subject": "Werkstudent Process und Data Science in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Process nahen Datenpipelines, Machine Learning auf Betriebsdaten und Dashboarding fuer Entscheidungstraeger. Ich habe eine vollstaendig automatisierte Bronze Silver Gold Medallion Pipeline in BigQuery mit einem leakage freien BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken ausgeliefert und eine Echtzeit Cloud Pipeline mit PySpark, dbt und Apache Airflow ueber mehr als 128 tausend Datensaetze betrieben. Sicher in Python, SQL und mit strukturiertem analytischem Blick fuer Prozessdaten und Business Fragen, bin ich die richtige Verstaerkung fuer Process und Data Science, Business Process Management und AI Themen bei der PMMG Group.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Process und Data Science bei der PMMG Group in Muenchen. Ihre Ausschreibung, strukturierte Recherchen und Analysen zu aktuellen Themen aus Process Mining, Business Process Management und AI, mit flexiblen Arbeitszeiten und Remote Anteilen, entspricht direkt den Systemen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit schemakonformer Datenaufbereitung, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator, ergaenzt durch ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen zu Genre ROI, Wachstum fremdsprachiger Filme und Release Saison Timing. Diese Architektur ist die richtige Basis fuer Event Log Aufbereitung und Prozess KPI Reporting im Process Mining Umfeld.",
            "In meinem Fast Food Meal Simulator habe ich ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken ausgeliefert, mit einer farbenblind sicheren Dark Mode Palette fuer geringere Time to Insight bei Nicht Technikern. In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark, dbt und Apache Airflow auf Google Cloud ueber 128 tausend Datensaetze verarbeitet, mit Refresh alle 15 Minuten. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln umgesetzt. Das ist die Grundlage, um Prozessdaten wirklich belastbar auszuwerten und Ergebnisse verstaendlich fuer Entscheidungstraeger aufzubereiten.",
            "Ich arbeite sicher in Python, SQL, PowerPoint fuer strukturierte Ergebnisdarstellung und BI Werkzeugen wie Tableau und Looker Studio, mit klarem Blick fuer Prozessdaten und Business Fragen. Mein aktuelles Deutschniveau ist B1 in Bearbeitung, Englisch fliessend. Ich bringe die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics und Google Data Analytics Foundations Zertifikate mit. Sehr gerne stelle ich mich in einem persoenlichen Gespraech vor.",
        ],
    },

    # 10. GEA Hilge GmbH & Co. KG — Bodenheim (Raum Mainz)
    # Werkstudent (m/w/d) Data Analytics & AI
    # (Indeed / StepStone / GEA Workday, mid July 2026, Werkstudent, DE track)
    {
        "folder": "GEA Hilge Werkstudent Data Analytics AI Bodenheim",
        "company": "GEA Hilge",
        "lang": "de",
        "role_strip": "Werkstudent Data Analytics und AI",
        "cl_date": "26. Juli 2026",
        "cl_subject": "Werkstudent Data Analytics und AI in Bodenheim im Raum Mainz",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Data Analytics, Machine Learning und Reporting auf realen Betriebsdaten. Ich habe ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken ausgeliefert, eine vollstaendig automatisierte Bronze Silver Gold Medallion Pipeline in BigQuery mit BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt und ein Random Forest basiertes Klimarisiko Projekt mit klaren Reports fuer nicht technische Stakeholder abgeschlossen. Sicher in Python, SQL und BI Werkzeugen und mit ausgepraegtem Blick fuer Datenqualitaet, bin ich die richtige Verstaerkung fuer das Data Analytics und AI Team bei GEA Hilge in Bodenheim im Raum Mainz.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_TABLEAU_DE, P_MOVIE_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Analytics und AI bei GEA Hilge in Bodenheim im Raum Mainz. Die Ausschreibung, Teil eines internationalen Teams zu werden und in der Kombination aus Data Analytics und AI Verantwortung zu uebernehmen, in einem fortgeschrittenen Bachelor oder Masterstudium mit Informatik, Data Science oder Wirtschaftsinformatik Hintergrund, entspricht sehr genau dem, was ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meinem Fast Food Nutritional Analyzer und Meal Simulator habe ich ein zweistufiges Tableau Dashboard mit einer Executive Makro Sicht und einer granularen Food Finder Sicht gebaut, mit Set Actions, parametergesteuerten Y Achsen und komplexen IF THEN Calculated Fields, auf einer farbenblind sicheren Dark Mode Palette fuer eine geringere Time to Insight. Das ist direkt die Analytics und Reporting Denke, die GEA fuer ein internationales Team braucht.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit einem leakage freien BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt. In meinem Klimarisiko Projekt habe ich Random Forest Modelle zur Analyse des Zusammenhangs zwischen Ereignisdauer und finanzieller Wirkung entwickelt und die Ergebnisse in vollstaendigen visuellen Reports und kalibrierten Konfidenzaussagen fuer nicht technische Stakeholder aufbereitet. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln geliefert. Das ist die Basis fuer belastbare Data Analytics und AI Arbeit auf realen Betriebs und Sensordaten.",
            "Ich arbeite sicher in Python, SQL, Tableau und Looker Studio, mit Erfahrung in Cloud Umgebungen wie GCP und AWS. Mein aktuelles Deutschniveau ist B1 in Bearbeitung, Englisch fliessend. Ich bringe die SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations und AWS Academy Cloud Foundations Zertifikate mit. Sehr gerne unterstuetze ich Ihr Team ab sofort und stelle mich in einem persoenlichen Gespraech vor.",
        ],
    },
]
