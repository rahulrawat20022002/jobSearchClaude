# Rahul Rawat

## Praktikum Künstliche Intelligenz und Machine Learning

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von KI Modellen für Vorhersage, Klassifikation und Retrieval. Ich habe eine rekursive Zeitreihen Pipeline für vier Wasserqualitätsindikatoren bei eRay GmbH mit CatBoost Multi Quantil Regression und strengen Anti Leakage Regeln geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act mit AIF360, SHAP und scikit learn umgesetzt und eine vollständig automatisierte BigQuery Medallion Pipeline mit einem BigQuery ML Klassifikator gebaut. Sicher in Python und Git, mit Erfahrung in XGBoost, scikit learn und modernen Cloud KI Workflows, bin ich die richtige Verstärkung für die AI Applications Abteilung der Witt-Gruppe.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
