# Rahul Rawat
Werkstudent Data Science und Process Mining

---

## PERSÖNLICHE DATEN

| | |
|---|---|
| **Adresse** | C2 16, 68159 Mannheim, Deutschland |
| **Telefon** | 015563603340 |
| **E-Mail** | rahulrawat2r@gmail.com |
| **LinkedIn** | linkedin.com/in/rahulrawat2r |
| **GitHub** | github.com/rahulrawat20022002 |
| **Portfolio** | rah-portfolio.pages.dev |
| **Geburtsdatum** | 20. Februar 2002 |
| **Nationalität** | Indisch, Studentenvisum mit gültiger Arbeitserlaubnis |
| **Verfügbarkeit** | Werkstudent 20 Stunden pro Woche ab sofort, Vollzeit ab April 2027 |

---

## PROFIL

M.Sc.-Student Data Science and Analytics an der SRH University of Applied Sciences Heidelberg mit praktischer Erfahrung in Python-basierter Datenanalyse, Prozessautomatisierung, Datenpipelines und maschinellem Lernen. Bei eRay GmbH entwickelte ich eine vollständige rekursive Prognosepipeline auf Basis realer Sensordaten. Weitere Projekte umfassen eine Cloud-Datenpipeline auf GCP mit automatisierter Orchestrierung über Apache Airflow sowie eine wirtschaftliche Auswirkungsanalyse globaler Klimaereignisse als vollständig reproduzierbare Analysepipeline. Ich möchte meine Kenntnisse in Datenanalyse, Python und Prozessauswertung bei viadee einbringen und freue mich auf die Arbeit mit ERP- und Produktionssteuerungsdaten.

---

## FÄHIGKEITEN

Python, SQL, R, PySpark, BigQuery, dbt, Apache Airflow, GCP, Dataproc, GCS, AWS, scikit-learn, CatBoost, LightGBM, XGBoost, Random Forest, MICE, SHAP, Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI, BPMN, Docker, Git

---

## BERUFSERFAHRUNG

**Data Scientist bei eRay GmbH, Heidelberg, Okt 2025 bis März 2026**
*6-monatige Zusammenarbeit mit der SRH University of Applied Sciences Heidelberg*

- Im Rahmen einer 6-monatigen Zusammenarbeit zwischen eRay GmbH und SRH Heidelberg zur Prognose der Wasserqualität eines deutschen Sees über **4** Zielindikatoren, bestand die Aufgabe darin, eine vollständige rekursive Zeitreihenpipeline über **40** Merkmale aufzubauen; entwickelte eine zielspezifische Lag-Sammlung und einen Orchestrator mit Datenqualitätsprüfungen; das System verarbeitet alle Zielindikatoren in unter **6** Stunden pro Prognosezyklus.
- Mit **6** Kandidatenmodellen und inkonsistentem Verhalten auf Ausreißer im Testset, bestand die Aufgabe darin, das zuverlässigste Modell auszuwählen; testete Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet mit strikten Baumparametern; CatBoost MultiQuantile erzielte asymmetrische Vorhersageintervalle von **80 Prozent** mit ehrlichem R-Quadrat von **0.86** bei gelöstem Sauerstoff und **0.81** beim pH-Wert.
- Mit Datenlücken in den Herbstmonaten, die die Modellintegrität gefährdeten, bestand die Aufgabe in der Datenrekonstruktion; wendete IterativeImputer MICE an und führte die vollständige Memory-Buffer-Neuberechnung über alle **6** Lag-Merkmale durch; lieferte eine vollständige, bereinigte Eingabe für die rekursive Prognose.

**Junior Associate Software Developer bei SS Engineers and Contractors, Indien, Aug 2023 bis Aug 2024**

- Bei SS Engineers and Contractors mit internen Data Dashboards, Analytics-Plattformen und Mitarbeiterportalen, bestand die Aufgabe darin, die benötigten Frontend-Funktionen zu liefern; entwickelte React-UI-Komponenten für alle drei internen Produkte, die täglich von internen Teams genutzt wurden.
- Mit einer Legacy-AngularJS-Migration in einem bestehenden Module-Federation-Setup, bestand die Aufgabe darin, die Migration ohne Produktionsunterbrechung durchzuführen; portierte ca. **8** Routen von AngularJS zu React in **4** Monaten inkrementeller Releases ohne Vorfälle.

**Front End Developer Intern bei SS Engineers and Contractors, Indien, Feb 2023 bis Juli 2023**

- Im 6-monatigen Praktikum, bestand die Aufgabe darin, UI-Komponenten für interne Dashboards unter Senior-Review zu entwickeln; lieferte Charts, Filter und Profilseiten nach Code-Review-Feedback; alle beigesteuerten Komponenten verblieben bis zum Ende des Praktikums im Produktiveinsatz.

---

## AUSBILDUNG

**M.Sc. Data Science and Analytics, Apr 2025 bis heute**
SRH University of Applied Sciences Heidelberg, GPA 1.9

