"""Role configurations for the 21 August 2026 job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 4 rows in status
'drafted' at run start (Sana HR Solutions GmbH Werkstudent Data Engineer,
Robert Bosch GmbH Masterarbeit Agentisches KI System REF293881R, FLEX
Capital Management GmbH Werkstudent Data Science and AI, and Amprion GmbH
Werkstudent KI Stellen ID 7959). Under 8 drafted falls in the normal top 3
to 5 tier under the 28 July 2026 yield reset.

IMPORTANT transparency note: three of those four Notion rows (Sana HR
Solutions, Robert Bosch Masterarbeit, FLEX Capital Management) carry a
Notion createdTime of 2026-08-21 11:48:15Z, roughly 16 minutes before this
run started, but have NO matching row in applied-log.csv and NO matching
folder under drafts/ in this checkout, and `git log` shows no commits
today. This strongly suggests a concurrent or very recently interrupted
Cowork run wrote to Notion but never reached the CSV write, commit, or
push steps. Per invariant #1 Notion is not reversed from this run (the
CSV only walks its own rows per Step 3), and per invariant #2 git remains
the source of truth for content, so this run does not fabricate draft
folders for those three roles. Flagged plainly in the digest for Rah to
check for a duplicate/stuck session.

Reconciliation this run (Step 3, full applied-log.csv sweep against
Notion, not just the tail rows): 32 CSV rows updated from stale statuses
to their true Notion Status. The 6 rows drafted on 20 Aug were rechecked:
Amprion Werkstudent KI Stellen-ID 7959 matched Notion (still drafted, no
change), Ed. Zueblin AG moved to applied, PwC Deutschland moved to
applied, Bosch Rexroth AG moved to applied, Ardex GmbH moved to Not
listed Anymore, Amprion Masterarbeit Initiativbewerbung KI und
Wissensmanagement moved to applied. The remaining 27 drifted rows were
older entries that had gone from applied to rejected in Notion (OpenClaw
or Rah's manual review outcomes) without the CSV mirror catching up.
CSV is now aligned with Notion. No CSV row was missing a Notion
counterpart (the earlier apparent mismatch on Ärzteverband Deutscher
Allergologen was a Unicode normalisation artifact in the diff script, not
real drift).

Search process this run: extensive search across LinkedIn, StepStone,
Xing, and company career pages. Several strong looking leads were found
and dropped before drafting, honestly logged here rather than silently
excluded:
  - Delivery Hero Working Student Data Engineering (Vendor), Berlin: the
    company careers page itself states "This vacancy has expired." Not
    drafted, per invariant #3 never draft a dead listing.
  - MEAG MUNICH ERGO Werkstudent Data Enablement, Muenchen: StepStone
    shows the apply button as "Nicht verfuegbar" (not available), a
    closed-listing signal. Also requires German and English at least B2.
    Not drafted.
  - Vecrion AI Werkstudent Generative AI, Agentic Systems: LinkedIn lists
    the company location as Indiana, United States, outside the Germany
    or remote-EU scope. Not drafted.
  - AKDB Werkstudent AI and Machine Learning NLP and Semantic Search,
    Muenchen: requires verhandlungssichere Deutschkenntnisse mindestens
    C1. Large gap versus Rah's current B1. Watchlisted, not drafted.
  - statworx Werkstudent Automation and AI, Frankfurt: still live on the
    company's own Personio careers page (contradicting an aggregator's
    stale "3 months ago" tag), but requires sehr gute Deutsch und
    Englischkenntnisse mindestens auf C1-Niveau. Watchlisted, not
    drafted.
  - 50Hertz Transmission Werkstudentin Data Analytics und Konzepte im
    EU-Strommarkt, Berlin: requires gute Deutschkenntnisse B2. Above B1.
    Watchlisted, not drafted.
  - Novo AI Data Engineer Intern (Pflichtpraktikum), Hannover/Frankfurt:
    LinkedIn required login to read the job description, could not
    verify content, not drafted to avoid guessing at requirements.
  - XING frankfurt-main-werkstudent-data-scientist-152990082 (aviation
    and facility services Data Scientist Werkstudent): XING itself
    returns "This job ad isn't available." Not drafted.
  - PIMCO Prime Real Estate/Allianz Intern Software and Data Engineering,
    Muenchen (XING): page rendered with empty task and requirement
    sections (JS-gated content), could not verify, not drafted.
  - Indeed: the Indeed MCP tool was not available in this session's tool
    set this run; Indeed sourcing was skipped rather than substituted
    with an unverified web fetch. Noted as a source gap in the digest.

Platform mix for this run: StepStone 2 (BCG Platinion, Arthrex), all
other sources 0. This is a narrower mix than the 28 July yield target
because every LinkedIn and Xing lead that looked promising this run
turned out expired, login-walled, or otherwise unverifiable; flagged
plainly rather than padded with a weaker pick.

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. BCG Platinion Werkstudent AI & Data Analytics, Energy Knowledge
     Management, Muenchen, posted about 17 hours ago on StepStone,
     Werkstudent, DE track (posting body in German)
  2. Arthrex GmbH Working Student Business Analytics & Process
     Optimization, Muenchen, posted about 2 days ago on StepStone,
     Werkstudent, EN track (posting body in English)

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. BCG Platinion posting body entirely in German ("Praege die Welt von
     morgen", "Du machst den Unterschied") -> DE track. No explicit CEFR
     level stated, only "gute Kommunikationsfaehigkeiten in Deutsch und
     Englisch" -> Notion German Level set to none, flagged in Notes.
  2. Arthrex posting body entirely in English ("Your Tasks", "Your
     Qualifications") despite being a Munich based company -> EN track.
     Requires "business-fluent German proficiency", no explicit CEFR
     level stated but reads as roughly B2 or above -> Notion German
     Level set to B2, gap versus Rah's B1 disclosed openly in the cover
     letter per the same honesty pattern used in the 13 Aug CHECK24 and
     BMW drafts.

Dedup check against applied-log.csv and Notion:
  - BCG Platinion: never applied. New company.
  - Arthrex GmbH: never applied. New company (Munich founded medical
    device firm, HQ now Naples FL).

Both tag as Werkstudent / Working Student; both in-scope target roles
under the master-projects.md Werkstudent / part time work type.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses/brackets in bullets, Languages EN+DE only (no Hindi),
German level locked to 'German: B1, in progress' on EN track and
'Deutsch: B1, laufend' on DE track, no page numbers/headers/footers, 2
page hard cap, Ojas style header (name, tag, contact lines, italic
status), Skills grouped into functional buckets, positioning tag under
the name is a pitch not the posting title, and banned strings on the
validation gate are met by the new header.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS,
    CERT_AWS_DE,
    CERT_SAS,
    CERT_GOOGLE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_DE,
    P_MOVIE_EN,
    P_MOVIE_DE,
    P_TABLEAU_EN,
    P_CLIMATE_EN,
)


CONFIGS_21AUG = [
    # 1. BCG Platinion, Muenchen
    # Werkstudent:in AI & Data Analytics - Energy Knowledge Management (all genders)
    # StepStone, posted about 17 hours ago. Homeoffice moeglich, Teilzeit.
    # Energy Practice Area, feasibility studies and agentic development of
    # AI and Analytics applications, market and technology trend research,
    # training materials for consultants. DE track.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-in-AI-Data-Analytics-Energy-Knowledge-Management-all-genders-Muenchen-BCG-Platinion--14369735-inline.html
    {
        "folder": "BCG Platinion Muenchen Werkstudent AI Data Analytics Energy Knowledge Management",
        "company": "BCG Platinion",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Analytics Prototyping | Python + LangGraph + BigQuery",
        "role_strip": "Werkstudent AI und Data Analytics, Energy Knowledge Management",
        "cl_date": "21. August 2026",
        "cl_subject": "Werkstudent AI und Data Analytics, Energy Knowledge Management",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim, mit praktischer Erfahrung im Prototyping agentischer KI und Analytics Anwendungen von der ersten Idee bis zum vorzeigbaren MVP. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B und Qwen2.5 14B gebaut und in einem Cloud Data Projekt eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run entwickelt, die vollstaendig automatisiert laeuft. Sicher in Python, SQL, LangGraph, BigQuery und aktuellen Agenten Frameworks.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI und Data Analytics im Energy Knowledge Management Team von BCG Platinion am Standort Muenchen. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich besonders die Verbindung aus Machbarkeitsstudien, agentischer Entwicklung und der Vorbereitung von Beraterinnen und Beratern auf neue KI Technologien, weil ich in den letzten Monaten genau an dieser Schnittstelle von Prototyp bis MVP gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente umfassenden Policy Korpus in Englisch und Deutsch end to end beantwortet. Ein JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports, sodass ein neuer Agent oder Chatbot Prototyp belastbar iteriert werden kann statt auf Bauchgefuehl zu laufen. Genau dieses Muster von Prototyp, Evaluation und Dokumentation laesst sich direkt auf die Machbarkeitsstudien und Trainingsmaterialien im Energy Knowledge Management Team uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run mit vollautomatisiertem Cloud Scheduler Trigger gebaut und einen BigQuery ML Klassifikator trainiert, der bewusst nur Pre Release Signale sieht, damit keine Leckage im Trainingssatz auftaucht. Das Ergebnis ist ein vorzeigbares Full Stack System von der Rohdaten Ingestion bis zum Looker Studio Dashboard, ganz ohne manuelle Eingriffe im Betrieb. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren mit CatBoost MultiQuantile geliefert, was zeigt, dass ich auch ausserhalb reiner Software Projekte in datenintensiven Branchen wie der Energiewirtschaft schnell produktiv werde.",
            "Ich arbeite sicher in Python, SQL, LangGraph, BigQuery und aktuellen Agenten Frameworks sowie in den ueblichen Cloud Plattformen AWS und GCP. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter. Als Werkstudent kann ich in Muenchen mit anteiligem Homeoffice einsteigen. Gerne bespreche ich meinen Beitrag zum Energy Knowledge Management Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Arthrex GmbH, Muenchen
    # Working Student Business Analytics & Process Optimization
    # StepStone, posted about 2 days ago. Homeoffice moeglich, Teilzeit.
    # Logistics and transportation process improvement, data analysis,
    # reporting and visualization, Salesforce/Jira/SharePoint tracking.
    # EN track (posting body entirely in English).
    # Apply: https://www.stepstone.de/stellenangebote--Working-Student-Business-Analytics-Process-Optimization-Muenchen-Arthrex-GmbH--14411716-inline.html
    {
        "folder": "Arthrex Muenchen Working Student Business Analytics Process Optimization",
        "company": "Arthrex GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | Business Analytics and Dashboards | Python + SQL + Tableau",
        "role_strip": "Working Student, Business Analytics and Process Optimization",
        "cl_date": "21 August 2026",
        "cl_subject": "Working Student, Business Analytics and Process Optimization",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience turning raw operational data into dashboards and decision support for non technical stakeholders. I built a Tableau based Fast Food Nutritional Analyzer with Set Actions and parameter driven analytics, and delivered an end to end climate economics analytics pipeline from raw CSV to a management ready report using Random Forest models and calibrated confidence statements. Comfortable across Python, SQL, Tableau and Excel for business facing reporting.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_TABLEAU_EN, P_CLIMATE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_SAS, CERT_GOOGLE, CERT_AWS],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in Business Analytics and Process Optimization at Arthrex in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of supporting digital transformation in logistics processes, building reports and visualizations for business decisions, and researching new digital tools maps closely to the analytics and dashboard projects I have shipped over the last several months.",
            "In my Fast Food Nutritional Analyzer project I built a dynamic shopping cart using Tableau Set Actions so end users can select scatter plot points and instantly total key macros for a simulated meal, and implemented parameter driven analytics with a dynamic Y axis tied to a user controlled goal parameter so the same dashboard serves two different objectives without reloading. I also authored complex order of operation IF and THEN calculated fields to flag deceptive high fat and high calorie items, which held up against manual spot checks on the source data. That same instinct for turning a pile of numbers into a decision a non technical stakeholder can act on is exactly what a logistics and process optimization dashboard needs.",
            "In my Economic Impact Analysis of Global Climate Events project I ran an end to end pipeline from raw CSV to a management ready report, cleaning outliers, missing values and inconsistent scales before training Random Forest models to trace where economic risk concentrates, then closed with calibrated confidence statements that survived a management review without further translation. I bring the same structured, source to insight discipline to project and operational process documentation, and I am comfortable tracking status across tools like Excel, PowerPoint and shared trackers similar to Salesforce, Jira or SharePoint.",
            "I work comfortably in Python, SQL, Tableau and Excel, and I am building familiarity with Power BI and Power Automate. I hold the SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics and AWS Academy Cloud Foundations certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and my German is B1 in progress; I want to be upfront that this is below the business fluent bar in the posting, and I am actively working to raise it. As a working student I can join in Munich immediately. I would welcome the chance to discuss how I could contribute to your Business Analytics and Process Optimization team.",
        ],
    },
]
