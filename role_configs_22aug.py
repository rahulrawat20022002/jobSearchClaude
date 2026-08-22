"""Role configurations for the 22 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 0 rows in
status 'drafted' at run start. Under 8 drafted falls in the normal top
3 to 5 tier under the 28 July 2026 yield reset.

Reconciliation this run found 6 CSV rows stale at 'drafted' while Notion
already showed 'applied' for the same company plus role (Amprion
Werkstudent KI Stellen-ID 7959, BCG Platinion, Arthrex, Sana HR
Solutions, Robert Bosch Renningen Masterarbeit, FLEX Capital
Management). CSV updated to match Notion per the source of truth rule;
no CSV row was missing a Notion counterpart.

Top 3 cut per 28 July 2026 yield reset: with 0 drafted at run start, the
run targets fresh roles. Held to top 3 today; a fourth candidate (ADAC
Werkstudent Data and AI Solutions, Muenchen, StepStone) was scored but
NOT drafted because every mirror of its posting (StepStone, Bundesagentur
fuer Arbeit, finest-jobs, bebee) rendered the Aufgaben and Profil sections
blank behind client side JavaScript; only a thin fragment of task text
could be recovered. Per CLAUDE.md invariant 3, never fabricate, a CV and
cover letter were not tailored against unread requirements. Listed on the
watchlist instead.

Platform mix for this run per 28 July 2026 yield weighting (Indeed
capped at 1 per run, 0 used today because no fresh Indeed lead cleared
the bar after checking the pipeline against known low signal snapshot
pages):
  - StepStone: 1 (AKDB Muenchen)
  - Xing: 1 (NewTec Ulm)
  - Company Page: 1 (Boellhoff Gruppe Bielefeld, jobs.boellhoff.com)
  - LinkedIn / Indeed: 0 this run

Freshness order per 12 July 2026 priority rule within the single
Germany tier:
  1. NewTec GmbH Ulm, Praxissemester/Werkstudent KI und Data Science,
     posted approximately 11 hours ago on Xing, Werkstudent, DE track.
  2. AKDB (Anstalt fuer Kommunale Datenverarbeitung in Bayern) Muenchen,
     Werkstudent AI and Machine Learning, NLP and Semantic Search,
     posted approximately 1 day ago on StepStone, Werkstudent, DE track.
  3. Boellhoff Gruppe Bielefeld, Masterarbeit mit optionalem Praktikum
     or Werkstudententaetigkeit im Bereich AI driven Patent Analytics,
     company career page jobs.boellhoff.com, freshness not date stamped
     on the posting itself but surfaced as a live open requisition this
     week via search, Masterarbeit, DE track.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all three posting bodies are written
in German, so all three ship on the DE track.
  - AKDB states verhandlungssichere Deutschkenntnisse mindestens auf
    C1-Niveau. Rah's B1 level is below the stated bar, noted in digest
    transparency block, still shipped per the standing rule that
    language level does not filter listings.
  - NewTec and Boellhoff postings do not state an explicit German level
    bar beyond being written in German throughout.

Dedup check against applied-log.csv and Notion: all three company plus
role combinations verified absent from both. NewTec, AKDB, and Boellhoff
are all new companies never previously contacted in this pipeline.

All three tag as Werkstudent, Praxissemester, or Masterarbeit; all three
are in-scope target roles under the master-projects.md 'Werkstudent /
part time' and 'Master Thesis' work types. None are dual-study,
apprenticeship, Quereinsteiger, or voluntary internship listings.

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
)


CONFIGS_22AUG = [
    # 1. NewTec GmbH, Ulm
    # Praxissemester/Werkstudent (m/w/d) KI und Data Science
    # Xing, posted approximately 11 hours ago. Teilzeit, mindestens 16h/Woche.
    # Stack: SQL database queries, in house AI use cases, cross functional
    # collaboration with subject matter experts across departments.
    # Apply: https://www.xing.com/jobs/ulm-praxissemester-werkstudent-ki-data-science-157353273
    {
        "folder": "NewTec Ulm Praxissemester Werkstudent KI Data Science",
        "company": "NewTec GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Datenbanken und KI Anwendungsfaelle | Python + SQL + LangGraph",
        "role_strip": "Praxissemester Werkstudent KI und Data Science",
        "cl_date": "22. August 2026",
        "cl_subject": "Praxissemester Werkstudent KI und Data Science am Standort Ulm",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Datenbankabfragen, Machine Learning Pipelines und KI Anwendungsfaellen fuer den Unternehmensalltag. Ich habe eine Real Time Flight Tracking Pipeline mit SQL nahen dbt Modellen auf Google Cloud gebaut und in einem Multi Agent RAG System KI Anwendungsfaelle end to end von der Idee bis zur Auswertung umgesetzt. Sicher in Python, SQL, dbt, BigQuery sowie in der abteilungsuebergreifenden Zusammenarbeit mit Fachexpertinnen und Fachexperten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_FLIGHT_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_GOOGLE_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Praxissemester beziehungsweise die Werkstudententaetigkeit im Bereich KI und Data Science am Standort Ulm bei der NewTec GmbH. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die in der Ausschreibung genannte Kombination aus dem Entwickeln und Optimieren von Datenbankabfragen mit SQL und dem Sammeln praktischer Erfahrung mit hausinterner KI fuer neue Anwendungsfaelle im Unternehmensalltag, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meiner Real Time Flight Tracking Pipeline habe ich Python Collectors auf der OpenSky Network API mit PySpark Cleaning auf Google Cloud gegen Flughafen, Flugzeug und Wetterdaten ueber vier Datenquellen zu einer sauberen Join Tabelle mit ueber 128 tausend Datensaetzen zusammengefuehrt und die Daten mit dbt in analysebereite, SQL nahe Tabellen modelliert. Das Gesamtsystem laeuft alle 15 Minuten unbeaufsichtigt auf Apache Airflow mit GCS und Dataproc, und die Ergebnisse liegen in einem Tableau Workbook mit Python Statistik ueber TabPy, das die Erkenntnis freilegte, dass der Flugverkehr bei starkem Regen um das 4,4 fache abnimmt. Genau dieses Muster, saubere Datenbankabfragen als Grundlage fuer verlaessliche Auswertungen, laesst sich direkt auf neue interne Datenanalysen bei NewTec uebertragen.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen Policy Korpus in Englisch oder Deutsch end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports. Genau dieses Muster, von der ersten Idee fuer einen KI Anwendungsfall bis zu einer messbaren Auswertung, deckt sich mit der in der Ausschreibung beschriebenen praktischen Arbeit an hausinterner KI und neuen Anwendungsfaellen fuer den Unternehmensalltag.",
            "Ich arbeite sicher in Python, SQL, dbt und BigQuery sowie in der Zusammenarbeit mit Fachexpertinnen und Fachexperten aus unterschiedlichen Bereichen und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die AWS Academy Cloud Foundations, Google Data Analytics und SAS Certified Specialist Visual Business Analytics Using SAS Viya Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Team vollstaendig auf Deutsch moeglich bleibt. Ich kann als Praxissemester oder Werkstudent mit mindestens 16 Stunden pro Woche in Ulm einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. AKDB, Anstalt fuer Kommunale Datenverarbeitung in Bayern, Muenchen
    # Werkstudent AI and Machine Learning, NLP and Semantic Search (m/w/d)
    # StepStone, posted approximately 1 day ago, verified listing.
    # Teilzeit, up to 20h/week, studienfreundliche Arbeitszeiten.
    # Stack: text embeddings, semantic search, TensorFlow, PyTorch,
    # scikit learn, Hugging Face, OpenAI, Sentence BERT, FAISS, Weaviate,
    # Milvus, Pinecone.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-AI-and-Machine-Learning-NLP-and-Semantic-Search-m-w-d-Muenchen-Anstalt-fuer-Kommunale-Datenverarbeitung-in-Bayern-AKDB--14368530-inline.html
    {
        "folder": "AKDB Muenchen Werkstudent AI Machine Learning NLP Semantic Search",
        "company": "Anstalt fuer Kommunale Datenverarbeitung in Bayern",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | RAG und Semantische Suche | Python + LangGraph + Pinecone",
        "role_strip": "Werkstudent AI and Machine Learning, NLP and Semantic Search",
        "cl_date": "22. August 2026",
        "cl_subject": "Werkstudent AI and Machine Learning, NLP and Semantic Search am Standort Muenchen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Wissensdatenbanken auf Basis von Text Embeddings und semantischer Suche. Ich habe ein Multi Agent RAG System gebaut, das Embeddings und Retrieval in einen geteilten mehrsprachigen Vektorraum mit Pinecone migriert und eine hybride BM25 plus Dense Retrieval Pipeline ueber 14 Dokumente betreibt. Sicher in Python, Vektordatenbanken, Embedding Modellen und im Uebersetzen fachlicher Anforderungen in technische Loesungsansaetze.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI and Machine Learning mit Schwerpunkt NLP und Semantic Search am Standort Muenchen bei der Anstalt fuer Kommunale Datenverarbeitung in Bayern. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Aufgabe, eine Wissensdatenbank auf Basis von Text Embeddings aufzubauen und eine semantische Suche fuer Personal und Fachdokumente zu unterstuetzen, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein English Only Retrieval System mit hybrider BM25 plus Dense Retrieval Pipeline auf einen geteilten mehrsprachigen Vektorraum mit paraphrase multilingual MiniLM L12 v2 migriert, sodass eine deutsche Anfrage englische Quellen findet und end to end auf Deutsch beantwortet wird, alles ueber Pinecone als Vektordatenbank orchestriert. Ein LanguageAgent zentralisiert die Spracherkennung mit einer Konfidenzschwelle und steuert die Ausgabesprache fuer jede nachgelagerte Komponente, waehrend ein JudgeAgent Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet. Genau dieses Muster, roh Dokumente ueber Embeddings in eine durchsuchbare Wissensbasis zu verwandeln, deckt sich direkt mit dem Aufbau einer semantischen Suche fuer fachliche Spezifikationen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut und den Silver Layer mit Schema Enforcement, sicherer Typkonvertierung und Deduplizierung ueber Window Functions gehaertet. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren mit einem 3 Pass Outlier System belastbar gemacht, was einen ehrlichen R Quadrat Wert von 0,86 bei geloestem Sauerstoff freilegte. Die Kombination aus sauberer Architektur, Dokumentation von Systemaufbau und Datenmodellen sowie einem ehrlichen Evaluationsblick deckt sich mit dem, was die intelligente Dokumentenanalyse und die Anforderungsabstimmung mit Requirements Engineers braucht.",
            "Ich arbeite sicher in Python, LangGraph, Pinecone sowie in Embedding Modellen und im Uebersetzen fachlicher Anforderungen in technische Loesungsansaetze. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ich moechte an dieser Stelle offen sein, dass mein Deutschniveau bei B1 laufend liegt und ich damit unter der ausgeschriebenen verhandlungssicheren C1 Marke liege, arbeite jedoch aktiv daran und lese englischsprachige Fachliteratur sowie technische Dokumentation sicher. Ich kann als Werkstudent in Muenchen mit flexiblen, studienfreundlichen Arbeitszeiten bis zu 20 Stunden pro Woche einsteigen. Gerne bespreche ich meinen Beitrag zum Aufbau der semantischen Suche in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Boellhoff Gruppe, Bielefeld
    # Masterarbeit mit optionalem Praktikum / Werkstudententaetigkeit im
    # Bereich AI driven Patent Analytics (m/w/d)
    # Company career page jobs.boellhoff.com, also mirrored on a university
    # careers PDF. Abteilung Patentwesen. Stack: Python, Machine Learning,
    # Power BI, Data Preprocessing, LLM Feintuning, RAG, NLP, Time Series,
    # graphische ML Modelle.
    # Apply: https://jobs.boellhoff.com/Masterarbeit-mit-optionalem-Praktikum-Werkstudententaetigk-de-j5807.html
    {
        "folder": "Boellhoff Bielefeld Masterarbeit AI Patent Analytics",
        "company": "Boellhoff Gruppe",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | RAG und LLM Feintuning fuer Textanalyse | Python + LangGraph + scikit learn",
        "role_strip": "Masterarbeit AI driven Patent Analytics",
        "cl_date": "22. August 2026",
        "cl_subject": "Masterarbeit im Bereich AI driven Patent Analytics am Standort Bielefeld",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung an der Schnittstelle von Retrieval Augmented Generation, LLM Evaluation und Zeitreihenanalyse. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama gebaut, das Dokumente ueber eine hybride BM25 plus Dense Retrieval Pipeline durchsucht, und in einem regulierten Kredit Scoring System SHAP getriebene Subgruppenanalyse fuer die Erkenntnisgewinnung aus komplexen Datensaetzen eingesetzt. Sicher in Python, scikit-learn, LangGraph und im Uebersetzen unstrukturierter Textdaten in belastbare Kennzahlen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Masterarbeit mit optionalem Praktikum oder Werkstudententaetigkeit im Bereich AI driven Patent Analytics am Standort Bielefeld bei der Boellhoff Gruppe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Aufgabe, mit KI gestuetzten Methoden Erkenntnisse aus Patentdaten zu gewinnen und Technologie Trends vorherzusagen, weil ich in den letzten Monaten genau an dieser Schnittstelle von Retrieval, Textanalyse und ehrlicher Auswertung Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente umfassenden Korpus in Englisch oder Deutsch end to end beantwortet. Die Retrieval Pipeline kombiniert BM25 mit Dense Retrieval ueber einen geteilten Vektorraum, und ein EvalAgent liefert 5 Retrieval Metriken wie hit at k, precision at k und nDCG at k sowie 4 Generation Metriken pro Sprache in JSON und Markdown Reports. Genau dieses Muster, aus einem grossen unstrukturierten Textkorpus systematisch und messbar Erkenntnisse zu gewinnen, laesst sich direkt auf die statistische und semantische Analyse bibliografischer und inhaltlicher Patentdaten uebertragen.",
            "In CreditIQ habe ich mit SHAP getriebener Subgruppenanalyse eine versteckte intersektionelle Verzerrung ueber Alter und Geschlecht in einem Kredit Scoring Modell aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert, was den Disparate Impact von 0,79 auf 0,88 gehoben hat. Bei eRay GmbH habe ich zusaetzlich sechs Kandidatenmodelle von Ridge bis CatBoost fuer eine Zeitreihenaufgabe benchmarkt und mich fuer CatBoost MultiQuantile mit asymmetrischen 80 Prozent Vorhersageintervallen entschieden. Die Kombination aus Mustererkennung in komplexen Datensaetzen, Zeitreihenanalyse und einem ehrlichen, nachvollziehbaren Evaluationsblick deckt sich mit dem, was die Analyse und Vorhersage von Technologie Trends aus Patentdaten braucht.",
            "Ich arbeite sicher in Python, scikit-learn, LangGraph sowie in Data Preprocessing und Time Series Modellen und bringe erste Beruehrungspunkte mit LLM Feintuning und RAG aus meinen eigenen Projekten mit. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Team vollstaendig auf Deutsch moeglich bleibt. Als Masterstudent an der SRH Heidelberg kann ich die Masterarbeit nach vorheriger Absprache mit der Fachabteilung in Bielefeld beginnen. Gerne bespreche ich den genauen Titel und inhaltlichen Umfang der Arbeit in einem persoenlichen Gespraech.",
        ],
    },
]
