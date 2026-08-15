# Rahul Rawat

## Praktikum und Abschlussarbeit Simulation und Machine Learning in der Robotik

Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und Praxis in Machine Learning Pipelines, Modellvergleich und robuster Bewertung. Ich habe eine rekursive Zeitreihen Pipeline mit sechs verglichenen Modellen und asymmetrischen 80 Prozent Vorhersageintervallen bei eRay GmbH geliefert, ein Fairness by Design Credit Scoring System nach EU AI Act umgesetzt und einen Hybrid RAG Orchestrator mit agentischem Routing ueber Python und LangChain gebaut. Sicher in Python, scikit learn, CatBoost, LightGBM, XGBoost und PyTorch, mit klarem Blick fuer Simulation, Anti Leakage und ehrliche Modellauswertung.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Im Rahmen einer sechsmonatigen Zusammenarbeit zwischen eRay GmbH und SRH Hochschule Heidelberg zur Prognose der Wasserqualität eines deutschen Sees, mit dem Auftrag vier Indikatoren über rollende Horizonte zu prognostizieren, wurde eine end to end rekursive Zeitreihen Pipeline für Chlorophyll a, Trübung, pH Wert und gelösten Sauerstoff aufgebaut, als produktionsreifes Modul geliefert, das der Kunde bei jeder neuen Sensordatenlieferung erneut ausführen kann.
* Angesichts unklarer Modellwahl für die Prognoseaufgabe und der Notwendigkeit, Unsicherheit gegenüber nichttechnischen Stakeholdern verständlich zu machen, wurden sechs Kandidaten direkt verglichen, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet, und die Entscheidung fiel auf CatBoost Multi Quantil Regression, die asymmetrische 80 Prozent Vorhersageintervalle lieferte und dem Kunden Entscheidungsunterstützung unter Unsicherheit ermöglichte.
* Aus der Sorge, dass naive Zeitreihen Splits die Genauigkeit verzerren würden, mit dem Auftrag die Evaluation belastbar zu machen, wurden strenge Anti Leakage Regeln in der gesamten Pipeline erzwungen, was die ehrliche Erkenntnis offenlegte, dass pH Wert und gelöster Sauerstoff physikalisch vorhersagbar sind, während Chlorophyll a und Trübung ohne optische Live Sensorik nicht seriös prognostizierbar sind.
* Bei fehlenden Winter Messwerten und baumbasierten Modellen, die während der rekursiven Vorhersage flach wurden, mit dem Ziel realistische saisonale Muster in den nachgelagerten Prognosen zu erhalten, wurden fehlende Werte mit MICE Imputation rekonstruiert und ein synthetischer Winter Decay Prognose Rahmen entwickelt, was glaubwürdiges Winterverhalten wiederherstellte, ohne Verzerrung in das Trainingsfenster einzubringen.
* Um zu verhindern, dass fehlerhafte Daten sich rekursiv durch den Forecaster fortpflanzen, mit dem Auftrag die Ausführungsschleife zu härten, wurde die Pipeline mit einem Orchestrator mit Gate Checks sowie Geschwindigkeits und ökologischen Grenzen umschlossen, sodass eine fehlgeschlagene Imputation nun den Lauf stoppt, statt Wochen nachgelagerter Vorhersagen zu beschädigen.
