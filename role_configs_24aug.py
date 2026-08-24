"""Role configurations for the 24 August 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 9 rows in
status 'drafted' at run start. 8 to 10 drafted falls in the yield reset
tier that caps this run at the top 3 newly scored roles.

Reconciliation this run updated 6 CSV rows from 'drafted' to their true
Notion Status, all flipped to 'applied' by OpenClaw since the 21 Aug run
(Amprion Werkstudent KI Stellen ID 7959, BCG Platinion, Arthrex, Sana HR
Solutions, Robert Bosch Halbleiterdatenbank, FLEX Capital Management).
All six had real rendered deliverables on disk confirming genuine
OpenClaw submissions, so the CSV flips are evidence backed per invariant
4. Separately, reconciliation surfaced 9 Notion rows in status 'drafted'
(Boellhoff Gruppe, Anstalt fuer Kommunale Datenverarbeitung in Bayern,
NewTec GmbH, Schaeffler Technologies, logen.ai, nerou GmbH, ADAC, DELO
Industrie Klebstoffe, Rosenberger Hochfrequenztechnik) whose Draft Path
values point at folders that do not exist anywhere in this git repo or
its history. Per invariant 2 git is the source of truth for content, and
per invariant 3 halting beats a false success, these 9 rows were NOT
mirrored into applied-log.csv (there is no real deliverable to point an
audit trail at) and were left untouched in Notion (Cowork does not own
modifying existing Notion rows, only creating new drafted rows). Flagged
prominently in today's digest for Rah to investigate; likely a prior run
that created the Notion rows but never rendered or committed the actual
files.

Because the 9 orphaned Notion rows still count toward the authoritative
Notion drafted total per the standing rule (Notion count is authoritative
regardless of the anomaly), the backlog gate this run used 9, landing in
the 8 to 10 cap tier. This run's 3 new roles are for different companies
than every one of the 9 orphaned rows, so no duplicate Notion row risk.

Platform mix this run:
  - LinkedIn: 1 (KPMG Deutschland)
  - StepStone: 2 (MEAG MUNICH ERGO, Senacor Technologies)
  - Indeed: 0 this run

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. KPMG Deutschland Werkstudent Business Intelligence and Analytics
     (Berlin), posted 3 days ago, Werkstudent, DE track
  2. MEAG MUNICH ERGO AssetManagement GmbH Werkstudent Data Enablement
     (Muenchen), posted 1 week ago, Werkstudent, DE track
  3. Senacor Technologies AG Abschlussarbeit Datenstrategie und
     Kuenstliche Intelligenz (multiple DACH locations, homeoffice
     possible), posted 3 days ago, Masterarbeit, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all three postings are written in
German -> DE track for all three.

Language level transparency: KPMG asks for "sehr gute Deutsch- und
Englischkenntnisse", MEAG asks for German and English at minimum B2, and
Senacor asks for "sehr gute Deutschkenntnisse" (no English requirement
stated). Rah's German is B1, currently in progress, below all three
stated bars. Shipped anyway per the standing rule that language level
does not filter listings, and the cover letters are upfront about the
current B1 level. Flagged in the digest transparency block.

Dedup check against applied-log.csv and Notion: KPMG Deutschland, MEAG
MUNICH ERGO AssetManagement GmbH, and Senacor Technologies AG are all
new companies, never previously logged.

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
    P_TABLEAU_DE,
    P_CLIMATE_DE,
)


CONFIGS_24AUG = [
    # 1. KPMG Deutschland, Berlin
    # Werkstudent Business Intelligence & Analytics (m/w/d)
    # LinkedIn, posted 3 days ago. Start October 2026, 6 months.
    # Tasks: internal Analytics team, SQL and Power BI dashboards,
    # Marketing and Sales Analytics, translating analyses into insights,
    # optional exposure to automation and KI tooling, Go to Market support.
    # Requirements: data/business/tech degree program, first touchpoints
    # with BI tools like Power BI, first experience with SQL and a
    # language like Python or R, interest in KI and automation, very good
    # German and English.
    # Apply: https://de.linkedin.com/jobs/view/werkstudent-business-intelligence-analytics-m-w-d-at-kpmg-deutschland-4456001674
    {
        "folder": "KPMG Berlin Werkstudent Business Intelligence Analytics",
        "company": "KPMG Deutschland",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | BI Dashboards und Data Storytelling | Python + SQL + Power BI + Tableau",
        "role_strip": "Werkstudent Business Intelligence und Analytics",
        "cl_date": "24. August 2026",
        "cl_subject": "Werkstudent Business Intelligence und Analytics im internen Analytics Team am Standort Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau interaktiver Dashboards und in der Uebersetzung komplexer Analysen in verstaendliche Insights fuer nicht technische Stakeholder. Ich habe ein Tableau Dashboard mit dynamischem Set Actions Warenkorb und ein 5 seitiges Looker Studio Dashboard fuer Geschaeftsfragen zu ROI und Timing gebaut sowie eine Random Forest Analyse globaler Klimaereignisse bis zum management fertigen Report gefuehrt. Sicher in SQL, Python, Power BI, Tableau und in der strukturierten Aufbereitung von Daten fuer Marketing, Sales und Automatisierung.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_TABLEAU_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_GOOGLE_DE, CERT_AWS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Business Intelligence und Analytics im internen Analytics Team am Standort Berlin ab Oktober 2026 fuer 6 Monate. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus SQL und Power BI Dashboard Arbeit, Marketing und Sales Analytics und der Uebersetzung komplexer Analysen in verstaendliche Insights fuer unterschiedliche interne Stakeholder, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Fast Food Naehrwert Analyzer und Meal Simulator Projekt habe ich mit Tableau Set Actions einen dynamischen Warenkorb umgesetzt, der beim Auswaehlen von Scatter Plot Punkten sofort die 3 zentralen Makros summiert, dazu eine parameter gesteuerte Y Achse per CASE Statement fuer 2 Nutzerziele ohne Dashboard Reload und komplexe IF THEN Calculated Fields fuer Warnflags wie Is It A Trap, die in manuellen Stichproben korrekt trafen. Genau dieses Muster, Rohdaten in ein interaktives Self Service Dashboard mit klaren Handlungsempfehlungen zu verwandeln, laesst sich direkt auf Marketing und Sales Analytics Dashboards uebertragen.",
            "In meiner wirtschaftlichen Analyse globaler Klimaereignisse habe ich ein end to end Projekt von der Roh CSV bis zum management fertigen Report gefuehrt, Ausreisser, fehlende Werte und inkonsistente Skalen bereinigt, Random Forest Modelle zur Analyse des Zusammenhangs zwischen Ereignisdauer und finanzieller Wirkung entwickelt und die Ergebnisse in vollstaendigen visuellen Reports mit kalibrierten Konfidenzaussagen kommuniziert, die einer Management Review ohne weitere Uebersetzung standhielten. Diese Faehigkeit, aus rohen Daten eine belastbare, fuer Nicht Techniker verstaendliche Insight Story zu bauen, deckt sich mit dem, was die Ausschreibung als Data Insights Aufgabe beschreibt.",
            "Ich arbeite sicher in SQL, Python, Power BI und Tableau, interessiere mich aktiv fuer KI und Automatisierungstools und nutze ChatGPT und Claude im Alltag. Ich halte das SAS Certified Specialist Visual Business Analytics Using SAS Viya und das Google Data Analytics Zertifikat sowie die AWS Academy Cloud Foundations Zertifizierung und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann ab Oktober 2026 in Berlin fuer 6 Monate als Werkstudent einsteigen. Gerne bespreche ich meinen Beitrag zum Analytics Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. MEAG MUNICH ERGO AssetManagement GmbH, Muenchen
    # Werkstudent Data Enablement (m|w|d)
    # StepStone, posted 1 week ago. Vor Ort in Muenchen erforderlich.
    # Tasks: use case team setup, Python and SQL technical work, data
    # pipeline support, data governance tool comparison, data policy
    # documentation.
    # Requirements: Informatik / Wirtschaftsinformatik / Data Science
    # study, first practical data experience (SQL, Python, BI tools),
    # basic understanding of data platforms and data governance, German
    # and English at least B2.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-Data-Enablement-mwd-Muenchen-MEAG-MUNICH-ERGO-AssetManagement-GmbH--14395291-inline.html
    {
        "folder": "MEAG Muenchen Werkstudent Data Enablement",
        "company": "MEAG MUNICH ERGO AssetManagement GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Data Pipelines und Data Governance | Python + SQL + Data Cataloguing",
        "role_strip": "Werkstudent Data Enablement",
        "cl_date": "24. August 2026",
        "cl_subject": "Werkstudent Data Enablement am Standort Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenpipelines, in der Bewertung von Data Governance Ansaetzen und in der strukturierten Dokumentation von Datenprozessen. Ich habe eine Real Time Flight Tracking Pipeline mit Python Collectors, PySpark Cleaning und dbt Modellierung ueber vier Datenquellen gebaut und in einem Cloud Data Projekt eine 3 stufige Bronze Silver Gold Medaillon Architektur mit Schema Enforcement und sauberer referenzieller Integritaet gehaertet. Sicher in Python, SQL, dbt, BigQuery und in der strukturierten Aufbereitung von Themen fuer Praesentationen und Excel.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Enablement am Standort Muenchen bei der MEAG MUNICH ERGO AssetManagement GmbH. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die in der Ausschreibung genannte Kombination aus technischen Data Aufgaben in Python und SQL, dem Vergleich von Data Governance Tools und Ansaetzen und der Pflege von Datenrichtlinien, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, die aus rohen Daten belastbare, dokumentierte Grundlagen machen.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt, die Daten mit dbt in analysebereite Tabellen modelliert und das Gesamtsystem mit Apache Airflow auf GCS Speicher und Dataproc Compute vollstaendig automatisiert. Genau dieses Muster, technische Datenaufgaben strukturiert dokumentieren und in ein wiederholbares System uebersetzen, deckt sich mit dem, was die Ausschreibung fuer den Aufbau kleiner Datenpipelines und die Durchfuehrung von Datenanalysen beschreibt.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung, Deduplizierung ueber Window Functions und Genre Normalisierung in ein relationales Modell gehaertet, was saubere referenzielle Integritaet ueber alle nachgelagerten Gold Tabellen lieferte, und das System mit einem Least Privilege Service Account und Secret Manager abgesichert. Diese Erfahrung mit Datenmodellen, Zugriffsmodellen und Metadaten deckt sich direkt mit dem in der Ausschreibung geforderten Grundverstaendnis von Datenplattformen und Data Governance sowie mit der Aufgabe, strukturierte Entscheidungsgrundlagen fuer Data Catalogue Loesungen zu erstellen.",
            "Ich arbeite sicher in Python, SQL, dbt, BigQuery und Apache Airflow, bereite Themen gerne strukturiert in Praesentationen und Excel auf und nutze ChatGPT und Claude aktiv im Alltag. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter Richtung des geforderten Niveaus, und Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen vor Ort einsteigen und meine Anwesenheit mit dem Team abstimmen. Gerne bespreche ich meinen Beitrag zum Data Enablement Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Senacor Technologies AG, mehrere DACH Standorte
    # Abschlussarbeit im Bereich Datenstrategie und Kuenstliche Intelligenz
    # StepStone, posted 3 days ago. Bachelor/Master Abschlussarbeit,
    # Homeoffice moeglich, Vollzeit, kein Umzug an einen Senacor Standort
    # noetig (remote von Deutschland, Oesterreich oder der Schweiz aus).
    # Tasks: research current tech developments like KI and prerequisites
    # for daily business use, analyse data strategy and data integration
    # processes and their significance for KI implementation, develop
    # concepts and recommendations for introducing KI based on an
    # efficient data strategy, work independently with close exchange to
    # subject matter experts.
    # Requirements: near completion of Bachelor or Master in
    # Wirtschaftsinformatik, Informatik, BWL or comparable with above
    # average grades, ideally first consulting or IT project experience,
    # interest in data strategy, data integration and KI, very good
    # abstraction ability and analytical thinking, proactive structured
    # work style, very good German.
    # Apply: https://www.stepstone.de/stellenangebote--Abschlussarbeit-im-Bereich-Datenstrategie-und-Kuenstliche-Intelligenz-Berlin-Bonn-Frankfurt-Hamburg-Muenchen-Nuernberg-Wien-Senacor-Technologies-AG--12683570-inline.html
    {
        "folder": "Senacor Masterarbeit Datenstrategie Kuenstliche Intelligenz",
        "company": "Senacor Technologies AG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Datenstrategie und KI Einfuehrung | Python + LangGraph + SQL",
        "role_strip": "Abschlussarbeit Datenstrategie und Kuenstliche Intelligenz",
        "cl_date": "24. August 2026",
        "cl_subject": "Abschlussarbeit im Bereich Datenstrategie und Kuenstliche Intelligenz",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Datenstrategie, regulatorischer Compliance und dem produktiven Einsatz von KI. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama gebaut und in CreditIQ ein reguliertes Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben hat und die Anforderungen aus EU AI Act Artikel 14 und GDPR Artikel 22 erfuellt. Sicher in Python, SQL, LangGraph und in der Uebersetzung von Datenstrategie Konzepten in produktionsreife, regulatorisch belastbare Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Abschlussarbeit im Bereich Datenstrategie und Kuenstliche Intelligenz bei Senacor Technologies AG. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Aufgabe, Datenstrategie und Datenintegrationsprozesse zu analysieren und daraus Konzepte fuer eine effiziente KI Einfuehrung abzuleiten, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe, in denen eine saubere Datenstrategie erst den verantwortungsvollen KI Einsatz moeglich macht.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Der LanguageAgent zentralisiert eine einheitliche Wahrheitsquelle fuer Sprache, der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Genau diese Faehigkeit, aktuelle technologische Entwicklungen wie KI zu recherchieren und in ein belastbares, messbares System zu uebersetzen, deckt sich mit dem in der Ausschreibung beschriebenen ersten Arbeitspaket der Abschlussarbeit.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben, mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und den Fairness Accuracy Trade off als bewusste, regulatorisch belastbare Entscheidung dokumentiert. Die vollstaendige regulatorische Dokumentation, die GDPR Artikel 22 und EU AI Act Artikel 14 abdeckt, ist genau die Art von Konzeptarbeit und Handlungsempfehlung, die die Ausschreibung fuer die Einfuehrung von KI basierend auf einer effizienten Datenstrategie beschreibt.",
            "Ich arbeite sicher in Python, SQL, LangGraph und Streamlit und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Notenschnitt an der SRH Heidelberg liegt bei 1,9. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich stehe kurz vor dem Abschluss meines Masterstudiums und kann die Abschlussarbeit remote aus Mannheim heraus beginnen, mit der Bereitschaft zu gelegentlichen Terminen an einem der Senacor Standorte. Gerne bespreche ich das Thema in einem persoenlichen Gespraech.",
        ],
    },
]
