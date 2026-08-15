# Rahul Rawat
Werkstudent Data Science und KI

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

M.Sc.-Student Data Science and Analytics an der SRH University of Applied Sciences Heidelberg mit praktischer Erfahrung im Aufbau von Datenpipelines, prädiktiven Analysemodellen und Cloud-nativer Dateninfrastruktur. Bei eRay GmbH entwickelte ich ein rekursives Prognosesystem für Wasserqualitätsdaten über 40 Merkmale, das vier Zielindikatoren verlässlich abdeckt. Weitere Projekte umfassen eine Cloud-Datenpipeline auf GCP, die über 128 Tausend Echtzeit-Flugbewegungen über Deutschland verarbeitet, sowie ein Analysemodell zur wirtschaftlichen Auswirkung globaler Klimaereignisse mit Entscheidungsunterstützung für das Management. Ich möchte meine Kenntnisse in Python, Machine Learning und Datenengineering in einem industriellen Umfeld bei Phoenix Contact einbringen.

---

## FÄHIGKEITEN

Python, SQL, PySpark, BigQuery, dbt, Apache Airflow, GCP, Dataproc, GCS, Cloud Scheduler, Cloud Run, AWS, scikit-learn, CatBoost, LightGBM, XGBoost, Prophet, MICE, Random Forest, SHAP, Tableau, Looker Studio, Power BI, TabPy, Pandas, NumPy, Matplotlib, Seaborn, Docker, Git

---

## BERUFSERFAHRUNG

**Data Scientist bei eRay GmbH, Heidelberg, Okt 2025 bis März 2026**
*6-monatige Zusammenarbeit mit der SRH University of Applied Sciences Heidelberg*

- Im Rahmen einer 6-monatigen Zusammenarbeit zwischen eRay GmbH und SRH Heidelberg zur Prognose der Wasserqualität eines deutschen Sees über **4** Zielindikatoren, bestand die Aufgabe darin, eine vollständige rekursive Zeitreihenpipeline über **40** Merkmale aufzubauen; entwickelte eine zielspezifische Lag-Sammlung und einen Orchestrator mit ökologischen Gültigkeitsprüfungen; das System verarbeitet alle Zielindikatoren in unter **6** Stunden pro Prognosezyklus.
- Mit **6** Kandidatenmodellen, die auf Sommer-Ausreißer im Testset inkonsistent reagierten, bestand die Aufgabe darin, das robusteste Modell für asymmetrische Unsicherheit in Umweltdaten auszuwählen; testete Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost und Prophet mit strikten Baumparametern; CatBoost MultiQuantile bei Alpha 0.05, 0.5 und 0.85 erzielte asymmetrische Vorhersageintervalle von **80 Prozent**, die den oberen **15 Prozent** der Sommer-Ausreißer abschneiden.
- Mit Lücken in den Herbstdaten, die die Modellintegrität gefährdeten, bestand die Aufgabe in der Datenrekonstruktion; wendete IterativeImputer MICE an, führte die vollständige Memory-Buffer-Neuberechnung über alle **6** Lag-Merkmale durch und erzeugte ein synthetisches Winterbild mit **4** Grad Celsius Grundtemperatur; lieferte eine vollständige 40-Merkmal-Eingabe für die rekursive Prognose.

**Junior Associate Software Developer bei SS Engineers and Contractors, Indien, Aug 2023 bis Aug 2024**

- Bei SS Engineers and Contractors mit internen Data Dashboards, Analytics-Plattformen und Mitarbeiterportalen als tägliche Arbeitsmittel, bestand die Aufgabe darin, die benötigten Frontend-Funktionen zu entwickeln; lieferte React-UI-Komponenten für alle drei internen Produkte, die das gesamte Jahr über täglich genutzt wurden.
- Mit einem Kunden, der eine Legacy-AngularJS-Anwendung in einem bestehenden Module-Federation-Setup betrieb, bestand die Aufgabe darin, die Migration durchzuführen ohne den Betrieb zu unterbrechen; portierte ca. **8** Routen von AngularJS zu React in **4** Monaten inkrementeller Releases ohne Produktionsvorfälle.

**Front End Developer Intern bei SS Engineers and Contractors, Indien, Feb 2023 bis Juli 2023**

