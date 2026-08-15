# Rahul Rawat

## Data Engineer und Analyst Werkstudent

Master Student der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Datenpipelines. Ich habe eine PySpark und dbt gestützte Echtzeit Pipeline für über 128 tausend Flugpositionen auf Google Cloud betrieben, eine Bronze Silver Gold Medallion Architektur auf BigQuery mit BigQuery ML Klassifikator ausgeliefert und ein modulares Retrieval Augmented Generation System mit LangChain und Llama 3.1 8b via Groq umgesetzt. Sicher in Python und PySpark sowie mit einem Grundverständnis von Databricks nahen Plattformen und Large Language Models, bin ich die richtige Verstärkung für Data Engineering und Data Analysis auf der Palantir Foundry Plattform.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
