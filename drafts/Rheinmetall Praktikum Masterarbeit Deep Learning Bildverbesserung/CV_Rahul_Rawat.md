# Rahul Rawat

## Praktikant und Masterarbeit Deep Learning

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Deep Learning naher Modellierung, Datenpipeline Arbeit und rigoroser Evaluation. Ich habe eine rekursive Zeitreihen Pipeline bei eRay GmbH mit sechs Modellen im Vergleich und CatBoost Multi Quantil Regression geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act mit AIF360 und SHAP umgesetzt sowie eine Echtzeit Pipeline auf Google Cloud betrieben, die über 128 tausend Datensätze verarbeitet. Sicher in Python, mit Erfahrung in PyTorch nahen Workflows und der Fähigkeit, Forschungsarbeiten im Deep Learning zu lesen, zu analysieren und umzusetzen, bin ich die richtige Verstärkung für das Team Deep Learning zur Bildverbesserung am Standort Bremen.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
