# Rahul Rawat

## Werkstudent Computer Vision

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in Machine Learning und bildnaher Datenpipeline Arbeit, von LLM Systemen über Echtzeit Anreicherung bis hin zu strenger Modellbewertung. Ich habe ein modulares Retrieval Augmented Generation System mit eigenem Entscheidungs Router auf Llama 3.1 8b via Groq und HuggingFace MiniLM L6 v2 Embeddings geliefert, ein Fairness by Design Klassifikationssystem nach EU AI Act umgesetzt und eine Echtzeit Pipeline auf Google Cloud betrieben, die Flugpositionen alle 30 Sekunden gegen vier Datenquellen anreichert. Sicher in Python, PyTorch nahen Workflows, scikit learn und strukturierter Evaluation, bin ich die richtige Verstärkung für die Computer Vision Projekte bei CeramTec in Plochingen.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
