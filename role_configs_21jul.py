"""Role configurations for the 21 July 2026 run (top 10).

Platform quota per 21 July 2026 rule:
  Indeed 3, StepStone 3, Xing 2, LinkedIn 2 = 10 roles.

All 10 postings are German language, so every deliverable ships on the German track
per the 20 July 2026 language match hard rule.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_21JUL = [
    # 1. aiomatic — Werkstudent Data Science, Hamburg (LinkedIn, freshest ~2 hours ago)
    {
        "folder": "aiomatic Werkstudent Data Science Hamburg",
        "company": "aiomatic",
        "lang": "de",
        "role_strip": "Werkstudent Data Science",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent Data Science bei aiomatic in Hamburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsnaher Machine Learning Systeme. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH mit CatBoost Multi Quantil Regression geliefert, ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain und ChromaDB gebaut und ein Fairness by Design Klassifikationssystem nach EU AI Act mit Unit Tests bei 100 Prozent Branch Coverage umgesetzt. Sicher in Python, scikit learn, pandas und LLM Frameworks, bin ich die richtige Verstärkung für das Data Science Team bei aiomatic in Hamburg.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Science bei aiomatic am Standort Hamburg. Die Ausschreibung, die Arbeit an modernen AI und Data Science Anwendungsfällen und die eigenständige Umsetzung von Modellen und Pipelines auf realen Daten, deckt sich sehr direkt mit den Projekten, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See geliefert, sechs Modelle direkt verglichen und CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt, mit strengen Anti Leakage Regeln über die gesamte Pipeline. In CreditIQ habe ich ein Fairness by Design System nach EU AI Act gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausführungspfade klassifiziert und über Llama 3.1 8b via Groq und LangChain dispatched, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore. In der Movie Analytics Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit einem leakage freien BigQuery ML Klassifikator und einem fünfseitigen Looker Studio Dashboard gebaut.",
            "Ich bin im vierten Semester des M.Sc. Data Science and Analytics eingeschrieben, arbeite sicher in Python, scikit learn und pandas, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne unterstütze ich Ihr Team ab sofort 20 Stunden pro Woche.",
        ],
    },

    # 2. Fraunhofer IIS — Praktikant/Abschlussarbeit Simulation und Machine Learning in der Robotik (Xing, ~15 hours ago)
    {
        "folder": "Fraunhofer IIS Praktikum Abschlussarbeit Simulation ML Robotik",
        "company": "Fraunhofer-Institut für Integrierte Schaltungen IIS",
        "lang": "de",
        "role_strip": "Praktikant und Abschlussarbeit Simulation und Machine Learning in der Robotik",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Praktikum und Abschlussarbeit Simulation und Machine Learning in der Robotik",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im rigorosen Aufbau von Machine Learning Pipelines auf realen Sensordaten. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH mit sechs Modellen im Vergleich und CatBoost Multi Quantil Regression geliefert, eine Echtzeit Google Cloud Pipeline betrieben, die über 128 tausend Flugdatensätze verarbeitet, und ein Fairness by Design Klassifikationssystem mit AIF360 und SHAP umgesetzt. Sicher in Python und mit Erfahrung in PyTorch nahen Workflows, bin ich die richtige Verstärkung für das Simulation und Machine Learning Team am Fraunhofer IIS.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für das Praktikum und die Abschlussarbeit im Bereich Simulation und Machine Learning in der Robotik am Fraunhofer Institut für Integrierte Schaltungen. Die Ausschreibung, die Kombination aus Simulation, Datenpipeline Arbeit und Machine Learning auf technischen Systemen, entspricht direkt der Denke, mit der ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline auf realen Sensordaten aufgebaut, sechs Modelle direkt verglichen, CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt und strenge Anti Leakage Regeln über die gesamte Pipeline erzwungen. Fehlende Winter Messwerte habe ich mit MICE Imputation rekonstruiert und einen synthetischen Winter Decay Prognose Rahmen entwickelt, damit die Modelle in der rekursiven Vorhersage nicht flach werden. Diese Disziplin, saubere Signalverarbeitung plus rigorose Evaluation, überträgt sich direkt auf Simulation und ML Aufgaben in der Robotik.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet, Live Positionen alle 30 Sekunden gegen vier Quellen aus Flughafen, Flugzeug und Wetterdaten angereichert und das Gesamtsystem mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten automatisch aktualisieren. In CreditIQ habe ich subgruppenweise Metriken mit SHAP berechnet und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent, das schult den Blick für belastbare Modellbewertung auf realen technischen Daten.",
            "Ich arbeite sicher in Python und komfortabel in PyTorch nahen Workflows, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne stimme ich mit meinem Professor an der SRH Heidelberg die genaue Fragestellung der Abschlussarbeit ab und starte im Vorfeld mit einem Pflichtpraktikum.",
        ],
    },

    # 3. Deloitte — Praktikant/Werkstudent Business & AI Insights (LinkedIn, fresh)
    {
        "folder": "Deloitte Praktikant Werkstudent Business AI Insights",
        "company": "Deloitte",
        "lang": "de",
        "role_strip": "Praktikant und Werkstudent Business und AI Insights",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Praktikant oder Werkstudent Business und AI Insights bei Deloitte",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Data Analytics, Business Intelligence und Generativer KI. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq gebaut. Sicher in Python, SQL und BI Werkzeugen, mit Erfahrung in Cloud Technologien, bin ich die richtige Verstärkung für Data Analytics und Business Intelligence Projekte bei Deloitte.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Praktikant oder Werkstudent Business und AI Insights bei Deloitte. Die Ausschreibung, die Mitarbeit an Data Analytics und Business Intelligence Projekten mit Python, SQL, BI Tools und Cloud Technologien sowie die Möglichkeit einer Bachelor oder Masterarbeit im gleichen Themenfeld, deckt sich direkt mit den Projekten, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur gebaut, mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen zu Genre ROI, Wachstum und Timing. Diese Struktur überträgt sich direkt auf die datengetriebenen Beratungsergebnisse, die Deloitte für Kunden liefert. In meinem Fast Food Nährwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit Executive Makro Sicht und granularer Detail Sicht entwickelt.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges Generative AI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore, das passt genau zum Bereich AI Insights. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit strengen Anti Leakage Regeln geliefert, das schult den Blick für saubere Analyseartefakte in einem Beratungsumfeld.",
            "Ich arbeite sehr sicher in Python, SQL und Excel, kenne Power BI und Tableau in Grundzügen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstütze ich Ihr Team ab dem gewünschten Startdatum.",
        ],
    },

    # 4. Pacemaker — Werkstudent Machine Learning Fokus Sustainability, Münster (Indeed, 15 July)
    {
        "folder": "Pacemaker Werkstudent ML Sustainability Muenster",
        "company": "pacemaker",
        "lang": "de",
        "role_strip": "Werkstudent Machine Learning mit Fokus Sustainability",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent Machine Learning Fokus Sustainability bei pacemaker",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in LLM basierten Systemen, Retrieval Methoden und Datenpipelines auf realen Daten. Ich habe ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain, ChromaDB und HuggingFace MiniLM L6 v2 Embeddings gebaut, eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert und ein Fairness by Design Klassifikationssystem nach EU AI Act umgesetzt. Sicher in Python und SQL, mit Erfahrung in Prompting, RAG Systemen und Embeddings, bin ich die richtige Verstärkung für das Sustainability Management Platform Team bei pacemaker.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Machine Learning mit Fokus Sustainability bei pacemaker. Die Ausschreibung, die Unterstützung bei der Entwicklung LLM basierter KI Systeme mit Embeddings und Retrieval Methoden, die Optimierung von Python Datenpipelines für Emissionsfaktor Datenbanken und die Analyse von Daten mit SQL für Machine Learning Modelle, spiegelt genau die Projekte wider, die ich in den letzten Monaten geliefert habe.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges LLM System mit einem eigenen Decision Making Router, der Nutzerintent in drei Ausführungspfade klassifiziert, lokale Wissensrecherche, externe Websuche oder direkte konversationelle Logik, alles auf Llama 3.1 8b via Groq mit LangChain. Ich habe ein persistentes semantisches Gedächtnis über PDF und Vektordaten mit ChromaDB und HuggingFace MiniLM L6 v2 Embeddings aufgebaut und multi turn Kontext über einen zustandsbehafteten MemoryAgent erhalten. Diese Prompting, RAG und Embedding Erfahrung überträgt sich direkt auf die pacemaker Sustainability Management Platform.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard. In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt, das schult den Blick für nachhaltigkeitsnahe Analysen.",
            "Ich bin im vierten Semester des M.Sc. Data Science and Analytics eingeschrieben, mit noch mindestens einem Jahr Studienzeit, arbeite sicher in Python und SQL, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne unterstütze ich Ihr Team an zwei bis drei Tagen pro Woche, remote first innerhalb Deutschlands mit gelegentlichen Terminen in Münster.",
        ],
    },

    # 5. Elobau — Werkstudent AI/Machine Learning, Leutkirch im Allgäu (Indeed, 8 July)
    {
        "folder": "Elobau Werkstudent AI ML Leutkirch",
        "company": "elobau GmbH und Co. KG",
        "lang": "de",
        "role_strip": "Werkstudent AI und Machine Learning",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent AI und Machine Learning bei elobau",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in end to end KI Lösungen, Datenanalyse und Modellierung. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH geliefert, ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain gebaut und eine vollständig automatisierte BigQuery Medallion Pipeline mit einem BigQuery ML Klassifikator und einem fünfseitigen Looker Studio Dashboard umgesetzt. Sicher in Python, mit Erfahrung in Klassifikation, Prognose und Natural Language Processing, bin ich die richtige Verstärkung für die AI und Machine Learning Anwendungsfälle bei elobau.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent AI und Machine Learning bei elobau in Leutkirch im Allgäu. Die Ausschreibung, die Entwicklung innovativer Anwendungsfälle im Bereich Künstliche Intelligenz gemeinsam mit den Fachbereichen, die Analyse und Visualisierung von Daten sowie die Implementierung von ML Modellen für Klassifikation, Prognose und Sprachverarbeitung, deckt sich direkt mit den Projekten, die ich im letzten Jahr geliefert habe.",
            "In CreditIQ habe ich ein Fairness by Design Klassifikationssystem gebaut, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent, gestützt auf scikit learn, AIF360 und SHAP mit Unit Tests bei 100 Prozent Branch Coverage. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline aufgebaut, sechs Modelle direkt verglichen und CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt. Diese end to end Denke überträgt sich direkt auf AI Lösungen in Ihrer Sensorik und Fahrzeugsystem Landschaft.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges Natural Language Processing System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore. In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine automatisierte Bronze Silver Gold Medallion Architektur in BigQuery mit einem leakage freien BigQuery ML Klassifikator und einem fünfseitigen Looker Studio Dashboard gebaut, das entspricht dem Aufbau produktiv einsatzfähiger AI Lösungen entlang Ihrer Wertschöpfungskette.",
            "Ich studiere im Master Data Science and Analytics, arbeite sicher in Python, kenne Datenanalyse und Modellierung, habe Berührungspunkte mit Microsoft Azure und den Grundprinzipien der Power Platform und kommuniziere sicher auf Englisch, mein Deutschniveau ist B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne unterstütze ich Frau Sylvia Losing und das interdisziplinäre Team ab dem gewünschten Startdatum.",
        ],
    },

    # 6. Tchibo — Werkstudent Data, Analytics & AI, Hamburg (Xing, 30 June)
    {
        "folder": "Tchibo Werkstudent Data Analytics AI Hamburg",
        "company": "Tchibo GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Data, Analytics und AI",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent Data, Analytics und AI bei Tchibo in Hamburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau moderner Data Analytics Plattformen und AI Werkzeuge. Ich habe eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerter Analytik umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq gebaut. Sicher in Python, SQL und BI Werkzeugen wie SAP Analytics Cloud, bin ich die richtige Verstärkung für die state of the art Big Data Analytics Platform bei Tchibo.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data, Analytics und AI bei der Tchibo GmbH am Standort Hamburg. Die Ausschreibung, die Arbeit an der state of the art Big Data Analytics Plattform mit Werkzeugen wie SAP Analytics Cloud und die Kombination aus Data Engineering, Analytics und AI, deckt sich direkt mit den Projekten, die ich in den letzten Monaten geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen zu Genre ROI, Wachstum und Timing. Diese Big Data Analytics Denke überträgt sich direkt auf die Tchibo Plattform. In meinem Fast Food Nährwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Feldern entwickelt.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit Anti Leakage Regeln und einem Orchestrator mit Gate Checks geliefert, das schult den Blick für saubere und zuverlässige Datenprodukte in einem retail nahen Umfeld.",
            "Ich arbeite sehr sicher in Python, SQL und Excel, kenne SAP Analytics Cloud und BI Werkzeuge in Grundzügen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstütze ich Ihr Team ab dem gewünschten Startdatum.",
        ],
    },

    # 7. Münchener Verein — Werkstudent Data Analytics und KI, München (StepStone)
    {
        "folder": "Muenchener Verein Werkstudent Data Analytics KI",
        "company": "Münchener Verein Versicherungsgruppe",
        "lang": "de",
        "role_strip": "Werkstudent Data Analytics und KI",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent Data Analytics und KI in München",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Reporting und KI gestützten Analyse Pipelines. Ich habe eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act mit AIF360 und SHAP umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain gebaut. Sicher in Python, SQL und Excel, mit Erfahrung in KI Werkzeugen und Modellevaluation, bin ich die richtige Verstärkung für das Data Analytics und KI Team der Münchener Direktion.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_CREDITIQ_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Data Analytics und KI in der Münchener Direktion des Münchener Verein für 15 bis 20 Stunden pro Woche. Die Ausschreibung, die Unterstützung im Bereich Data Analytics und KI in einer traditionsreichen Versicherungsgruppe, deckt sich direkt mit den Projekten, die ich im letzten Jahr in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur gebaut, mit Schema Enforcement, Deduplikation und einem leakage freien BigQuery ML Klassifikator, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. Diese Pipeline und Reporting Denke überträgt sich direkt auf Data Analytics Use Cases in einer Versicherung. In CreditIQ habe ich ein Fairness by Design Klassifikationssystem gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und den Fairness Accuracy Trade off als regulatorisch belastbare Entscheidung dokumentiert.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore, das ist genau die Art KI Werkzeug, das interne Prozesse einer Versicherung sinnvoll unterstützen kann. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit Anti Leakage Regeln geliefert, das schärft den Blick für Reporting Qualität in Compliance sensitiven Umgebungen.",
            "Ich arbeite sehr sicher in Python, SQL und Excel, kenne Power BI und moderne KI Werkzeuge in Grundzügen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstütze ich Ihr Team 15 bis 20 Stunden pro Woche ab dem gewünschten Startdatum.",
        ],
    },

    # 8. 1&1 — Werkstudent Quality Management und Datenanalyse, Düsseldorf (StepStone)
    {
        "folder": "1und1 Werkstudent Quality Management Datenanalyse",
        "company": "1und1 Mobilfunk GmbH",
        "lang": "de",
        "role_strip": "Werkstudent Quality Management und Datenanalyse",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent Quality Management und Datenanalyse bei 1und1",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Datenqualität, Reporting und quantitativer Analyse auf realen operativen Daten. Ich habe eine Echtzeit Google Cloud Pipeline aufgebaut, die über 128 tausend Datensätze verarbeitet, eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Pipeline mit Deduplikation und Schema Enforcement geliefert und ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerter Analytik umgesetzt. Sicher in Python, SQL und Excel, mit Erfahrung in Datenqualität und Reporting, bin ich die richtige Verstärkung für das 5G Service Team bei 1und1 im Bereich Quality Management.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE, P_TABLEAU_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Quality Management und Datenanalyse bei der 1und1 Mobilfunk GmbH in Düsseldorf. Die Ausschreibung, die Unterstützung des Teams im Bereich 5G Service über Datenanalyse, Qualitätskontrolle und die Aufbereitung operativer Kennzahlen, deckt sich sehr direkt mit den Projekten, die ich in den letzten Monaten geliefert habe.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet, Live Positionen alle 30 Sekunden gegen vier Quellen aus Flughafen, Flugzeug und Wetterdaten angereichert und das Gesamtsystem mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten automatisch alle 15 Minuten aktualisieren. In meiner Movie Analytics Pipeline auf GCP habe ich Schema Enforcement, Deduplikation per Window Functions und Genre Normalisierung in eine relationale Silver Schicht integriert, das entspricht genau der Datenqualitätsdisziplin, die 5G Service Analytics braucht.",
            "In meinem Fast Food Nährwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit Executive Makro Sicht und granularer Detail Sicht entwickelt, mit dynamischen Set Actions und parameter gesteuerten Feldern, dazu komplexe Calculated Fields, die ein Nicht Techniker direkt bedienen kann. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit einem Orchestrator gebaut, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, das schult den Blick für Qualitätssicherung in operativen Systemen.",
            "Ich arbeite sehr sicher in Python, SQL und Excel, kenne Tableau und Power BI Grundlagen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr 5G Service Team ab dem gewünschten Startdatum.",
        ],
    },

    # 9. REWE digital — Werkstudent IT Business Analyst Building Management, Köln (StepStone)
    {
        "folder": "REWE digital Werkstudent IT Business Analyst Building Management",
        "company": "REWE digital",
        "lang": "de",
        "role_strip": "Werkstudent IT Business Analyst Building Management",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Werkstudent IT Business Analyst Building Management in Köln",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung als Business Analyst nahe Schnittstelle zwischen fachlichen Anforderungen und technischer Umsetzung. Ich habe ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerter Analytik umgesetzt, eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq gebaut. Sicher in Python, SQL, Excel und dokumentationsorientierter Arbeit, bin ich die richtige Verstärkung für das Building Management IT Team bei REWE digital in Köln.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_TABLEAU_DE, P_MOVIE_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent IT Business Analyst Building Management bei REWE digital am Standort Köln. Die Ausschreibung, die Unterstützung bei der Analyse fachlicher Anforderungen an Building Management Systeme, die Übersetzung in technische Konzepte, die Dokumentation von Prozessen und die Zusammenarbeit mit interdisziplinären Teams, deckt sich direkt mit den Projekten, die ich in den letzten Monaten geliefert habe.",
            "In meinem Fast Food Nährwert Analyzer habe ich ein zweistufiges Tableau Dashboard mit Executive Makro Sicht und granularer Detail Sicht entwickelt, mit dynamischen Set Actions, parameter gesteuerten Feldern und komplexen Calculated Fields, das nicht technische Nutzer aktiv steuern. Diese Übersetzungsarbeit von fachlicher Frage zur klaren Analyse und dem passenden Dashboard ist die Kernaufgabe eines IT Business Analyst. In meiner Movie Analytics Pipeline auf GCP habe ich zusätzlich Anforderungen an Reporting in eine end to end automatisierte BigQuery Medallion Architektur mit Cloud Scheduler übersetzt.",
            "In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt und die Ergebnisse in Reports kommuniziert, die auch ein nicht technisches Publikum direkt umsetzen kann. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit einem Orchestrator gebaut, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft, das schärft den Blick für saubere Anforderungsanalyse und dokumentierte Prozesse.",
            "Ich arbeite sehr sicher in Python, SQL und Excel, kenne Tableau, Power BI und Confluence in Grundzügen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr Team ab dem gewünschten Startdatum in Köln.",
        ],
    },

    # 10. Porsche AG — Masterarbeit Datengetriebene Analyse und Prognose Thermal Runaway (Indeed, 18 May)
    {
        "folder": "Porsche Masterarbeit Thermal Runaway Weissach",
        "company": "Dr. Ing. h.c. F. Porsche AG",
        "lang": "de",
        "role_strip": "Masterarbeit Datengetriebene Analyse und Prognose Thermal Runaway",
        "cl_date": "21. Juli 2026",
        "cl_subject": "Masterarbeit Datengetriebene Analyse und Prognose charakteristischer Thermal Runaway Kenngrößen von Lithium Ionen Zellen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im datengetriebenen Modellieren technischer Messdaten. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH mit sechs Modellen im Vergleich und CatBoost Multi Quantil Regression für asymmetrische Vorhersageintervalle geliefert, eine Echtzeit Google Cloud Pipeline betrieben, die über 128 tausend Sensor Datensätze verarbeitet, und ein Machine Learning Klassifikationssystem auf einem klinischen Datensatz von 768 Datensätzen mit ROC AUC als Leitmetrik gebaut. Sicher in Python mit scikit learn und PyTorch nahen Workflows, mit Erfahrung in Datenanalyse und statistischer Modellierung, bin ich die richtige Verstärkung für die Masterarbeit im Kompetenzfeld Batteriesicherheit am Standort Weissach.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_CREDITIQ_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für die Masterarbeit zur datengetriebenen Analyse und Prognose charakteristischer Thermal Runaway Kenngrößen von Lithium Ionen Zellen bei der Dr. Ing. h.c. F. Porsche AG am Standort Weissach, Kennziffer J000020702. Die Aufgabenstellung, systematische Aufbereitung experimenteller Messdaten aus Thermal Runaway Versuchen, Identifikation charakteristischer Zielgrößen wie Onset Zeitpunkte, Maximalwerte und Venting Charakteristika sowie Konzeption und Training eines datengetriebenen Modellierungsansatzes, entspricht direkt der Art Arbeit, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff aufgebaut, sechs Modelle direkt verglichen, CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt und strenge Anti Leakage Regeln erzwungen. Fehlende Winter Messwerte habe ich mit MICE Imputation rekonstruiert und einen synthetischen Winter Decay Prognose Rahmen entwickelt. Diese Disziplin, saubere Datenaufbereitung plus rigorose Modellevaluation auf technischen Messdaten, überträgt sich direkt auf die Prognose charakteristischer Thermal Runaway Kenngrößen.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet, Live Positionen alle 30 Sekunden gegen vier Datenquellen angereichert und die Erkenntnis abgeleitet, dass der Luftverkehr bei starkem Regen um Faktor 4,4 einbricht, gestützt auf Python Statistik über TabPy. In CreditIQ habe ich mit SHAP subgruppenweise Metriken berechnet und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent, das schult den Blick für belastbare Identifikation dominanter Einflussgrößen in einem Parameterraum.",
            "Ich arbeite sicher in Python mit scikit learn und pandas, habe erste Erfahrung mit PyTorch nahen Workflows, kenne MS Office sehr sicher, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne stimme ich mit dem Fachbereich die genaue Ausgestaltung der Masterarbeit ab und starte zum gewünschten Zeitpunkt.",
        ],
    },
]
