# Rahul Rawat

## Werkstudent Geospatial Data Science

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Geodaten naher Datenanalyse, Cloud Datenpipelines und BI Visualisierung. Ich habe eine Echtzeit Google Cloud Pipeline betrieben, die alle 30 Sekunden Live Flugpositionen ueber Deutschland gegen Flughafen, Flugzeug und Wetterdaten anreichert und ueber 128 tausend Datensaetze verarbeitet, eine BigQuery Medallion Pipeline mit fuenfseitigem Looker Studio Dashboard geliefert und ein interaktives Tableau Dashboard mit Set Actions und parameter gesteuerten Kennzahlen umgesetzt. Sicher in Python, PySpark, SQL, dbt und BI Werkzeugen, bin ich die richtige Verstaerkung fuer das Geospatial Data Science Team bei wemove.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
