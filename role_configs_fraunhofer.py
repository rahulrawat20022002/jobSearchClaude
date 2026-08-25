"""Role configurations for 5 Fraunhofer thesis listings Rah asked to be
tailored on 25 August 2026, ad hoc (outside the scheduled daily run).

Sources: all 5 are jobs.fraunhofer.de postings, fetched in full via Tavily
extract on 25 Aug 2026.

Honesty note (invariant 3, never fabricate): of the 5, 2 are strong fits
for a Data Science and Analytics profile (Aachen DL/ML in production,
Karlsruhe training data anonymization, Darmstadt age estimation loss
design are the 3 strong fits), and 2 are genuine domain mismatches:
  - Stuttgart Binder Jetting 3D print process development (Fraunhofer IPA)
    wants materials science / process engineering / additive manufacturing
    lab experience. Rah has none. The cover letter is honest about this,
    leaning on real transferable skills (structured experimentation,
    parameter optimisation from ML work, careful documentation) rather
    than inventing lab or materials science background.
  - Stuttgart ATMP evaluation matrix for space production (Fraunhofer IPA
    Pharma und Bioproduktionstechnik) explicitly wants Biotechnologie,
    Bioprozesstechnik, Pharmatechnik, Medizintechnik or Verfahrenstechnik
    students. Rah has none of these. Weakest fit of the 5; cover letter
    is honest about approaching from a data and analytics background.

Language track: all 5 postings are written in German -> DE track for all.

All 5 use the 19 August 2026 CV content rules (no hyphens/dashes in CV
body text, no parentheses in bullets, tag field, Ojas style header). The
official Fraunhofer institute names (which contain a hyphen, e.g.
"Fraunhofer-Institut fuer Produktionstechnologie IPT") are proper names
used in the cover letter addressee block only, the same exception already
used for hyphenated real company names elsewhere in this repo.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_FLIGHT_DE,
    P_MOVIE_DE,
    P_CLIMATE_DE,
)


CONFIGS_FRAUNHOFER = [
    # 1. Fraunhofer-Institut fuer Produktionstechnologie IPT, Aachen
    # Bachelor/Masterarbeit: Deep Learning und Machine Learning in der Produktion
    # Kennziffer 8382, posted 16.08.2026. Strong fit: DL/ML pipelines over
    # tabular and image production data, compared against classical methods.
    # Apply: https://jobs.fraunhofer.de/talentcommunity/apply/766751001/?locale=de_DE
    {
        "folder": "Fraunhofer IPT Aachen Masterarbeit Deep Learning Machine Learning Produktion",
        "company": "Fraunhofer-Institut fuer Produktionstechnologie IPT",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | ML Pipelines fuer Produktionsdaten | Python + scikit learn + CatBoost",
        "role_strip": "Masterarbeit Deep Learning und Machine Learning in der Produktion",
        "cl_date": "25. August 2026",
        "cl_subject": "Bachelor oder Masterarbeit Deep Learning und Machine Learning in der Produktion, Kennziffer 8382",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von ML Pipelines fuer tabulare und Bilddaten sowie im belastbaren Vergleich moderner Verfahren gegen klassische Datenanalyse. Ich habe in meiner Bachelorarbeit sechs Klassifikatoren gegeneinander mit 10 facher Kreuzvalidierung verglichen und in eigenen Projekten End to End Pipelines von Rohdaten bis zum produktionsreifen Modell gebaut. Sicher in Python, scikit learn, CatBoost, Pandas und in der Validierung und Dokumentation von Modellergebnissen fuer produktionsnahe Anwendungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Bachelor oder Masterarbeit Deep Learning und Machine Learning in der Produktion unter der Kennziffer 8382 am Fraunhofer IPT in Aachen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Aufgabe, fuer reale Produktionsanwendungen DL und ML Pipelines auf tabularen und Bilddaten zu bauen und gegen klassische Datenanalyse zu vergleichen, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme entwickelt habe.",
            "In meiner Bachelorarbeit zur Diabetesvorhersage habe ich sechs Klassifikatoren mit 10 facher Kreuzvalidierung und pro Modell erstellten Konfusionsmatrizen verglichen und bei einer 65 zu 35 Klassenungleichgewicht Verteilung die Leitmetrik bewusst von Genauigkeit auf ROC AUC umgestellt, um die realen Fehlermuster nicht zu verdecken. Genau diese Faehigkeit, mehrere Modellierungsansaetze fair gegeneinander zu vergleichen und die Wahl der Metrik kritisch zu hinterfragen, deckt sich mit dem in der Ausschreibung geforderten Vergleich von DL und ML basierten Methoden mit klassischer Datenanalyse.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten aus vier Quellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt und die Daten mit dbt in analysebereite Tabellen geformt. In CreditIQ habe ich einen realen Kreditdatensatz aufbereitet, ein Modell trainiert und den Disparate Impact von 0,79 auf 0,88 gehoben. Beide Projekte zeigen die gleiche Herangehensweise, die die Ausschreibung fuer die Produktion braucht: Rohdaten in Zusammenarbeit mit Fachexperten aufbereiten, Modelle implementieren und die Ergebnisse sauber validieren und dokumentieren.",
            "Ich arbeite sicher in Python, scikit learn, CatBoost, Pandas und SQL und habe Eigenmotivation, mich in neue Themenfelder wie Bild und tabulare Produktionsdaten einzuarbeiten. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Gerne bespreche ich das Thema in einem persoenlichen Gespraech mit Herrn Hemmerich.",
        ],
    },

    # 2. Fraunhofer-Institut fuer Produktionstechnik und Automatisierung IPA, Stuttgart
    # Studien/Abschlussarbeit: Prozessentwicklung fuer nachhaltigen Binder Jetting 3D Druck
    # Kennziffer 85106, posted 20.08.2026. WEAK FIT: wants materials science /
    # additive manufacturing lab experience Rah does not have. Honest, modest
    # letter leaning on transferable structured experimentation from ML work.
    # Apply: https://jobs.fraunhofer.de/talentcommunity/apply/1417868133/?locale=de_DE
    {
        "folder": "Fraunhofer IPA Stuttgart Abschlussarbeit Binder Jetting 3D Druck",
        "company": "Fraunhofer-Institut fuer Produktionstechnik und Automatisierung IPA",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Strukturierte Experimente und Parameteroptimierung | Python + Datenanalyse",
        "role_strip": "Studien oder Abschlussarbeit Prozessentwicklung fuer nachhaltigen Binder Jetting 3D Druck",
        "cl_date": "25. August 2026",
        "cl_subject": "Studien oder Abschlussarbeit Prozessentwicklung fuer nachhaltigen Binder Jetting 3D Druck, Kennziffer 85106",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim mit einem quantitativen, datengetriebenen Hintergrund statt einer Materialwissenschaft oder additiven Fertigung Ausbildung. Ich bringe strukturiertes Experimentieren und Parameteroptimierung aus eigenen Machine Learning Projekten mit, in denen ich systematisch verschiedene Modellkonfigurationen verglichen, Schwellenwerte kalibriert und Ergebnisse sauber dokumentiert habe. Sicher in Python, in der statistischen Auswertung von Messreihen und in einer selbststaendigen, strukturierten Arbeitsweise.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CLIMATE_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit moechte ich mein Interesse an der Studien oder Abschlussarbeit Prozessentwicklung fuer nachhaltigen Binder Jetting 3D Druck unter der Kennziffer 85106 am Fraunhofer IPA in Stuttgart zum Ausdruck bringen. Ich bin ehrlich, dass mein bisheriger Hintergrund als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim kein klassisches Materialwissenschaft oder additive Fertigung Studium ist, doch die in der Ausschreibung beschriebene Aufgabe, Prozessparameter systematisch zu untersuchen und den Druckprozess ueber Versuche zu optimieren, spricht meine Staerken in strukturiertem Experimentieren und quantitativer Auswertung direkt an.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich rohe Messdaten bereinigt, Ausreisser und inkonsistente Skalen behandelt und Random Forest Modelle systematisch gegen mehrere Parametrisierungen getestet, was stabile Ergebnisse vor und nach dem Feature Scaling ergab. In CreditIQ habe ich eine vierstufige Schwellenwertmatrix ueber Alter und Geschlecht entworfen und deren Effekt kontrolliert gemessen, bevor ich mich fuer die finale Kalibrierung entschieden habe. Beide Projekte zeigen die gleiche Denkweise, die Dropwatching Versuche und die Ermittlung stabiler Druckprozessparameter brauchen: Parameter systematisch variieren, Ergebnisse messen und die beste Konfiguration datenbasiert auswaehlen.",
            "Mir ist bewusst, dass mir praktische Laborerfahrung mit Pulver und Bindersystemen fehlt, und ich moechte das nicht kleinreden. Was ich mitbringe ist Eigeninitiative, eine schnelle Einarbeitung in neue Themenfelder und die Faehigkeit, aus Versuchsreihen belastbare, dokumentierte Schlussfolgerungen zu ziehen, so wie ich es in meiner Bachelorarbeit mit sechs verglichenen Klassifikatoren und einer kritischen Metrikwahl bei starkem Klassenungleichgewicht demonstriert habe.",
            "Ich arbeite sicher in Python und in der statistischen Auswertung von Datenreihen, halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, Englisch spreche ich fliessend. Gerne bespreche ich in einem persoenlichen Gespraech mit Frau Leppich, ob mein Profil trotz des fachfremden Hintergrunds zu Ihrem Team passt.",
        ],
    },

    # 3. Fraunhofer-Institut fuer Produktionstechnik und Automatisierung IPA,
    # Abteilung Pharma und Bioproduktionstechnik, Stuttgart
    # Abschlussarbeit: Entwicklung einer Bewertungsmatrix fuer eine modulare
    # On Demand Produktion von missionsrelevanten ATMP fuer den Weltraum,
    # in Kooperation mit ESA. Posted 14.08.2026. WEAKEST FIT of the 5: wants
    # Biotechnologie, Bioprozesstechnik, Pharmatechnik, Medizintechnik or
    # Verfahrenstechnik students. Rah has none of these. Honest letter.
    # Apply: https://jobs.fraunhofer.de/talentcommunity/apply/1426470533/?locale=de_DE
    {
        "folder": "Fraunhofer IPA Stuttgart Abschlussarbeit Bewertungsmatrix ATMP Weltraum",
        "company": "Fraunhofer-Institut fuer Produktionstechnik und Automatisierung IPA",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Strukturierte Bewertungsmatrizen und Entscheidungsgrundlagen | Python + Datenanalyse",
        "role_strip": "Abschlussarbeit Bewertungsmatrix fuer eine modulare On Demand Produktion von ATMP im Weltraum",
        "cl_date": "25. August 2026",
        "cl_subject": "Abschlussarbeit Entwicklung einer Bewertungsmatrix fuer eine modulare On Demand Produktion von missionsrelevanten ATMP",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim mit einem quantitativen Hintergrund in Datenanalyse und regulatorisch belastbarer Bewertungslogik statt einer Biotechnologie oder Pharmatechnik Ausbildung. Ich habe in eigenen Projekten strukturierte Bewertungsrahmen entworfen, die technische, regulatorische und Fairness Kriterien systematisch gegeneinander abwaegen und in einer transparenten Entscheidungsgrundlage muenden. Sicher in Python, in der Aufbereitung komplexer Kriterien zu einer nachvollziehbaren Bewertungsmatrix und im regulatorisch sauberen Dokumentieren von Ergebnissen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit moechte ich mein Interesse an der Abschlussarbeit Entwicklung einer Bewertungsmatrix fuer eine modulare On Demand Produktion von missionsrelevanten ATMP am Fraunhofer IPA in Stuttgart zum Ausdruck bringen. Mein Studium der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim ist kein Biotechnologie, Bioprozesstechnik, Pharmatechnik, Medizintechnik oder Verfahrenstechnik Studium, wie in der Ausschreibung gesucht, und ich moechte das offen ansprechen. Die in der Arbeit beschriebene Aufgabe, eine strukturierte Bewertungsmatrix mit Gap Analyse und Risikobewertung ueber technische, regulatorische, logistische und medizinische Kriterien zu entwickeln, spricht jedoch genau meine Staerke im Bau nachvollziehbarer, regulatorisch belastbarer Entscheidungsgrundlagen an.",
            "In CreditIQ habe ich unter EU AI Act und AGG Vorgaben ein Kredit Scoring System entwickelt, mit SHAP getriebener Subgruppenanalyse eine versteckte Verzerrung aufgedeckt und ueber eine vierstufige Schwellenwertmatrix korrigiert, dazu den Fairness Accuracy Trade off als bewusste, regulatorisch belastbare Entscheidung mit einer vollstaendigen Dokumentation nach GDPR Artikel 22 und EU AI Act Artikel 14 festgehalten. Diese Faehigkeit, mehrere Kriterien in eine transparente, pruefbare Bewertungslogik zu ueberfuehren, ist strukturell das, was die Ausschreibung fuer die Priorisierung von ATMP Kandidaten fuer den Einsatz im Weltraum beschreibt, auch wenn die fachliche Domaene bei mir eine andere ist.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich ein end to end Projekt von der Roh CSV bis zum management fertigen Report mit kalibrierten Konfidenzaussagen gefuehrt, das einer Management Review ohne weitere Uebersetzung standhielt. Ich bin mir bewusst, dass mir die fachliche Tiefe in Zell und Gentherapien fehlt, moechte aber betonen, dass ich mich schnell und eigenstaendig in neue, komplexe Themenfelder einarbeite, wie meine bisherigen Projekte ueber sehr unterschiedliche Domaenen hinweg zeigen.",
            "Ich arbeite sicher in Python und in der strukturierten Aufbereitung komplexer Kriterien, halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, Englisch spreche ich fliessend. Gerne bespreche ich in einem persoenlichen Gespraech mit Frau Schaefer offen, ob mein fachfremder aber methodisch passender Hintergrund fuer Ihr Team infrage kommt.",
        ],
    },

    # 4. Fraunhofer-Institut fuer Optronik, Systemtechnik und Bildauswertung IOSB, Karlsruhe
    # Abschlussarbeit: Training Data Anonymization for Object Detection and
    # Human Pose Estimation. Kennziffer 85446, posted 24.08.2026, deadline
    # 11.09.2026, ideal start October 2026, onsite only in Karlsruhe (kein
    # mobiles Arbeiten). Strong fit: Python, ML/DL, computer vision, privacy.
    # Apply: https://jobs.fraunhofer.de/talentcommunity/apply/1429164233/?locale=de_DE
    {
        "folder": "Fraunhofer IOSB Karlsruhe Abschlussarbeit Training Data Anonymization",
        "company": "Fraunhofer-Institut fuer Optronik, Systemtechnik und Bildauswertung IOSB",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Privacy bewusste ML Pipelines und Evaluation | Python + LangGraph + scikit learn",
        "role_strip": "Abschlussarbeit Training Data Anonymization for Object Detection and Pose Estimation",
        "cl_date": "25. August 2026",
        "cl_subject": "Abschlussarbeit Training Data Anonymization for Object Detection and Human Pose Estimation, Kennziffer 85446",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Machine Learning, Datenschutz und rigoroser Modellevaluation. Ich habe ein Multi Agent RAG System mit einem eigenen Evaluationsrahmen gebaut, der Retrieval und Generation Metriken pro Sprache aufschluesselt, und in CreditIQ Fairness und Datenschutz Anforderungen unter EU AI Act und GDPR direkt in die Modellentwicklung eingebaut. Sicher in Python, Machine Learning Grundlagen und im systematischen Vergleich verschiedener Verfahren gegen eine gemeinsame Metrik.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Abschlussarbeit Training Data Anonymization for Object Detection and Human Pose Estimation unter der Kennziffer 85446 am Fraunhofer IOSB in Karlsruhe, mit dem Wunsch ab Oktober 2026 vor Ort zu starten. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Schnittstelle von Computer Vision, Kuenstlicher Intelligenz und Datenschutz, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, in denen Datenschutz und Fairness kein nachtraeglicher Zusatz sind, sondern von Anfang an Teil der Pipeline.",
            "In CreditIQ habe ich unter EU AI Act und AGG Vorgaben ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, dabei den Fairness Accuracy Trade off als bewusste, regulatorisch belastbare Entscheidung dokumentiert. Genau diese Faehigkeit, den Effekt einer Datenschutz oder Fairness Massnahme auf die Modellleistung sauber zu messen und den Trade off transparent zu machen, deckt sich mit der in der Ausschreibung beschriebenen Aufgabe, den Einfluss verschiedener Anonymisierungsstufen auf die Performance von Object Detection und Pose Estimation zu analysieren.",
            "In meinem Multi Agent RAG Projekt habe ich einen EvalAgent gebaut, der 5 Retrieval Metriken neben 4 Generation Metriken aggregiert und pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set ausgibt, mit einem Judge Modell, das bewusst getrennt vom Generator laeuft, um Self Preference Bias zu vermeiden. Diese Erfahrung im Aufbau eines rigorosen, wiederholbaren Evaluationsrahmens fuer mehrere Modellvarianten laesst sich direkt auf den Vergleich verschiedener Anonymisierungsverfahren und deren Einfluss auf die Modellperformance uebertragen.",
            "Ich arbeite sicher in Python, in Machine Learning Grundlagen und im Trainieren neuronaler Netze, habe erste Beruehrung mit Computer Vision Aufgaben und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, Englisch spreche ich fliessend. Ich kann die Arbeit ausschliesslich vor Ort in Karlsruhe ab Oktober 2026 antreten. Gerne bespreche ich das Thema in einem persoenlichen Gespraech mit Herrn Dr. Cormier.",
        ],
    },

    # 5. Fraunhofer-Institut fuer Sichere Informationstechnologie SIT, Darmstadt
    # Masterarbeit: Modellierungsansaetze und Loss Design fuer praezise
    # Altersschaetzung. Kennziffer 82686, posted 21.08.2026. Strong fit: loss
    # function design, class imbalance, ordinal regression, critical
    # evaluation of metrics, directly mirrors the Diabetes thesis and CreditIQ.
    # Apply: https://jobs.fraunhofer.de/talentcommunity/apply/1278821501/?locale=de_DE
    {
        "folder": "Fraunhofer SIT Darmstadt Masterarbeit Alterschaetzung Loss Design",
        "company": "Fraunhofer-Institut fuer Sichere Informationstechnologie SIT",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Loss Design und Evaluation bei Klassenungleichgewicht | Python + scikit learn + CatBoost",
        "role_strip": "Masterarbeit Modellierungsansaetze und Loss Design fuer praezise Alterschaetzung",
        "cl_date": "25. August 2026",
        "cl_subject": "Masterarbeit Modellierungsansaetze und Loss Design fuer praezise Alterschaetzung, Kennziffer 82686",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im kritischen Vergleich von Modellierungsansaetzen und Metriken unter starkem Klassenungleichgewicht. Ich habe in meiner Bachelorarbeit sechs Klassifikatoren verglichen und bei einer 65 zu 35 Klassenungleichgewicht Verteilung die Leitmetrik bewusst von Genauigkeit auf ROC AUC umgestellt, und in CreditIQ eine SHAP getriebene Subgruppenanalyse genutzt, um eine versteckte, durch die falsche Metrik verdeckte Verzerrung aufzudecken. Sicher in Python, Machine Learning Grundlagen und im Design und der kritischen Pruefung von Evaluationsmetriken.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit Modellierungsansaetze und Loss Design fuer praezise Alterschaetzung unter der Kennziffer 82686 am Fraunhofer SIT in Darmstadt. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Fragestellung, wann die Wahl von Loss und Architektur wirklich entscheidungsrelevant ist und wann nicht, weil ich in den letzten Monaten genau an dieser Schnittstelle von Metrikwahl, Klassenungleichgewicht und Modellvergleich gearbeitet habe.",
            "In meiner Bachelorarbeit zur Diabetesvorhersage habe ich sechs Klassifikatoren mit 10 facher Kreuzvalidierung verglichen und bei einer 65 zu 35 Klassenungleichgewicht Verteilung, die Genauigkeit zu einer truegerisch schoenen Leitmetrik gemacht haette, die Leitmetrik auf ROC AUC umgestellt, was die realen Fehlermuster offenlegte, die die Genauigkeitszahl maskiert hatte. Genau diese Faehigkeit, bei unausgewogenen Daten und langen Verteilungsenden die richtige Metrik zu waehlen statt sich auf eine irrefuehrende Standardmetrik zu verlassen, deckt sich direkt mit der in der Ausschreibung geforderten kritischen Pruefung bestehender Metriken fuer die Alterschaetzung.",
            "In CreditIQ habe ich mit SHAP getriebener Subgruppenanalyse eine versteckte intersektionale Verzerrung ueber Alter und Geschlecht aufgedeckt, die eine einachsige Korrektur uebersehen hatte, und ueber eine vierstufige Schwellenwertmatrix korrigiert, ohne in umgekehrte Diskriminierung zu kippen. In meinem Multi Agent RAG Projekt habe ich einen JudgeAgent gebaut, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet und bewusst auf einem anderen Modell laeuft als der Generator, um Self Preference Bias zu vermeiden. Beide Projekte zeigen die gleiche Sorgfalt im Design und in der kritischen Pruefung von Evaluationsmetriken, die die Ausschreibung fuer den Vergleich von Punkt Regression, probabilistischer Regression, Quantil Regression, Klassifikation, ordinaler Klassifikation und Label Distribution Learning braucht.",
            "Ich arbeite sicher in Python, Machine Learning Grundlagen und im Training neuronaler Netze, habe erste Beruehrung mit Computer Vision Aufgaben und interessiere mich stark fuer Optimierungs und Evaluationsmetriken. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, Englisch spreche ich fliessend. Gerne bespreche ich das Thema in einem persoenlichen Gespraech.",
        ],
    },
]
