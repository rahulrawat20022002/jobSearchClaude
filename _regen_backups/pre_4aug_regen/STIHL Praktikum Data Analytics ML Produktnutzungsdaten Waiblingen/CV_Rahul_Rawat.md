# Rahul Rawat

## Praktikum Data Analytics und Machine Learning fuer Produktnutzungsdaten

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Machine Learning auf realen Sensor und Prozessdaten. Ich habe eine rekursive Zeitreihen Pipeline bei eRay GmbH geliefert, die vier Umweltindikatoren prognostiziert und sechs Modelle direkt vergleicht, eine end to end Batch Pipeline mit BigQuery ML Klassifikator und Bronze Silver Gold Medallion Architektur gebaut und einen Hybrid RAG Orchestrator mit agentischem Routing entwickelt. Sicher in Python, scikit learn, Databricks nahen Tools und AI Agenten, mit klarem Blick fuer Mustererkennung, Klassifikation und statistische Auswertung auf Messdaten.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