**Bachelor of Technology in Computer Science, 2019 bis 2023**
GL Bajaj Institute of Technology and Management, CGPA 7.3 von 10

---

## PERSÖNLICHE PROJEKTE

### Real-Time Flight Tracking Datenpipeline
*Entwickelt mit: Python, PySpark, BigQuery, dbt, Apache Airflow, GCP (Dataproc, GCE, GCS), Tableau, TabPy, OAuth2*

- Für ein Data-Engineering-Modul an der SRH mit dem Ziel einer Echtzeit-Übersicht über Flugbewegungen über Deutschland, bestand die Aufgabe im Aufbau der Erfassungs- und Anreicherungsschicht; entwickelte Python-Kollektoren, die die OpenSky-Network-API alle **30 Sekunden** abfragen, und eine PySpark-Verarbeitung auf GCP, die Daten aus **4** Quellen zusammenführt; erzeugte eine saubere Tabelle mit mehr als **128 Tausend** Datensätzen.
- Mit dem Ziel automatischer Aktualisierung ohne manuellen Eingriff, bestand die Aufgabe in der Orchestrierung; modellierte Daten mit dbt, berechnete nächste-Flughafen-Labels mit PySpark und orchestrierte die Pipeline mit Apache Airflow auf GCS und Dataproc; Batch- und Echtzeit-Schichten werden alle **15 Minuten** automatisch aktualisiert.
- Mit dem Ziel geschäftsrelevanter Erkenntnisse aus den Daten, bestand die Aufgabe im Aufbau der Analyse-Oberfläche; erstellte ein Tableau-Workbook mit Python-Statistiken über TabPy, das belegt, dass der Luftverkehr bei starkem Regen um das **4,4-fache** zurückgeht.

### Wirtschaftliche Auswirkungsanalyse globaler Klimaereignisse
*Entwickelt mit: Python (Pandas, scikit-learn), Matplotlib, Seaborn, Random Forest*

- Für ein Data-Science-Projekt zur Analyse wirtschaftlicher Risiken durch globale Klimaereignisse, bestand die Aufgabe im Aufbau einer vollständigen Analysepipeline; führte das Projekt von der Rohdatenaufnahme bis zum Management-Report als reproduzierbare Einzelpipeline durch.
- Mit Ausreißern, fehlenden Werten und inkonsistenten Skalen in den Rohdaten, bestand die Aufgabe in der Datenaufbereitung; wendete umfassende Bereinigung mit Ausreißerkorrektur, Imputation und Normalisierung an; die Modellleistung blieb vor und nach der Skalierung stabil.
- Mit nicht-technischen Stakeholdern als Zielgruppe, bestand die Aufgabe in der verständlichen Kommunikation; entwickelte Random-Forest-Modelle mit Feature-Importance-Analyse und erstellte visuelle Berichte, die ohne weitere Erläuterung in einer Management-Präsentation verstanden wurden.

---

## FORSCHUNG UND ABSCHLUSSARBEIT

### Bachelorarbeit: Diabetesvorhersage mit Machine Learning
*Entwickelt mit: Python, scikit-learn, Pandas, Seaborn, Google Colab*

- Für eine Bachelorarbeit zur Diabetesvorhersage mit einem klinischen Datensatz von **768** Patienten, bestand die Aufgabe darin, einen prüfbaren Modellvergleich zu erstellen; baute eine vollständige ML-Pipeline mit **6** Klassifikatoren und **10-facher** Kreuzvalidierung auf; der Vergleich bestand die Thesis-Verteidigung.
- Mit biologisch unmöglichen Nullwerten im Quelldatensatz, bestand die Aufgabe in der Datenbereinigung vor dem Modelltraining; wendete IQR-basierte Ausreißerbereinigung und Imputation an; hob den Datensatz auf ein sauberes Trainingsniveau.
- Mit einem Klassenungleichgewicht von **65 zu 35**, das Genauigkeit als irreführende Kennzahl entlarvte, bestand die Aufgabe in der richtigen Bewertung; wechselte zur ROC-AUC als Hauptkennzahl und produzierte einen IEEE-Artikel, den der Betreuer als publikationsreif akzeptierte.

---

## ZERTIFIKATE

**AWS Academy Graduate: AWS Academy Cloud Foundations** — Ausgestellt 15. Juli 2025
**SAS Certified Specialist: Visual Business Analytics Using SAS Viya** — Ausgestellt 7. Mai 2025

---

## AUSZEICHNUNGEN

**USAII Global AI Hackathon 2026, Finalist auf Graduate-Ebene** — Ausgezeichnet vom United States Artificial Intelligence Institute für das Erreichen der Finalrunde durch Innovation, technische Kreativität und angewandte KI auf realen Herausforderungen.

---

## SPRACHEN

| Sprache | Niveau |
|---|---|
| Englisch | Fließend, schriftlich und mündlich |
| Deutsch | B1 laufend Richtung B2 |
| Hindi | Muttersprache |
