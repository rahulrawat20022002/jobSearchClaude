# Rahul Rawat

## Werkstudent Data Engineering

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau produktionsreifer Datenpipelines, Cloud ETL und BI Reporting. Ich habe eine Echtzeit Google Cloud Pipeline betrieben, die alle 30 Sekunden Live Flugpositionen ueber Deutschland gegen Flughafen, Flugzeug und Wetterdaten anreichert und ueber 128 tausend Datensaetze verarbeitet, eine vollstaendig automatisierte BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert und ein interaktives Tableau Dashboard mit dynamischen Set Actions und parameter gesteuerten Kennzahlen umgesetzt. Sicher in Python, PySpark, SQL, dbt, Apache Airflow und modernen Cloud Umgebungen, bin ich die richtige Verstaerkung fuer das Data und Technology Team bei Mediaplus.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
