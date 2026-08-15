"""Role configurations for the 20 July 2026 run (top 9).

Imports base project bank and building blocks from role_configs.py.
The main role_configs.CONFIGS pointer aliases this module's CONFIGS_20JUL.
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


CONFIGS_20JUL = [
    # 1. MTU Aero Engines — Werkstudent Customer Support & Data Analytics Industriegasturbine, Ludwigsfelde (German track, posted 16 July)
    {
        "folder": "MTU Aero Engines Werkstudent Data Analytics Industriegasturbine",
        "company": "MTU Aero Engines",
        "lang": "de",
        "role_strip": "Werkstudent Customer Support und Data Analytics",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Werkstudent Customer Support und Data Analytics Industriegasturbine in Ludwigsfelde",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Datenanalyse, Reporting und Dashboarding auf realen technischen Daten. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt und eine Random Forest gestützte Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse veröffentlicht. Sicher in Python, SQL, Excel, PowerPoint und Power BI nahen Werkzeugen, bin ich die richtige Verstärkung für das Customer Account Management Team bei der datenbasierten Entscheidungsunterstützung rund um die Industriegasturbinen LM2500 und LM6000.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Customer Support und Data Analytics Industriegasturbine am Standort Ludwigsfelde. Ihre Ausschreibung, die Vorbereitung und Umsetzung von Datenanalysen und Auswertungen für die datenbasierte Entscheidungsfindung des Top Managements, die Erstellung von Management Reports und Entscheidungsvorlagen sowie die Mitarbeit bei der Analyse von Projektkosten und Leistungsdaten, deckt sich sehr genau mit der Arbeit, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator gebaut, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen zu Genre ROI, Wachstum und Timing. Diese Reporting Architektur überträgt sich direkt auf Kostenvoranschläge, Shop Visit Kosten und Field Service Kennzahlen im Aeroderivate Umfeld.",
            "In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt und die Ergebnisse in Reports kommuniziert, die auch ein nicht technisches Publikum direkt umsetzen kann. Mein Fast Food Nährwert Analyzer zeigt die Dashboard Seite mit Set Actions, parameter gesteuerter Analytik und einer klaren Executive Sicht neben einer Detail Sicht. Beides passt zu den Kunden und Management Präsentationen, die die Rolle verlangt.",
            "Zur Sprachanforderung: mein aktuelles Deutschniveau ist B1 in Bearbeitung, ich lerne aktiv weiter, und Englisch spreche ich fließend. Ich arbeite sehr sicher in Excel, PowerPoint, Python und SQL, kenne die Grundlagen von Power BI und bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations sowie AWS Academy Cloud Foundations mit. Sehr gerne unterstütze ich Ihr Team ab der ersten Woche bei Analysen, Reports und schnittstellenübergreifenden Prozessverbesserungen.",
        ],
    },

    # 2. Dräger — Praktikum Künstliche Intelligenz und maschinelles Lernen für interne Prozessoptimierung, Lübeck (German track, posted 16 July)
    {
        "folder": "Draeger Praktikum KI ML Prozessoptimierung",
        "company": "Drägerwerk AG und Co. KGaA",
        "lang": "de",
        "role_strip": "Praktikant KI und Maschinelles Lernen",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Praktikum Künstliche Intelligenz und maschinelles Lernen für interne Prozessoptimierung in Lübeck",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning, Vorhersagemodellen und produktionsnahen Datenpipelines. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH aufgebaut, ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain und ChromaDB geliefert sowie ein Fairness by Design Klassifikationssystem nach EU AI Act mit Unit Tests bei 100 Prozent Branch Coverage umgesetzt. Sicher in Python, scikit learn, pandas und SQL, bin ich die richtige Verstärkung für die KI und Machine Learning gestützte Prozessoptimierung im Bereich Corporate Technology und Innovation bei Dräger.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für das Praktikum Künstliche Intelligenz und maschinelles Lernen für interne Prozessoptimierung am Standort Lübeck. Die Ausschreibung, die Entwicklung von Vorhersagemodellen und intelligenten Systemen für betriebliche Effizienz und Entscheidungsprozesse, die Analyse großer Datenmengen und die Zusammenarbeit mit einem interdisziplinären Team aus Controlling, Produktion und IT, deckt sich direkt mit dem, was ich im laufenden Master und in der Praxis bei eRay GmbH gebaut habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff geliefert, sechs Modelle direkt verglichen und CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt, mit strengen Anti Leakage Regeln über die gesamte Pipeline hinweg. In CreditIQ habe ich Machine Learning Modelle rigoros gegen Fairness Grenzwerte validiert, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System, das Nutzerintent über einen eigenen Decision Making Router in drei Ausführungspfade klassifiziert und dabei Llama 3.1 8b via Groq mit LangChain, ChromaDB und HuggingFace MiniLM L6 v2 Embeddings kombiniert. In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit leakage freiem BigQuery ML Klassifikator und einem fünfseitigen Looker Studio Dashboard, das entspricht der Reporting Seite, die intelligente Systeme in einem Produktionsumfeld tragen müssen.",
            "Ich arbeite sicher in Python mit scikit learn und pandas, kenne SQL Datenbanken und habe erste Berührungspunkte mit Apache Spark und Databricks nahen Plattformen. Ich bin im vierten Semester des M.Sc. Data Science and Analytics eingeschrieben und mein aktuelles Deutschniveau ist B1 in Bearbeitung. Sehr gerne stelle ich mich in einem persönlichen Gespräch vor und unterstütze das Corporate Technology und Innovation Team ab dem gewünschten Startdatum.",
        ],
    },

    # 3. Witt-Gruppe — Praktikum Künstliche Intelligenz und Machine Learning 50% Remote, Weiden (German track, posted 15 July)
    {
        "folder": "Witt-Gruppe Praktikum KI ML",
        "company": "Witt-Gruppe",
        "lang": "de",
        "role_strip": "Praktikum Künstliche Intelligenz und Machine Learning",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Praktikum Künstliche Intelligenz und Machine Learning in Weiden",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von KI Modellen für Vorhersage, Klassifikation und Retrieval. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH mit CatBoost Multi Quantil Regression und strengen Anti Leakage Regeln geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act mit AIF360, SHAP und scikit learn umgesetzt und eine vollständig automatisierte BigQuery Medallion Pipeline mit einem BigQuery ML Klassifikator gebaut. Sicher in Python und Git, mit Erfahrung in XGBoost, scikit learn und modernen Cloud KI Workflows, bin ich die richtige Verstärkung für die AI Applications Abteilung der Witt-Gruppe.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_MOVIE_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für das Praktikum Künstliche Intelligenz und Machine Learning bei der Witt-Gruppe in Weiden mit 50 Prozent Remote Anteil. Die Ausschreibung, das Konzipieren und Auswerten komplexer Datenanalysen auf einer vielfältigen Shop und Datenlandschaft, das End to End Betreuen von Use Cases und das eigenverantwortliche Anwenden moderner KI Technologien in der Google Cloud oder Azure, spiegelt genau die Projekte wider, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See geliefert, sechs Modelle direkt verglichen und CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt. In CreditIQ habe ich mit scikit learn und XGBoost nahen Werkzeugen ein Fairness by Design Klassifikationssystem gebaut, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit einem leakage freien BigQuery ML Klassifikator, der bewusst nur Pre Release Signale nutzt. Mein Hybrider RAG Orchestrator ist ein arbeitsfähiges KI System mit einem Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings, das schult den Blick für State of the Art KI Werkzeuge auf produktiven Daten.",
            "Ich bin im vierten Semester des M.Sc. Data Science and Analytics eingeschrieben, arbeite sicher in Python und Git, kenne Predictive Analytics und Modellbildung und bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Mein aktuelles Deutschniveau ist B1 in Bearbeitung. Sehr gerne unterstütze ich Ihr Team ab Mitte September 2026 im Pflichtpraktikum.",
        ],
    },

    # 4. HELLA — Praktikum im Bereich Data & AI, Lippstadt (German track, posted 15 July)
    {
        "folder": "HELLA Praktikum Data AI",
        "company": "FORVIA HELLA",
        "lang": "de",
        "role_strip": "Praktikant Data und AI",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Praktikum im Bereich Data und AI in Lippstadt",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in datengetriebenen Produkten, Datenaufbereitung, Visualisierung und modernen KI Anwendungsfällen. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit einem fünfseitigen Looker Studio Dashboard und einem BigQuery ML Klassifikator geliefert, ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain und ChromaDB gebaut und eine Random Forest gestützte Business Intelligence Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse veröffentlicht. Sicher in Python und mit Grundkenntnissen in Typescript, mit Erfahrung in Machine Learning, Generative AI und Natural Language Processing, bin ich die richtige Verstärkung für das Business Transformation Studio bei HELLA in Lippstadt.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_RAG_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich für das Praktikum im Bereich Data und AI bei HELLA im Business Transformation Studio in Lippstadt. Die Ausschreibung, die Entwicklung datengetriebener Produkte und moderner KI und Datenlösungen, die Analyse, Aufbereitung und Visualisierung von Daten aus verschiedenen Unternehmensquellen, die Konzeption und Bewertung von Data Analytics und KI Anwendungsfällen sowie die Implementierung und Optimierung von Datenpipelines, deckt sich direkt mit den Projekten, die ich im letzten Jahr geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut, mit Schema Enforcement, Deduplikation per Window Functions und einem leakage freien BigQuery ML Klassifikator, aufgesetzt auf ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen. Diese Pipeline und Reporting Denke überträgt sich direkt auf die datengetriebenen Produkte im FORVIA HELLA Umfeld.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges Generative AI System mit einem eigenen Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore, was direkt zu Ihrem Interesse an Machine Learning, Generative AI und Natural Language Processing passt. In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt und die Ergebnisse in visuellen Reports kommuniziert, die ein Managementpublikum direkt umsetzen kann.",
            "Ich bin im Master Data Science and Analytics eingeschrieben, arbeite sicher in Python und kenne Typescript in Grundzügen, spreche fließend Englisch auf C1 Niveau und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne bespreche ich in einem persönlichen Gespräch, wie ich das Business Transformation Studio unterstützen kann.",
        ],
    },

    # 5. BwFuhrparkService — Werkstudent Controlling & Data Analytics, Siegburg (German track, posted 8 July)
    {
        "folder": "BwFuhrparkService Werkstudent Controlling Data Analytics",
        "company": "BwFuhrparkService",
        "lang": "de",
        "role_strip": "Werkstudent Controlling und Data Analytics",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Werkstudent Controlling und Data Analytics in Siegburg",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Controlling naher Datenarbeit, Reporting und Visualisierung. Ich habe ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerter Analytik geliefert, eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard umgesetzt und eine Random Forest gestützte Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse veröffentlicht. Sicher in Excel, PowerPoint, Python und SQL, mit Grundkenntnissen in Power BI, PowerQuery und PowerPivot, bin ich die richtige Verstärkung für Controlling, kennzahlenorientierte Unternehmenssteuerung und Reporting bei BwFuhrparkService in Siegburg.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_TABLEAU_DE, P_MOVIE_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent Controlling und Data Analytics am Standort Siegburg. Die Ausschreibung, die Aufnahme und Identifikation von Fragestellungen zur Unternehmenssteuerung, die Visualisierung von Erkenntnissen in Power BI und Excel, die Erstellung von Präsentationen für Geschäftsführung und Bereichsleitungen sowie die Konzeption und Erstellung von Proto Typen von Reports in PowerPivot und Excel, deckt sich direkt mit den Projekten, die ich in den letzten Monaten geliefert habe.",
            "In meinem Fast Food Nährwert Analyzer und Meal Simulator habe ich ein zweistufiges Tableau Dashboard aus einer Executive Makro Sicht und einer granularen Detail Sicht entwickelt, mit dynamischen Set Actions, parameter gesteuerten Feldern und komplexen Calculated Fields. Diese Struktur überträgt sich direkt auf ein Reporting Layout für Geschäftsführung und Abteilungsleitungen bei BwFuhrparkService. In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine Bronze Silver Gold Medallion Pipeline gebaut und in einem fünfseitigen Looker Studio Dashboard Business Fragen zu ROI und Timing beantwortet, das entspricht der Reporting Denke, die die Rolle verlangt.",
            "In meiner Wirtschaftlichen Analyse globaler Klimaereignisse habe ich mit Random Forest und statistischer Modellierung rohe Ereignisdaten in strukturierte Business Intelligence überführt und die Ergebnisse in Reports kommuniziert, die auch ein nicht technisches Publikum direkt umsetzen kann. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit Anti Leakage Regeln und einem Orchestrator mit Gate Checks geliefert, das schärft den Blick für belastbare Zahlen im Berichtswesen.",
            "Ich arbeite sehr sicher in Excel, PowerPoint, Python und SQL, kenne Power BI und PowerQuery in Grundzügen und bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations sowie AWS Academy Cloud Foundations mit. Mein aktuelles Deutschniveau ist B1 in Bearbeitung, ich lerne aktiv weiter. Sehr gerne unterstütze ich Ihr Team ab dem gewünschten Startdatum bei Requirements Engineering, Report Prototypen und der Umstellung auf SAP HANA.",
        ],
    },

    # 6. Siemens Mobility — Werkstudent IT Controlling & Data Analytics, Erlangen (German track, posted 7 July)
    {
        "folder": "Siemens Erlangen Werkstudent IT-Controlling Data Analytics",
        "company": "Siemens Mobility",
        "lang": "de",
        "role_strip": "Werkstudent IT Controlling und Data Analytics",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Werkstudent IT Controlling und Data Analytics in Erlangen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau moderner Reporting und Analyse Strukturen. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerter Analytik umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain gebaut. Sicher in Excel, PowerPoint, Python und SQL, mit Grundkenntnissen in Power BI und AI Werkzeugen, bin ich die richtige Verstärkung für das Siemens Mobility IT Controlling bei Ist Analyse, Forecast und Budgeterstellung im internationalen Umfeld.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent im Function Controlling bei Siemens Mobility am Standort Erlangen. Die Ausschreibung, die Unterstützung bei Ist Analyse, Forecast und Budgeterstellung weltweit, die Digitalisierung und Weiterentwicklung der Reporting, Analyse und Verrechnungsstrukturen sowie die Mithilfe bei der Einführung von AI und Data Analytics im IT Controlling, entspricht direkt der Art Arbeit, die ich im letzten Jahr geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold BigQuery Medallion Architektur gebaut, mit einem leakage freien BigQuery ML Klassifikator und einem fünfseitigen Looker Studio Dashboard für konkrete Business Fragen. Diese Denke, saubere Datenpipeline plus klares Reporting Layout, überträgt sich direkt auf die Digitalisierung von Reporting und Verrechnungsstrukturen im Siemens Mobility IT Controlling. In meinem Fast Food Nährwert Analyzer habe ich ein zweistufiges Tableau Dashboard aus Executive Makro Sicht und granularer Detail Sicht mit dynamischen Set Actions und parameter gesteuerten Feldern entwickelt.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System mit einem Decision Making Router über Llama 3.1 8b via Groq und LangChain, ergänzt um HuggingFace MiniLM L6 v2 Embeddings und einen ChromaDB Vektorstore. Diese Erfahrung mit AI in einer realen Pipeline unterstützt die Mithilfe bei der Einführung von AI und Data Analytics im Controlling direkt. Bei eRay GmbH habe ich eine rekursive Zeitreihen Pipeline mit strengen Anti Leakage Regeln geliefert, das schärft den Blick für Reporting Qualität.",
            "Ich arbeite sehr sicher in Excel, PowerPoint und Teams, kenne Power BI und AI Tools in Grundzügen, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstütze ich Frau Hitz und das Team 15 bis 20 Stunden pro Woche ab dem gewünschten Startdatum.",
        ],
    },

    # 7. Craftview Software — Werkstudent People Analytics & AI Reporting 100% remote, Frankfurt (German track, posted 7 July)
    {
        "folder": "Craftview Werkstudent People Analytics AI Reporting Remote",
        "company": "Craftview Software GmbH",
        "lang": "de",
        "role_strip": "Werkstudent People Analytics und AI Reporting",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Werkstudent People Analytics und AI Reporting, 100 Prozent Remote",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von KI gestützten Reporting Prozessen und Data Analytics Werkzeugen. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit fünfseitigem Looker Studio Dashboard geliefert, ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerter Analytik umgesetzt und ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain gebaut. Sicher in Excel, Python und SQL, mit Erfahrung in ChatGPT, Copilot und modernen No und Low Code AI Werkzeugen, bin ich die richtige Verstärkung, um das internationale Personnel Controlling bei Craftview von Grund auf mit aufzubauen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_MOVIE_DE, P_TABLEAU_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_NVIDIA_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent People Analytics und AI Reporting bei Craftview, 100 Prozent Remote innerhalb Deutschlands. Die Mission, KI und Automatisierung in HR Controlling wirklich zu nutzen, Reports und Ad hoc Analysen für Finance, Managementteam und Investoren zu liefern und HR Dashboards in Power BI, Tableau oder Looker aufzubauen, deckt sich sehr direkt mit dem, was ich in den letzten Monaten in der Praxis geliefert habe.",
            "In meiner Movie Analytics und ML Pipeline auf GCP habe ich eine vollständig automatisierte Bronze Silver Gold Medallion Architektur in BigQuery gebaut und ein fünfseitiges Looker Studio Dashboard für konkrete Business Fragen aufgesetzt, mit klarer Datenqualität, Deduplikation und Governance. Diese Struktur überträgt sich direkt auf Headcount, Personalkosten und FTE Reporting im internationalen Personnel Controlling. In meinem Fast Food Nährwert Analyzer habe ich ein Tableau Dashboard mit Set Actions und parameter gesteuerten Feldern gebaut, das nicht technische Nutzer aktiv steuern.",
            "Mein Hybrider RAG Orchestrator ist ein lauffähiges KI System, in dem ein eigener Decision Making Router Nutzerintent klassifiziert und über LangChain und Llama 3.1 8b via Groq dispatched, das ist genau die Denke, mit der AI Vorarbeiten in Reports realistisch werden. Ich nutze aktiv ChatGPT, Claude und Copilot, um wiederkehrende Analyseschritte zu automatisieren, und habe bei eRay GmbH eine rekursive Zeitreihen Pipeline mit Anti Leakage Regeln geliefert, das schärft den Blick für Datenqualität in HR und Finance Reporting.",
            "Ich arbeite sehr sicher in Excel, Python und SQL, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate SAS Certified Specialist Visual Business Analytics, Google Data Analytics Foundations und NVIDIA Building LLM Applications With Prompt Engineering mit. Sehr gerne unterstütze ich Fabian Schulze Wierling und das Team ab sofort 15 bis 20 Stunden pro Woche und übernehme den Greenfield Aufbau des Personnel Controllings.",
        ],
    },

    # 8. Forschungszentrum Jülich — Master Thesis Benchmarking Grid Foundation Models, Jülich (English track, posted 19 June)
    {
        "folder": "Juelich Master Thesis Grid Foundation Models",
        "company": "Forschungszentrum Jülich",
        "lang": "en",
        "role_strip": "Master Thesis Student",
        "cl_date": "20 July 2026",
        "cl_subject": "Master Thesis, Benchmarking and Transferability of Grid Foundation Models for Power Grid Analysis",
        "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning work spanning time series forecasting on real sensor data, rigorous benchmarking across models, and physics aware evaluation. I have shipped a recursive time series pipeline at eRay GmbH forecasting four water quality indicators with anti leakage guarantees, a fairness by design classification system with subgroup benchmarking, and a real time Google Cloud pipeline enriching flight positions against airport, aircraft, and weather sources. Comfortable in Python and PyTorch style workflows, with a working feel for physics informed and graph structured data, I am the right fit for a Master Thesis on benchmarking and transferability of Grid Foundation Models at ICE 1.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_FLIGHT_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am applying for the Master Thesis on Benchmarking and Transferability of Grid Foundation Models for Power Grid Analysis at the Institute of Climate and Energy Systems in Jülich. The brief on designing and evaluating machine learning models for benchmark grids, comparing graph neural networks and physics informed approaches, and assessing transferability to a real campus network is directly the kind of scientific, rigorously benchmarked work I have been shipping.",
            "At eRay GmbH I built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake over a six month collaboration with SRH University. I benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression for asymmetric 80 percent prediction intervals. I enforced strict anti leakage rules and reported the honest finding that some indicators are physically predictable while others are not, that same discipline transfers directly to benchmarking Grid Foundation Models under realistic grid analysis tasks.",
            "In CreditIQ I ran rigorous ML benchmarking with SHAP driven subgroup analysis and per subgroup metrics, cutting the false negative rate from 44 to 16.7 percent while holding accuracy at 75 percent, and backed everything with unit tests at 100 percent branch coverage and a full regulatory write up. In my Real Time Flight Tracking Data Pipeline I processed over 128 thousand records with PySpark on Google Cloud, joining live flight positions with airport, aircraft, and weather data every 30 seconds, which trained my instinct for how graph and geospatial signals interact.",
            "I am proficient in Python with strong analytical and data processing skills, comfortable in PyTorch style workflows, and hold the NVIDIA Building LLM Applications With Prompt Engineering certificate. My English is at C1 level. I would be glad to shape the thesis together with my professor at SRH Heidelberg, start with a preceding mandatory internship phase if that fits the project schedule, and align the exact focus with your team at ICE 1.",
        ],
    },

    # 9. Rheinmetall — Praktikant und Masterarbeit Deep Learning zur Bildverbesserung, Bremen (German track, posted 9 June)
    {
        "folder": "Rheinmetall Praktikum Masterarbeit Deep Learning Bildverbesserung",
        "company": "Rheinmetall Electronics",
        "lang": "de",
        "role_strip": "Praktikant und Masterarbeit Deep Learning",
        "cl_date": "20. Juli 2026",
        "cl_subject": "Praktikant und Masterarbeit Deep Learning zur Bildverbesserung in Bremen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Deep Learning naher Modellierung, Datenpipeline Arbeit und rigoroser Evaluation. Ich habe eine rekursive Zeitreihen Pipeline bei eRay GmbH mit sechs Modellen im Vergleich und CatBoost Multi Quantil Regression geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act mit AIF360 und SHAP umgesetzt sowie eine Echtzeit Pipeline auf Google Cloud betrieben, die über 128 tausend Datensätze verarbeitet. Sicher in Python, mit Erfahrung in PyTorch nahen Workflows und der Fähigkeit, Forschungsarbeiten im Deep Learning zu lesen, zu analysieren und umzusetzen, bin ich die richtige Verstärkung für das Team Deep Learning zur Bildverbesserung am Standort Bremen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Praktikant und für die Masterarbeit im Bereich Deep Learning zur Bildverbesserung am Standort Bremen. Die Ausschreibung, die Unterstützung im Training neuronaler Netze, die Sammlung und Vorverarbeitung von Bilddaten sowie Modell Pruning, Quantisierung und Testen, deckt sich mit den ML Pipelines und Modellevaluationen, die ich in den letzten Monaten in der Praxis geliefert habe.",
            "Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline zur Prognose von vier Wasserqualitätsindikatoren aufgebaut, sechs Modelle direkt verglichen, CatBoost Multi Quantil Regression für asymmetrische 80 Prozent Vorhersageintervalle eingesetzt und strenge Anti Leakage Regeln über die gesamte Pipeline hinweg erzwungen. In CreditIQ habe ich mit AIF360 und SHAP subgruppenweise Metriken berechnet, die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt bei stabiler Genauigkeit von 75 Prozent und die Pipeline mit Unit Tests bei 100 Prozent Branch Coverage abgesichert.",
            "In meiner Echtzeit Flugverfolgungs Pipeline habe ich mit PySpark auf Google Cloud über 128 tausend Datensätze verarbeitet, Live Positionen alle 30 Sekunden gegen vier Datenquellen angereichert und das Gesamtsystem mit Apache Airflow so orchestriert, dass sich Batch und Echtzeit Schichten alle 15 Minuten aktualisieren. Mein Hybrider RAG Orchestrator zeigt die Modellintegrationsseite, ein eigener Decision Making Router über Llama 3.1 8b via Groq mit LangChain und persistentem Vektorspeicher, das schult den Blick für saubere Deep Learning Frameworks in der Praxis.",
            "Ich bin im Master Data Science and Analytics eingeschrieben, arbeite sicher in Python und komfortabel in PyTorch nahen Workflows, spreche fließend Englisch und lerne Deutsch aktiv weiter, aktuell B1 in Bearbeitung. Ich bringe die Zertifikate NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Foundations mit. Sehr gerne bespreche ich mit Frau Behrens die genaue Ausgestaltung des Praktikums und der Masterarbeit.",
        ],
    },
]
