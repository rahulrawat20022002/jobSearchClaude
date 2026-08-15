# Rahul Rawat

## Werkstudent Process und Data Science

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Process nahen Datenpipelines, Machine Learning auf Betriebsdaten und Dashboarding fuer Entscheidungstraeger. Ich habe eine vollstaendig automatisierte Bronze Silver Gold Medallion Pipeline in BigQuery mit einem leakage freien BigQuery ML Klassifikator und fuenfseitigem Looker Studio Dashboard umgesetzt, ein interaktives Tableau Dashboard mit dynamischen Set Actions und parametergesteuerten Analytiken ausgeliefert und eine Echtzeit Cloud Pipeline mit PySpark, dbt und Apache Airflow ueber mehr als 128 tausend Datensaetze betrieben. Sicher in Python, SQL und mit strukturiertem analytischem Blick fuer Prozessdaten und Business Fragen, bin ich die richtige Verstaerkung fuer Process und Data Science, Business Process Management und AI Themen bei der PMMG Group.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
