# Rahul Rawat

## Praktikant Data und AI

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in datengetriebenen Produkten, Datenaufbereitung, Visualisierung und modernen KI Anwendungsfällen. Ich habe eine vollständig automatisierte BigQuery Medallion Pipeline mit einem fünfseitigen Looker Studio Dashboard und einem BigQuery ML Klassifikator geliefert, ein modulares Retrieval Augmented Generation System auf Llama 3.1 8b via Groq mit LangChain und ChromaDB gebaut und eine Random Forest gestützte Business Intelligence Studie zu wirtschaftlichen Auswirkungen globaler Ereignisse veröffentlicht. Sicher in Python und mit Grundkenntnissen in Typescript, mit Erfahrung in Machine Learning, Generative AI und Natural Language Processing, bin ich die richtige Verstärkung für das Business Transformation Studio bei HELLA in Lippstadt.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
