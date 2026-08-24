"""Role configurations for the 23 August 2026 scheduled Cowork run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 5 rows in
status 'drafted' at run start (Boellhoff Gruppe, NewTec GmbH, Anstalt
fuer Kommunale Datenverarbeitung in Bayern, Schaeffler Technologies AG
und Co. KG, logen.ai). Under 8 drafted falls in the normal top 3 to 5
tier under the 28 July 2026 yield reset.

Reconciliation this run found two-way drift:
  - 6 CSV rows still marked 'drafted' had already been flipped to
    'applied' in Notion by OpenClaw since the 21 Aug run: Amprion GmbH
    Werkstudent KI Stellen-ID 7959, BCG Platinion, Arthrex GmbH, Sana HR
    Solutions GmbH, Robert Bosch GmbH Masterarbeit Agentisches KI-System
    fuer eine Halbleiterdatenbank, FLEX Capital Management GmbH. All 6
    updated CSV drafted -> applied to match Notion.
  - 5 Notion rows dated 22 Aug 2026 (a run not reflected in this git
    checkout, likely a session whose git push never landed) had no CSV
    counterpart and no rendered files on disk: Boellhoff Gruppe, Anstalt
    fuer Kommunale Datenverarbeitung in Bayern, NewTec GmbH, Schaeffler
    Technologies AG und Co. KG, logen.ai. Per the Notion CSV Drift
    playbook, all 5 appended to the CSV as 'drafted' with Notion's data.
    Flagged in the digest transparency block since Rah has no CV or CL
    PDFs anywhere for these 5 despite Notion showing them as drafted.

Top 4 cut per 28 July 2026 yield reset. Only 3 truly fresh non-Indeed
leads confirmed still open across LinkedIn, Xing, StepStone, and company
pages today, plus one older but strong domain fit LinkedIn listing kept
in because of an unusually tight project match.

Platform mix for this run per 28 July 2026 yield weighting (Indeed used
0 times, none confirmed both fresh and strong fit today):
  - StepStone: 3 (ADAC Muenchen, Rosenberger Fridolfing, DELO Windach
    bei Muenchen)
  - LinkedIn: 1 (nerou GmbH Berlin, email apply, out of OpenClaw scope)

Freshness order within the Germany tier:
  1. Rosenberger Hochfrequenztechnik GmbH und Co. KG, Werkstudent fuer
     KI Projekte, Fridolfing, posted 2 days ago (StepStone).
  2. ADAC, Werkstudent Data and AI Solutions, Muenchen, posted 4 days
     ago (StepStone).
  3. DELO Industrie Klebstoffe GmbH und Co. KGaA, Werkstudent IT mit
     Schwerpunkt Kuenstliche Intelligenz, Windach bei Muenchen, posted
     1 week ago (StepStone).
  4. nerou GmbH, Werkstudent Data Science, Berlin, posted 1 month ago
     per the LinkedIn listing itself (evergreen repost). Kept despite
     the age because nerou builds ML based decision support software
     for Klaeranlagen operators, an unusually close domain match to the
     eRay GmbH lake water quality forecasting experience entry.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all four posting bodies are in
German, so all four are DE track.

Dedup check against applied-log.csv and Notion: ADAC, Rosenberger
Hochfrequenztechnik, DELO Industrie Klebstoffe, and nerou GmbH are all
new companies, never previously applied to.

Apply method notes:
  - Rosenberger and DELO both show StepStone's own one click "Ich bin
    interessiert" apply button on the listing itself (no redirect to an
    external company portal visible), so Apply Method is set to
    platform-native for OpenClaw.
  - ADAC's listing did not show that same one click button; Apply
    Method left unset for OpenClaw to confirm live in browser per its
    own step 2 scope check.
  - nerou GmbH's posting is an email only application (send CV, cover
    letter, and transcripts to jobs@nerou.de), not a platform Easy
    Apply flow. Apply Method set to company-portal (out of OpenClaw's
    platform-native automation scope) with Notes explaining the email
    address Rah needs to send to manually.

German level per posting:
  - ADAC: no explicit level stated in the posting text, set to none.
  - Rosenberger: "gute Deutschkenntnisse in Wort und Schrift" stated,
    set to B2, flagged as a stretch above Rah's current B1 in progress
    per master-projects.md, consistent with prior AKDB (C1) precedent
    of drafting and flagging rather than dropping.
  - DELO: "gute Deutsch und Englischkenntnisse" stated, set to B2.
  - nerou: no explicit level stated in the posting text but the entire
    ad and application flow are German only, set to B1.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses/brackets in bullets, Languages EN+DE only (no Hindi),
German level locked to 'Deutsch: B1, laufend' on DE track, no page
numbers/headers/footers, 2 page hard cap, Ojas style header (name, tag,
contact lines, italic status), Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title, and
banned strings on the validation gate are met by the new header.
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


CONFIGS_23AUG = [
    # 1. ADAC, Muenchen
    # Werkstudent Data & AI Solutions (w|m|d). StepStone, posted 4 days
    # ago, Teilzeit, Homeoffice moeglich. Stack: Power BI, SQL, Excel,
    # M365 Copilot KI-Loesungen, Digitalisierung/Automatisierung im
    # Assistance-Umfeld.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Data-AI-Solutions-wmd-Muenchen-ADAC--14408416-inline.html
    {
        "folder": "ADAC Muenchen Werkstudent Data AI Solutions",
        "company": "ADAC",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | BI Dashboards und KI Use Cases | Python + SQL + Power BI",
        "role_strip": "Werkstudent Data and AI Solutions",
        "cl_date": "23. August 2026",
        "cl_subject": "Werkstudent Data and AI Solutions am Standort Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Dashboards, Reports und Automatisierungsloesungen fuer produktionsnahe Umgebungen. Ich habe eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit einem 5 seitigen Looker Studio Dashboard geliefert und in einer Real Time Flight Tracking Pipeline Python Collectors, PySpark Cleaning und ein Tableau Workbook mit Python Statistik ueber TabPy kombiniert. Sicher in Python, SQL, Power BI und Looker Studio sowie im Uebersetzen von KI Use Cases wie Copilot gestuetzten Automatisierungen in konkrete Dashboards und Reports.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data and AI Solutions am Standort Muenchen beim ADAC. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Kombination aus Datenaufbereitung und Analyse gemeinsam mit einem Data Analyst, der Pflege von Dashboards und Reports in Power BI und der Entwicklung und dem Testen KI basierter Loesungen wie M365 Copilot, weil ich in den letzten Monaten genau an dieser Kette Systeme gebaut habe, die aus Rohdaten verlaessliche Dashboards machen.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt und die Ergebnisse in ein Tableau Workbook mit Python Statistik ueber TabPy ueberfuehrt, das die Erkenntnis freilegte, dass der Flugverkehr bei starkem Regen um das 4,4 fache einbricht. Das gesamte System laeuft alle 15 Minuten unbeaufsichtigt auf Apache Airflow. Genau dieses Muster, roh Signale zu sauberen Tabellen und dann zu einem Dashboard mit klarer Handlungsempfehlung, laesst sich direkt auf Digitalisierungs und Automatisierungsinitiativen im Assistance Umfeld des ADAC uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut und einen 5 seitigen Looker Studio Dashboard mit Aussagen zu Genre ROI und Erscheinungssaison ausgeliefert. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit einem 3 Pass Outlier System belastbar gemacht, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff freilegte. Die Kombination aus sauberer Datenaufbereitung, Reporting und einem ehrlichen Blick auf Modellqualitaet ist genau das, was neue Data und AI Use Cases beim ADAC brauchen, um Dokumentation und Ergebnisse verlaesslich aufzubereiten.",
            "Ich arbeite sicher in Python, SQL, Excel und Power BI, interessiere mich aktiv fuer KI, IT und digitale Innovationen und nutze taeglich ChatGPT und Claude als Werkzeuge. Ich halte die SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics und AWS Academy Cloud Foundations Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter. Als Werkstudent kann ich in Muenchen im Rahmen des Werkstudentenmodells einsteigen und bringe eine strukturierte, analytische Arbeitsweise mit. Gerne bespreche ich meinen Beitrag zum Data and AI Team des ADAC in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Rosenberger Hochfrequenztechnik GmbH und Co. KG, Fridolfing
    # Werkstudent fuer KI-Projekte (m/w/d). StepStone, posted 2 days ago,
    # Homeoffice moeglich, Teilzeit. Stack: Generative AI, Computer
    # Vision, LLM Fine Tuning und Evaluation, Python, Azure AI.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-fuer-KI-Projekte-m-w-d-Fridolfing-Rosenberger-Hochfrequenztechnik-GmbH-Co-KG--13985042-inline.html
    {
        "folder": "Rosenberger Fridolfing Werkstudent KI Projekte",
        "company": "Rosenberger Hochfrequenztechnik GmbH und Co. KG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Generative AI und LLM Evaluation | Python + LangGraph + Azure AI",
        "role_strip": "Werkstudent fuer KI Projekte",
        "cl_date": "23. August 2026",
        "cl_subject": "Werkstudent fuer KI Projekte am Standort Fridolfing",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Generative AI, Large Language Models und ehrlicher Evaluation. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B als Generator und Qwen2.5 14B als Judge gebaut und in CreditIQ ein reguliertes Kredit Scoring System von Prototyp bis produktivem Streamlit Tool entwickelt. Sicher in Python, LangGraph und Cloud KI Diensten sowie im End to End Aufbau von Prototypen von der Datenaufbereitung bis zur Praesentation der Ergebnisse.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit fuer KI Projekte am Standort Fridolfing bei der Rosenberger Hochfrequenztechnik GmbH und Co. KG. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Mitarbeit an Forschungs und Entwicklungsprojekten im Bereich Generative AI und Computer Vision sowie die Entwicklung, das Fine Tuning und die Evaluation von KI Modellen, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, die nicht nur antworten, sondern auch messbar richtig antworten.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Evaluations Set. Genau dieses Muster aus Modell Fine Tuning, Evaluation und End to End Prototyp in Python laesst sich direkt auf die geforderten Forschungs und Entwicklungsprojekte im Bereich Generative AI uebertragen.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und korrigiert. Das Modell laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer und einer Unit Test Suite mit 100 Prozent Branch Coverage. Genau diese Verbindung aus Datenaufbereitung, Feature Engineering, Modelltraining und Dokumentation der Ergebnisse deckt sich mit dem geforderten End to End Ablauf von der Datenaufbereitung bis zur Praesentation.",
            "Ich arbeite sicher in Python, LangGraph und Cloud Plattformen, habe erste Beruehrung mit Azure durch meine Cloud Projekte auf GCP und AWS und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit ich Dokumentation und Praesentationen zunehmend auf Deutsch liefern kann. Als Werkstudent kann ich in Fridolfing oder mobil einsteigen und bringe eine motivierte, selbststaendige Arbeitsweise mit. Gerne bespreche ich meinen Beitrag zu den KI Projekten der Rosenberger Gruppe in einem persoenlichen Gespraech.",
        ],
    },

    # 3. DELO Industrie Klebstoffe GmbH und Co. KGaA, Windach bei Muenchen
    # Werkstudent IT mit Schwerpunkt Kuenstliche Intelligenz (w/m/d).
    # StepStone, posted 1 week ago, Teilzeit, cover letter optional per
    # the posting's "Anschreiben nicht erforderlich" tag but produced
    # anyway per the 11 August 2026 CoverLetter PDF required rule.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-IT-mit-Schwerpunkt-Kuenstliche-Intelligenz-w-m-d-Windach-bei-Muenchen-DELO-Industrie-Klebstoffe-GmbH-Co-KGaA--14153215-inline.html
    {
        "folder": "DELO Windach Werkstudent IT KI",
        "company": "DELO Industrie Klebstoffe GmbH und Co. KGaA",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Use Cases und Automatisierung | Python + LangGraph + SQL",
        "role_strip": "Werkstudent IT mit Schwerpunkt Kuenstliche Intelligenz",
        "cl_date": "23. August 2026",
        "cl_subject": "Werkstudent IT mit Schwerpunkt Kuenstliche Intelligenz am Standort Windach bei Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in der Umsetzung von KI Use Cases von der Idee bis zum funktionierenden Prototyp. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama gebaut und eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger geliefert. Sicher in Python, SQL, LangGraph und Streamlit sowie in der engen Abstimmung mit Fachabteilungen bei technischen Umsetzungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit IT mit Schwerpunkt Kuenstliche Intelligenz bei der DELO Industrie Klebstoffe GmbH und Co. KGaA am Standort Windach bei Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die in der Ausschreibung beschriebene Unterstuetzung bei der Umsetzung von KI Usecases in enger Abstimmung mit dem DI Projektteam und anderen Fachabteilungen, weil ich in den letzten Monaten genau an dieser Schnittstelle zwischen technischer Umsetzung und Fachbereich Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports. Genau dieses Muster, einen KI Usecase von der ersten Idee bis zu einem messbar funktionierenden System zu bringen und dabei eng mit Anforderungen aus anderen Bereichen abzustimmen, laesst sich direkt auf neue KI Usecases bei DELO uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut, den Silver Layer mit Schema Enforcement und Deduplizierung gehaertet und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Diese Sorgfalt bei der technischen Umsetzung und Dokumentation deckt sich mit dem, was ein Mittelstaendler wie DELO fuer verlaessliche KI Loesungen braucht.",
            "Ich arbeite sicher in Python, SQL, LangGraph und Streamlit, interessiere mich aktiv fuer aktuelle Entwicklungen rund um das Thema KI und nutze taeglich ChatGPT und Claude als Werkzeuge. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ich verfuege ueber gute Deutsch und Englischkenntnisse, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter. Als Werkstudent kann ich in Windach bei Muenchen einsteigen und bringe eine selbststaendige und zuverlaessige Arbeitsweise mit. Gerne bespreche ich meinen Beitrag zur IT Abteilung von DELO in einem persoenlichen Gespraech.",
        ],
    },

    # 4. nerou GmbH, Berlin
    # Werkstudent:in Data Science. LinkedIn, listing itself dated 1
    # month ago (evergreen repost), email only application to
    # jobs@nerou.de, out of OpenClaw's platform-native automation scope.
    # Kept in the top cut for the unusually close domain fit: nerou
    # builds ML based decision support software for Klaeranlagen
    # operators, which maps directly onto the eRay GmbH lake water
    # quality forecasting experience entry.
    # Apply: https://de.linkedin.com/jobs/view/werkstudent-in-data-science-at-nerou-gmbh-4437373126 (send CV, cover letter and transcripts to jobs@nerou.de)
    {
        "folder": "nerou Berlin Werkstudent Data Science",
        "company": "nerou GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Zeitreihen und Entscheidungsunterstuetzung | Python + scikit learn + Statistik",
        "role_strip": "Werkstudent Data Science",
        "cl_date": "23. August 2026",
        "cl_subject": "Werkstudent:in Data Science am Standort Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Machine Learning gestuetzten Entscheidungshilfen aus grossen, teils luekenhaften Sensordatenbestaenden. Bei eRay GmbH habe ich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren einer deutschen Seeanlage gebaut und mit einem 3 Pass Outlier System und IterativeImputer MICE Rekonstruktion belastbar gemacht. Sicher in Python, scikit learn, statistischer Modellierung und im Extrahieren und Validieren grosser Datenbestaende auf Basis wechselnder Fragestellungen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CLIMATE_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science bei der nerou GmbH am Standort Berlin. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim hat mich die Beschreibung Ihrer Datenanalyse Software fuer Betreiber von Klaeranlagen sofort angesprochen, weil ich in meiner eRay GmbH Zusammenarbeit genau an einer vergleichbaren Aufgabe gearbeitet habe, komplexe, sich staendig aendernde Sensordaten einer Wasseranlage in verlaessliche Entscheidungshilfen zu uebersetzen.",
            "Bei eRay GmbH habe ich ueber 6 Monate eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren, Chlorophyll a, Truebung, pH Wert und geloesten Sauerstoff, ueber einen 40 Feature Raum mit CatBoost MultiQuantile Modellen gebaut, die asymmetrische 80 Prozent Vorhersageintervalle liefern. Ein 3 Pass Outlier System mit rollierendem Z Score und der Ausschluss unzuverlaessiger Sensoren machten die Evaluation belastbar und legten einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff frei, und Datenluecken wurden mit IterativeImputer MICE rekonstruiert. Genau diese Kombination aus Extraktion, Validierung und statistischer Analyse grosser, teils luekenhafter Sensordatenbestaende auf Basis wechselnder Fragestellungen ist die Aufgabe, die die Ausschreibung beschreibt.",
            "In meinem Projekt zur wirtschaftlichen Analyse globaler Klimaereignisse habe ich eine end to end Pipeline von der Rohdatenaufbereitung ueber Ausreisser und fehlende Werte bis zu Random Forest Modellen gebaut, die Zusammenhaenge zwischen Ereignisdauer und finanzieller Wirkung ueber Feature Importance und Residuenanalyse offenlegten, und die Ergebnisse in verstaendlichen Reports fuer nicht technische Stakeholder aufbereitet. In meiner Real Time Flight Tracking Pipeline habe ich zusaetzlich Python Collectors und PySpark Cleaning ueber vier Datenquellen zu einer sauberen, validierten Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt. Diese Erfahrung im Aufbau geeigneter statistischer Methoden fuer wechselnde Fragestellungen deckt sich direkt mit dem, was Ihr Data Science Bereich braucht.",
            "Ich arbeite sicher in Python, scikit learn und statistischer Modellierung, strukturiere meine Arbeit selbststaendig und halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate sowie die Auszeichnung als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, mein Englisch ist fliessend. Als Werkstudent kann ich flexibel zwischen Buero und Home Office arbeiten und bin an eigenen Projekten im Data Science Bereich sehr interessiert. Gerne bespreche ich meinen Beitrag zum nerou Team in einem persoenlichen Gespraech. Anbei sende ich meinen Lebenslauf, mein Anschreiben und meine Zeugnisse.",
        ],
    },
]