- Im 6-monatigen Praktikum bei SS Engineers and Contractors, bestand die Aufgabe darin, nach dem Einarbeiten in den Code eigenständig UI-Komponenten für interne Dashboards zu entwickeln; lieferte Charts, Filter und Profilseiten unter Senior-Review; alle beigesteuerten Komponenten verblieben bis zum Ende des Praktikums im Produktiveinsatz.

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

- Für ein Data-Engineering-Modul an der SRH mit dem Ziel einer Echtzeit-Übersicht über Flugbewegungen über Deutschland, bestand die Aufgabe im Aufbau der Erfassungs- und Anreicherungsschicht; entwickelte Python-Kollektoren, die die OpenSky-Network-API alle **30 Sekunden** abfragen, und eine PySpark-Verarbeitung auf GCP, die Daten aus **4** Quellen zusammenführt und eine saubere Tabelle mit mehr als **128 Tausend** Datensätzen liefert.
- Mit dem Ziel automatischer Datenaktualisierung ohne manuellen Eingriff, bestand die Aufgabe in der Orchestrierung des gesamten Systems; modellierte Daten mit dbt, berechnete Flughafen-Labels mit PySpark und orchestrierte die Pipeline mit Apache Airflow auf GCS und Dataproc, sodass Batch- und Echtzeit-Schichten alle **15 Minuten** automatisch aktualisiert werden.
- Mit dem Ziel, aus den Daten geschäftsrelevante Erkenntnisse zu gewinnen, bestand die Aufgabe im Aufbau der Analyse-Oberfläche; erstellte ein Tableau-Workbook mit Python-Statistiken über TabPy, das zeigt, dass der Luftverkehr bei starkem Regen um das **4,4-fache** zurückgeht.

### Wirtschaftliche Auswirkungsanalyse globaler Klimaereignisse
*Entwickelt mit: Python (Pandas, scikit-learn), Matplotlib, Seaborn, Random Forest*

- Für ein Data-Science-Projekt zur Entscheidungsunterstützung bei Ressourcenallokation und Risikoabschätzung, bestand die Aufgabe darin, eine vollständige Analysepipeline aufzubauen; führte das Projekt von der Rohdaten-Aufnahme bis zum Management-Report als reproduzierbare Einzelpipeline durch.
- Mit Ausreißern, fehlenden Werten und inkonsistenten Skalen in den Rohdaten, bestand die Aufgabe im Aufbau einer sauberen Datenbasis; wendete umfassende Datenaufbereitung mit Ausreißerbereinigung, Imputation und Normalisierung an; die Modellleistung blieb vor und nach der Skalierung stabil.
- Mit nicht-technischen Stakeholdern als Zielgruppe, bestand die Aufgabe in der verständlichen Kommunikation der Ergebnisse; erstellte umfassende visuelle Berichte mit kalibrierten Konfidenzaussagen, die in einer Management-Präsentation ohne weitere Erklärung verstanden wurden.

---

## FORSCHUNG UND ABSCHLUSSARBEIT

### Bachelorarbeit: Diabetesvorhersage mit Machine Learning
*Entwickelt mit: Python, scikit-learn, Pandas, Seaborn, Google Colab*

- Für eine Bachelorarbeit zur Diabetesvorhersage mit einem klinischen Datensatz von **768** Patienten, bestand die Aufgabe darin, einen prüfbaren Modellvergleich zu entwickeln; baute eine vollständige ML-Pipeline mit **6** Klassifikatoren und **10-facher** Kreuzvalidierung; der Modellvergleich bestand die Thesis-Verteidigung.
- Mit biologisch unmöglichen Nullwerten im Quelldatensatz, bestand die Aufgabe in der Datenbereinigung; wendete IQR-basierte Ausreißerbereinigung und korrekte Imputation an; hob den Datensatz von fehlerhaft auf eine saubere Trainingsgrundlage.
- Mit einem Klassenungleichgewicht von **65 zu 35**, das Genauigkeit zu einer irreführenden Kennzahl machte, bestand die Aufgabe in der richtigen Bewertungsmetrik; wechselte zur ROC-AUC als Hauptkennzahl; produzierte einen IEEE-Artikel mit ehrlichem Limitierungsabschnitt, den der Betreuer als publikationsreif akzeptierte.

---

## ZERTIFIKATE

**AWS Academy Graduate: AWS Academy Cloud Foundations** — Ausgestellt 15. Juli 2025
**NVIDIA: Building LLM Applications With Prompt Engineering** — Ausgestellt 12. November 2025

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
