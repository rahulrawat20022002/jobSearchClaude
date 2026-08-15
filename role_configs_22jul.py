"""Role configurations for the 22 July 2026 run (top 10).

Platform quota per 21 July 2026 rule:
  Indeed 4, StepStone 3, LinkedIn 3, Xing 0 (shortfall redistributed to Indeed
  first per the rule).

Language track per role, per the 20 July 2026 language match hard rule:
  1. Fraunhofer IEM Paderborn   DE (posting body in German)
  2. Porsche Weissach            EN (posting body in English)
  3. MVTec Muenchen              DE (posting body in German, requires B2 to C1 German)
  4. Muenchener Verein Muenchen  DE
  5. S-Kreditpartner Berlin      DE
  6. SimonsVoss Unterfoehring    DE
  7. Siemens Muenchen or Erlangen  EN (Mandatory Internship, posted in English)
  8. wemove digital solutions    DE
  9. CHECK24 Muenchen            DE (requires C1 German)
 10. Pacemaker Muenster          DE (Remote first)
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


CONFIGS_22JUL = [
    # 1. Fraunhofer IEM Paderborn — Masterarbeit Automating Software Product Health Monitoring with Agentic AI (Indeed, 22 July, Master Thesis)
    {
        "folder": "Fraunhofer IEM Masterarbeit Agentic AI SPHA",
        "company": "Fraunhofer-Institut fuer Entwurfstechnik Mechatronik IEM",
        "lang": "de",
        "role_strip": "Masterarbeit Agentic AI und Software Health Monitoring",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Masterarbeit Automating Software Product Health Monitoring with Agentic AI, Kennziffer 85145",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau agentischer LLM Systeme, rigoroser Modellbewertung und produktionsnaher Datenpipelines. Ich habe ein modulares Retrieval Augmented Generation System mit einem eigenen Decision Making Router auf Llama 3.1 8b via Groq und LangChain gebaut, ein Fairness by Design Klassifikationssystem nach EU AI Act mit Unit Tests bei 100 Prozent Branch Coverage geliefert und bei eRay GmbH eine end to end Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln umgesetzt. Sicher in Python, agiler Softwareentwicklung, LLM und Machine Learning Workflows, bin ich die richtige Verstaerkung fuer den naechsten Ausbaustand des Software Product Health Assistant am Fraunhofer IEM.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit zur Automatisierung des Software Product Health Monitoring mit Agentic AI in den Projekten CyberResilience.nrw und SPHA am Fraunhofer IEM in Paderborn, Kennziffer 85145. Die Ausschreibung, aktuelle Arbeiten zu agentischer KI im Software Monitoring auswerten, die relevantesten Agentenmuster identifizieren und einen Agenten implementieren, der sich in das SPHA Datenmodell integriert und rollenspezifische Ergebnisse fuer Entwicklung, Sicherheitsteam und Management liefert, entspricht sehr genau der Arbeit, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffaehiges agentisches System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausfuehrungspfade dispatched, lokale Wissensrecherche, externe Websuche oder direkte konversationelle Logik, umgesetzt auf Llama 3.1 8b via Groq und LangChain, mit einem persistenten ChromaDB Vektorstore und einem zustandsbehafteten MemoryAgent direkt in der Inference Pipeline. Das entspricht direkt dem Agentenmuster, das Sie fuer die SPHA KPI Hierarchie und die rollenspezifische Interpretation der Signale suchen.",
            "In CreditIQ habe ich rigorose Evaluations und Benchmarking Harnesses fuer ein Klassifikationssystem gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage sowie einer vollstaendigen regulatorischen Dokumentation nach EU AI Act und GDPR abgesichert. Bei eRay GmbH habe ich in einer sechsmonatigen Zusammenarbeit mit der SRH Hochschule eine end to end Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln geliefert. Diese Disziplin, saubere Signalverarbeitung, ehrliche Bewertung und rollentaugliche Ausgaben, ist genau die Denke, die das SPHA Team braucht.",
            "Ich arbeite sicher in Python und agiler Softwareentwicklung, habe Erfahrung mit LLM, Machine Learning und Deep Learning und spreche Englisch fliessend, Deutsch aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und SAS Certified Specialist Visual Business Analytics mit. Sehr gerne stimme ich die genaue Fragestellung mit Herrn Johnson und Herrn Ufuk ab und starte kurzfristig.",
        ],
    },

    # 2. Porsche AG Weissach — Masterarbeit Plausibilization of ADAS Front Camera Impairments Using ML (Indeed, 21 July, Master Thesis, EN)
    {
        "folder": "Porsche Weissach Masterarbeit ADAS Front Camera ML",
        "company": "Dr. Ing. h.c. F. Porsche AG",
        "lang": "en",
        "role_strip": "Master Thesis Student, ADAS Front Camera Machine Learning",
        "cl_date": "22 July 2026",
        "cl_subject": "Master Thesis Plausibilization of ADAS Front Camera Impairments Using Machine Learning, Kennziffer J000021231",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning work on real tabular sensor data and rigorous, explainable model evaluation. I have shipped a fairness by design credit scoring system with interpretable SHAP based subgroup analysis validated to EU AI Act thresholds, a recursive time series pipeline at eRay GmbH that benchmarked six models on real sensor data with strict anti leakage rules, and a Random Forest driven study translating raw global event data into calibrated, business relevant risk signals. Comfortable in Python and pandas, Git, and structured statistical evaluation, I am the right fit for a Master Thesis on plausibilizing ADAS front camera impairments using contextual, environmental, and vehicle based signals.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis on Plausibilization of ADAS Front Camera Impairments Using Machine Learning at Porsche AG in Weissach, Kennziffer J000021231. The brief on inferring impairment hypotheses from contextual, environmental, and vehicle based signals alone, clustering recurring patterns like fogging, icing, or low sun, and developing an interpretable model that assesses plausibility with transparent reasoning maps directly to the interpretable machine learning work I have been shipping over the past year.",
            "In CreditIQ I built an interpretable model that lifted the Disparate Impact ratio from 0.79 to 0.88 against the EU AI Act 80 percent fairness threshold, diagnosed a hidden intersectional bias through SHAP driven subgroup analysis, and cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent. Every decision was documented as a deliberate and regulator defensible trade off with a plain language LLM generated explanation, which is exactly the transparent reasoning your brief calls for.",
            "At eRay GmbH I built a recursive time series pipeline forecasting four water quality indicators for a German lake, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and enforcing strict anti leakage rules across the pipeline. In my Economic Impact Analysis of Global Climate Events I ran Random Forest models on tabular event data to translate context signals like duration and severity into calibrated business relevant risk assessments. That is the tabular, context driven, honest evaluation mindset your fleet impairment analysis needs.",
            "I am fluent in English and comfortable in German at B1 in progress, in depth in Python especially pandas, confident with Microsoft Office and Git, and familiar with common statistical frameworks. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates. I would be glad to shape the exact scope with my professor at SRH Heidelberg and start on the schedule that fits your team.",
        ],
    },

    # 3. MVTec Software GmbH Muenchen — Masterarbeit Computer Vision / Deep Learning (Indeed, 21 July, Master Thesis, DE, B2 to C1 German required)
    {
        "folder": "MVTec Masterarbeit Computer Vision Deep Learning",
        "company": "MVTec Software GmbH",
        "lang": "de",
        "role_strip": "Masterarbeit Computer Vision und Deep Learning",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Masterarbeit Computer Vision und Deep Learning",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Machine Learning und Deep Learning Systemen auf realen Daten. Ich habe ein modulares Retrieval Augmented Generation System mit LangChain, Llama 3.1 8b via Groq und HuggingFace Embeddings umgesetzt, ein Fairness by Design Klassifikationssystem nach EU AI Act mit rigoroser Evaluation und Unit Tests bei 100 Prozent Branch Coverage geliefert und bei eRay GmbH eine sechsmonatige Zeitreihen Pipeline mit sechs verglichenen Modellen aufgebaut. Sicher in Python, scikit learn, numpy, pandas und mit erster Erfahrung in Deep Learning Frameworks, bin ich die richtige Verstaerkung fuer eine industrienahe Masterarbeit im Bereich Computer Vision und Deep Learning bei MVTec.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit Computer Vision und Deep Learning bei der MVTec Software GmbH in Muenchen. Die Ausschreibung, eine Abschlussarbeit im industrienahen Umfeld eines weltweit fuehrenden Herstellers fuer Bildverarbeitungssoftware, in der moderne Bildverarbeitungsalgorithmen evaluiert und gegebenenfalls neu gestaltet werden, entspricht der Denke, mit der ich in den letzten Monaten Machine Learning Systeme in der Praxis geliefert habe.",
            "Mein Hybrider RAG Orchestrator zeigt meine Deep Learning Arbeit in einer produktionsaehnlichen Pipeline, mit Llama 3.1 8b via Groq, LangChain Orchestrierung, HuggingFace MiniLM L6 v2 Embeddings und einem ChromaDB Vektorstore, mit lauffaehiger Streamlit Oberflaeche. In CreditIQ habe ich rigorose Modellbewertung mit SHAP getriebener Subgruppenanalyse und Standardmetriken einschliesslich ROC AUC gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert. Diese Evaluationsdisziplin ist genau das, was die Arbeit an Bildverarbeitungsalgorithmen braucht.",
            "Bei eRay GmbH habe ich eine end to end Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln geliefert. In der Diabetes Prediction Bachelorarbeit habe ich sechs Klassifikatoren auf einem klinischen Datensatz mit 10 facher Kreuzvalidierung verglichen und ROC AUC als ehrliche Leitmetrik fuer einen unausgeglichenen Zieltyp gewaehlt. Diese Kombination aus sauberer Datenaufbereitung, ehrlicher Bewertung und Zusammenarbeit mit Fachbereichen ist die richtige Grundlage fuer eine Abschlussarbeit im MVTec Forschungsteam.",
            "Ich arbeite sicher in Python, kenne scikit, numpy und pandas und habe erste Erfahrungen mit Deep Learning Frameworks. Deutsch spreche ich aktuell auf Niveau B1 in Bearbeitung und lerne aktiv weiter, Englisch fliessend in Wort und Schrift. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und SAS Certified Specialist Visual Business Analytics mit. Sehr gerne stimme ich die genaue Fragestellung mit dem Forschungsteam ab und starte am naechstmoeglichen Termin.",
        ],
    },

    # 4. Muenchener Verein Versicherungsgruppe Muenchen — Werkstudent Data Analytics und KI (StepStone, ~21 July, Werkstudent, DE)
    {
        "folder": "Muenchener Verein Werkstudent Data Analytics KI",
        "company": "Muenchener Verein Versicherungsgruppe",
        "lang": "de",
        "role_strip": "Werkstudent Data Analytics und KI",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent Data Analytics und KI in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Datenanalyse, Business Intelligence und angewandter Kuenstlicher Intelligenz. Ich habe eine vollstaendig automatisierte BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt und eine Random Forest gestuetzte Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse erstellt. Sicher in Python, scikit learn, pandas, NumPy und BI Werkzeugen, bin ich die richtige Verstaerkung fuer das Data Analytics und KI Team des Muenchener Verein.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Analytics und KI beim Muenchener Verein in Muenchen. Die Ausschreibung, die Mitarbeit an praktischen Data Science und KI Anwendungen in der Versicherungsbranche, Recherche zu aktuellen Entwicklungen und Best Practices sowie die Arbeit an einem modernen Technologie Stack, deckt sich sehr genau mit der Praxis, die ich in den letzten Monaten in eigenen Projekten geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit schemakonformer Datenaufbereitung, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator gebaut, ergaenzt durch ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen. In meinem Fast Food Nuetzwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit dynamischer Set Action Steuerung und farbenblind sicherer Dark Mode Palette ausgeliefert, das nicht technische Nutzer direkt bedienen koennen.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich Random Forest Modelle auf rohen Ereignisdaten trainiert, Feature Importance und Residuenanalysen genutzt und die Ergebnisse fuer nicht technische Stakeholder in klaren visuellen Reports aufbereitet. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und Anti Leakage Regeln umgesetzt. Diese Kombination aus BI, angewandter Statistik und ehrlicher Modellbewertung ist genau die Grundlage, die eine Versicherung fuer datengetriebene Entscheidungen braucht.",
            "Ich arbeite sicher in Python, scikit learn, pandas und NumPy, kenne TensorFlow und PyTorch nahe Workflows und bin vertraut mit BI Tools wie Tableau und Power BI. Deutsch aktuell B1 in Bearbeitung, Englisch fliessend. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne stelle ich mich in einem persoenlichen Gespraech vor.",
        ],
    },

    # 5. S-Kreditpartner GmbH Berlin — Werkstudent Advanced Analytics und AI (StepStone, ~21 July, Werkstudent, DE)
    {
        "folder": "S-Kreditpartner Werkstudent Advanced Analytics AI",
        "company": "S-Kreditpartner GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Advanced Analytics und AI",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent Advanced Analytics und AI in Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Analytics und KI Systeme fuer regulierte Anwendungsfelder wie Kreditscoring. Ich habe ein Fairness by Design Credit Scoring System nach EU AI Act mit Streamlit Entscheidungsunterstuetzung geliefert, ein modulares Retrieval Augmented Generation System mit einem eigenen Decision Making Router auf Llama 3.1 8b via Groq und LangChain umgesetzt und eine automatisierte BigQuery Medallion Pipeline mit BigQuery ML Klassifikator und Looker Studio Reporting aufgebaut. Sicher in Python, SQL und modernen KI Frameworks, bin ich die richtige Verstaerkung fuer Advanced Analytics und AI in der Sparkassen Finanzgruppe.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Advanced Analytics und AI bei der S-Kreditpartner GmbH in Berlin. Die Ausschreibung, die Mitwirkung an Python basierten Microservices, ueber die analytische Verfahren automatisiert, skalierbar und bankweit nutzbar werden, und die Konzeption von KI Agenten, die Analysen automatisieren, Daten interpretieren und Qualitaetspruefungen unterstuetzen, deckt sich sehr direkt mit den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "In CreditIQ habe ich ein Kreditscoring System End to End nach EU AI Act und AGG aufgesetzt, den Disparate Impact Wert von 0,79 auf 0,88 gehoben, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage sowie einer vollstaendigen regulatorischen Dokumentation abgesichert. Das Streamlit Entscheidungsunterstuetzungs Tool liefert Finanzverantwortlichen eine Empfehlung plus eine in einfacher Sprache generierte LLM Erklaerung, konform zu GDPR Artikel 22 und EU AI Act Artikel 14.",
            "Mein Hybrider RAG Orchestrator ist ein lauffaehiges KI Agenten System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausfuehrungspfade klassifiziert, ergaenzt um ChromaDB Vektorstore und HuggingFace MiniLM L6 v2 Embeddings. Zusammen mit meiner Movie Analytics und ML Pipeline auf GCP, einer vollstaendig automatisierten Bronze Silver Gold Medallion Architektur mit leakage freiem BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard, zeigt das die Skalierung analytischer Verfahren zu Microservice Denke.",
            "Ich arbeite sicher in Python, SQL und modernen KI Frameworks, spreche Deutsch aktuell B1 in Bearbeitung und Englisch fliessend. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und SAS Certified Specialist Visual Business Analytics mit. Sehr gerne unterstuetze ich Ihr Team ab sofort 20 Stunden pro Woche.",
        ],
    },

    # 6. SimonsVoss Technologies Unterfoehring — Werkstudent IT Data Science und KI (StepStone, ~21 July, Werkstudent, DE)
    {
        "folder": "SimonsVoss Werkstudent IT Data Science KI",
        "company": "SimonsVoss Technologies GmbH",
        "lang": "de",
        "role_strip": "Werkstudent IT Data Science und KI",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent IT Data Science und KI in Unterfoehring",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Business Intelligence, Data Analytics und angewandter KI. Ich habe eine vollstaendig automatisierte BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq und LangChain gebaut. Sicher in Python, SQL und BI Werkzeugen, bin ich die richtige Verstaerkung fuer das IT Team bei SimonsVoss rund um Business Intelligence, Data Analytics und KI.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent IT im Bereich Business Intelligence, Data Analytics und KI bei SimonsVoss Technologies in Unterfoehring bei Muenchen. Die Ausschreibung, die Kombination aus BI, Datenanalyse und angewandter KI in einem produktnahen IT Team, entspricht direkt den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit schemakonformer Aufbereitung, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator gebaut, mit fuenfseitigem Looker Studio Dashboard fuer konkrete Business Fragen. In meinem Fast Food Analyzer habe ich ein zweistufiges Tableau Dashboard mit Set Actions, parameter gesteuerten Y Achsen und farbenblind sicherer Dark Mode Palette umgesetzt, das nicht technische Stakeholder direkt bedienen koennen. Diese Kombination aus Pipeline und Frontend ist die Grundlage fuer BI Arbeit in einem modernen IT Team.",
            "Mein Hybrider RAG Orchestrator ist ein lauffaehiges KI System mit einem eigenen Decision Making Router auf Llama 3.1 8b via Groq und LangChain, mit persistentem ChromaDB Vektorstore und HuggingFace MiniLM L6 v2 Embeddings. Bei eRay GmbH habe ich eine end to end Zeitreihen Pipeline mit sechs verglichenen Modellen und Anti Leakage Regeln geliefert. Zusammengenommen zeigt das die drei Beine, die die Rolle braucht, BI, Analytics und angewandte KI.",
            "Ich arbeite sicher in Python und SQL, kenne Cloud Umgebungen und BI Tools und spreche Deutsch aktuell B1 in Bearbeitung, Englisch fliessend. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstuetze ich Ihr Team von Mannheim aus mit regelmaessigen Praesenztagen am Standort Unterfoehring.",
        ],
    },

    # 7. Siemens Muenchen / Erlangen — Mandatory Internship Data Science and Deep Learning for Energy Systems (LinkedIn, Internship, EN)
    {
        "folder": "Siemens Mandatory Internship DS DL Energy Systems",
        "company": "Siemens",
        "lang": "en",
        "role_strip": "Mandatory Intern, Data Science and Deep Learning for Energy Systems",
        "cl_date": "22 July 2026",
        "cl_subject": "Mandatory Internship, Data Science and Deep Learning for Energy Systems",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on time series forecasting, deep learning, and cloud data pipeline work on real sensor data. I have shipped a recursive time series pipeline at eRay GmbH forecasting four water quality indicators for a German lake using CatBoost multi quantile regression with asymmetric 80 percent prediction intervals, a real time Google Cloud pipeline processing over 128 thousand flight records enriched against four data sources every 30 seconds, and a fairness by design classification system with rigorous evaluation and unit tests at 100 percent branch coverage. Proficient in Python and deep learning frameworks, comfortable with anti leakage evaluation, I am the right fit for a Mandatory Internship on Data Science and Deep Learning for Energy Systems at Siemens.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_FLIGHT_EN, P_CREDITIQ_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_SAS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Mandatory Internship on Data Science and Deep Learning for Energy Systems at Siemens, based in Munich or Erlangen at 35 hours per week. The brief on forecasting, modeling, and optimization for energy systems using Python and deep learning frameworks maps directly to the time series and cloud data pipeline work I have been shipping over the past year.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty. I enforced strict anti leakage rules and surfaced the honest finding that some indicators are physically predictable while others are not without live optical sensors. That forecasting and honest evaluation discipline transfers directly to energy demand and generation modeling.",
            "In my Real Time Flight Tracking Data Pipeline I collected live positions from the OpenSky Network every 30 seconds, enriched them against four data sources including weather, and orchestrated PySpark and dbt on Google Cloud with Apache Airflow so batch and real time layers refresh automatically every 15 minutes across more than 128 thousand records. In CreditIQ I built rigorous evaluation and benchmarking harnesses with SHAP driven analysis and unit tests at 100 percent branch coverage. That is the same automation and evaluation mindset your energy systems work needs.",
            "I am proficient in Python and comfortable with deep learning frameworks, hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and SAS Certified Specialist Visual Business Analytics certificates, and my current German level is B1 in progress. I would be glad to start the Mandatory Internship for six months at 35 hours per week on the schedule that fits your team.",
        ],
    },

    # 8. wemove digital solutions GmbH — Werkstudent im Bereich Geospatial Data Science (LinkedIn, Werkstudent, DE)
    {
        "folder": "wemove Werkstudent Geospatial Data Science",
        "company": "wemove digital solutions GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Geospatial Data Science",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent im Bereich Geospatial Data Science",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Geodaten naher Datenanalyse, Cloud Datenpipelines und BI Visualisierung. Ich habe eine Echtzeit Google Cloud Pipeline betrieben, die alle 30 Sekunden Live Flugpositionen ueber Deutschland gegen Flughafen, Flugzeug und Wetterdaten anreichert und ueber 128 tausend Datensaetze verarbeitet, eine BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert und ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerten Kennzahlen umgesetzt. Sicher in Python, PySpark, SQL, dbt und BI Werkzeugen, bin ich die richtige Verstaerkung fuer das Geospatial Data Science Team bei wemove.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent im Bereich Geospatial Data Science bei wemove digital solutions. Die Ausschreibung, praxisnahe Arbeit an Geodaten mit einem engagierten Team, entspricht direkt den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich alle 30 Sekunden Live Flugpositionen von der OpenSky Network API gesammelt und mit PySpark auf Google Cloud gegen vier Quellen aus Flughafen, Flugzeug und Wetterdaten angereichert, ueber 128 tausend Datensaetze sauber verarbeitet und mit dbt in analysebereite Tabellen ueberfuehrt, wobei jeder Flugbewegung der naechstgelegene Flughafen berechnet wurde. Apache Airflow orchestriert das Gesamtsystem, so dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. Das ist eine direkte Vorschau darauf, wie ich raeumliche Datenmodelle bei wemove baue.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit sauberer Datenaufbereitung und einem leakage freien BigQuery ML Klassifikator umgesetzt, ergaenzt durch ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen. In meinem Fast Food Analyzer habe ich ein zweistufiges Tableau Dashboard mit Set Actions und farbenblind sicherer Dark Mode Palette gebaut, das entspricht der Visualisierungsseite geospatialer Analytics.",
            "Ich arbeite sicher in Python, PySpark, SQL, dbt und BI Werkzeugen, kenne Cloud Umgebungen und spreche Deutsch aktuell B1 in Bearbeitung, Englisch fliessend. Ich bringe die Zertifikate AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstuetze ich Ihr Team ab sofort und stelle mich gerne in einem persoenlichen Gespraech vor.",
        ],
    },

    # 9. CHECK24 Vergleichsportal Muenchen — Werkstudent Data Engineering CFO Office (Indeed, 15 July, Werkstudent, DE, C1 required)
    {
        "folder": "CHECK24 Werkstudent Data Engineering CFO Office",
        "company": "CHECK24 Strategy Hub GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Data Engineering CFO Office",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent Data Engineering im CFO Office in Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer ETL Pipelines, Reporting und KI Datenprodukten. Ich habe eine Echtzeit Google Cloud Pipeline betrieben, die alle 30 Sekunden Live Positionen sammelt und ueber 128 tausend Datensaetze verarbeitet, eine vollstaendig automatisierte BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert und ein interaktives Tableau Dashboard mit dynamischen Set Actions umgesetzt. Sicher in Python, SQL, Tableau, Power BI und Google Cloud sowie AWS, bin ich die richtige Verstaerkung fuer das Data Studio im CFO Office bei CHECK24.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Engineering im CFO Office bei CHECK24 in Muenchen. Die Ausschreibung, Entwicklung von Trackingsystemen, Aufbau SQL basierter ETL Pipelines aus relationalen Datenbanken, tiefgreifende Analysen auf grossen Datenmengen, robuste Dashboards in Tableau oder Power BI und aktive Gestaltung datengetriebener Steuerungsinstrumente, entspricht sehr direkt den Systemen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud alle 30 Sekunden Live Positionen gesammelt und mit dbt in analysebereite Tabellen ueberfuehrt, das Ganze mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollstaendig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit sauberer Datenaufbereitung und einem leakage freien BigQuery ML Klassifikator gebaut, ergaenzt durch ein fuenfseitiges Looker Studio Dashboard fuer konkrete Business Fragen. Das ist die ETL und Reporting Grundlage, die das CFO Office braucht.",
            "In meinem Fast Food Nuetzwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit dynamischer Set Action Steuerung und parameter gesteuerten Kennzahlen umgesetzt, das nicht technische Stakeholder direkt bedienen koennen. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und Anti Leakage Regeln geliefert. Diese Kombination aus Data Engineering, BI und ehrlicher Analyse ist die richtige Grundlage fuer strategische KPI Steuerung im CFO Office.",
            "Ich arbeite sicher in Python und SQL, kenne Tableau, Power BI, Google Cloud und AWS und arbeite gerne mit KI Tools wie ChatGPT und Cursor.ai. Deutsch aktuell B1 in Bearbeitung mit aktivem Lernen, Englisch fliessend. Ich bringe die Zertifikate AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics und Google Data Analytics Foundations mit. Sehr gerne unterstuetze ich Ihr Data Studio ab sofort.",
        ],
    },

    # 10. Pacemaker Muenster — Werkstudentin Machine Learning Fokus Sustainability (Indeed, 15 July, Werkstudent, DE, Remote first)
    {
        "folder": "Pacemaker Werkstudent Machine Learning Sustainability",
        "company": "pacemaker.ai",
        "lang": "de",
        "role_strip": "Werkstudent Machine Learning mit Fokus Sustainability",
        "cl_date": "22. Juli 2026",
        "cl_subject": "Werkstudent Machine Learning mit Fokus Sustainability",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Machine Learning, LLM Systemen und Nachhaltigkeitsanalytik. Ich habe ein modulares Retrieval Augmented Generation System mit LangChain, Llama 3.1 8b via Groq, HuggingFace MiniLM L6 v2 Embeddings und einem ChromaDB Vektorstore gebaut, ein Fairness by Design Klassifikationssystem nach EU AI Act mit Unit Tests bei 100 Prozent Branch Coverage geliefert und eine Random Forest gestuetzte Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse erstellt. Sicher in Python, SQL und LLM Frameworks, mit erster Beruehrung zu Emissionsfaktor Datenbanken und Nachhaltigkeitsthemen, bin ich die richtige Verstaerkung fuer die Sustainability Management Platform bei pacemaker.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Machine Learning mit Fokus Sustainability bei pacemaker.ai in Muenster. Die Ausschreibung, die Mitentwicklung Ihrer KI Systeme rund um LLM basierte Ansaetze, Embeddings und Retrieval Methoden zur praezisen Berechnung von Carbon Footprints und weiteren Nachhaltigkeitskennzahlen sowie die Optimierung Python basierter Datenpipelines fuer Ihre Emissionsfaktor Datenbank, deckt sich sehr genau mit den Systemen, die ich in den letzten Monaten in der Praxis gebaut habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffaehiges LLM System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausfuehrungspfade dispatched, ergaenzt um HuggingFace MiniLM L6 v2 Embeddings und einen persistenten ChromaDB Vektorstore, mit einer Streamlit Oberflaeche darueber. Das entspricht direkt der Kombination aus Prompting, RAG Systemen und Embeddings, die Sie in Ihrer Sustainability Management Platform einsetzen.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich Random Forest Modelle auf rohen globalen Ereignisdaten trainiert und die Ergebnisse in fuer nicht technische Stakeholder verstaendliche Reports uebersetzt, mit ehrlichen Konfidenzaussagen. In CreditIQ habe ich rigorose ML Evaluation gebaut, mit SHAP getriebener Subgruppenanalyse, ROC AUC als Leitmetrik und Unit Tests bei 100 Prozent Branch Coverage. Diese Denke, saubere Datenaufbereitung, ehrliche Bewertung und klare Kommunikation an Fachbereiche, ist genau die Grundlage, die Ihre Sustainability Manager brauchen.",
            "Ich arbeite sicher in Python und SQL, habe mit LLMs, Prompting, RAG und Embeddings eigene Projekte umgesetzt und interessiere mich stark fuer Nachhaltigkeitsthemen. Deutsch aktuell B1 in Bearbeitung, Englisch sehr gut in Wort und Schrift. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne unterstuetze ich Ihr Team an 2 bis 3 Tagen pro Woche remote von Mannheim aus.",
        ],
    },
]
