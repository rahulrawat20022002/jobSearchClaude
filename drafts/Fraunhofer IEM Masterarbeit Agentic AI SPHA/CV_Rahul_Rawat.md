# Rahul Rawat

## Masterarbeit Agentic AI und Software Health Monitoring

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau agentischer LLM Systeme, rigoroser Modellbewertung und produktionsnaher Datenpipelines. Ich habe ein modulares Retrieval Augmented Generation System mit einem eigenen Decision Making Router auf Llama 3.1 8b via Groq und LangChain gebaut, ein Fairness by Design Klassifikationssystem nach EU AI Act mit Unit Tests bei 100 Prozent Branch Coverage geliefert und bei eRay GmbH eine end to end Zeitreihen Pipeline mit sechs verglichenen Modellen und strengen Anti Leakage Regeln umgesetzt. Sicher in Python, agiler Softwareentwicklung, LLM und Machine Learning Workflows, bin ich die richtige Verstaerkung fuer den naechsten Ausbaustand des Software Product Health Assistant am Fraunhofer IEM.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Entwickelte eine end to end rekursive Zeitreihen Pipeline zur Prognose von Chlorophyll a, Trübung, pH Wert und gelöstem Sauerstoff für einen deutschen See, umgesetzt als sechsmonatige Zusammenarbeit mit der SRH Hochschule Heidelberg.
* Verglich sechs Modelle direkt, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und nutzte CatBoost Multi Quantil Regression, um asymmetrische 80 Prozent Vorhersageintervalle für die Entscheidungsunterstützung unter Unsicherheit zu liefern.
* Erzwang strenge Anti Leakage Regeln in der gesamten Pipeline und legte die ehrliche Erkenntnis offen, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Rekonstruierte fehlende Winter Messwerte mit MICE Imputation und entwickelte einen synthetischen Winter Decay Prognose Rahmen, damit baumbasierte Modelle während der rekursiven Vorhersage nicht flach werden.
* Umschloss die gesamte Pipeline mit einem Orchestrator, der Gate Checks sowie Geschwindigkeits und ökologische Grenzen prüft und bei fehlgeschlagener Imputation stoppt, statt schlechte Daten weiterfließen zu lassen.
