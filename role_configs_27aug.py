"""Role configurations for the 27 August 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 4 rows in status
'drafted' at run start (Reply Deutschland SE, Rohde und Schwarz, Volkswagen
Group, Kaufland, all from the 26 August 2026 run). CSV in agreement, no
status drift found on any row. Two CSV rows had no Notion counterpart
(Mercedes-Benz Group KI Kommunikationsdaten Masterarbeit, Deutsche Bank TDI
Internship) and were created in Notion with the CSV status, never the
reverse direction. 4 drafted falls under the 28 July 2026 gate's under 8
tier, so this run uses the normal top 3 to 5 cut; 4 new roles drafted.

Search targeting per the 26 August 2026 narrowing in master-projects.md:
AI Engineer and AI Evaluation only. All four roles below are agentic AI,
LLM engineering, or AI evaluation flavored, not plain Data roles.

Platform mix this run:
  - Company Page: 3 (SAP careers, Mercedes-Benz Group via Xing listing that
    resolves to the company's own Werkstudent programme, KOSTAL career
    site)
  - StepStone: 1 (Cinemo GmbH)

Freshness order per 12 July 2026 priority rule within the Germany tier:
  1. Cinemo GmbH Karlsruhe Working Student GenAI / LLM Evaluation, Agentic
     AI / NLP (f/m/d), posted about 1 week ago on StepStone, Werkstudent,
     EN track
  2. SAP Berlin Working Student (f/m/d) Signavio Next Development, Agentic
     AI, live posting on jobs.sap.com, Werkstudent, EN track
  3. Mercedes-Benz Group Sindelfingen Werkstudent*in Applied AI and Process
     Automation, live posting via Xing sourced from the company's own
     careers portal, start October 2026, Werkstudent, DE track
  4. KOSTAL Luedenscheid Werkstudent fuer KI Entwicklung, Artificial
     Intelligence Development, live posting on kostal-career.com,
     Werkstudent, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Cinemo posting body written entirely in English -> EN track.
  2. SAP posting body written entirely in English (title bilingual
     Working Student / Werkstudent per SAP's standard dual language
     listing convention, body text is English) -> EN track.
  3. Mercedes-Benz Group posting body written in German -> DE track.
  4. KOSTAL posting body written in German, "Gute Englischkenntnisse,
     gute Deutschkenntnisse willkommen" (English required, German
     welcome not required) -> DE track since the posting body itself is
     German; Rah's B1 in progress level is noted as sufficient given
     German is only welcome, not a hard requirement, flagged in the
     digest transparency block for completeness.

Apply method transparency: Cinemo's listing is hosted and reached entirely
on stepstone.de with a "Schnelle Bewerbung" style flow, tentatively
platform-native pending OpenClaw's on click verification per its scope
rule. SAP (jobs.sap.com), Mercedes-Benz Group (resolves off Xing to the
company's own Werkstudent application flow), and KOSTAL
(kostal-career.com) all land on the employer's own careers domain, so all
three are company-portal, out of OpenClaw's automated submission scope;
Rah submits those three manually. Noted per role below and in the digest.

Dedup check against applied-log.csv and Notion: Cinemo GmbH, SAP Signavio
Next Development Agentic AI, Mercedes-Benz Group Applied AI and Process
Automation, and KOSTAL are all new company plus role combinations, never
previously logged. SAP and Mercedes-Benz Group both already appear in the
log for many other distinct roles, allowed under the 'different roles at
the same company' rule.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses/brackets in bullets, Languages EN+DE only (no Hindi),
German level locked to 'German: B1, in progress' / 'Deutsch: B1, laufend'
on the respective track, no page numbers/headers/footers, 2 page hard
cap, Ojas style header (name, tag, contact lines, italic status), Skills
grouped into functional buckets, positioning tag under the name is a
pitch not the posting title, and banned strings on the validation gate
are met by the new header.
"""

from role_configs import (
    ERAY_BULLETS_EN,
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_EN,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA,
    CERT_NVIDIA_DE,
    CERT_AWS,
    CERT_AWS_DE,
    CERT_SAS,
    CERT_SAS_DE,
    CERT_GOOGLE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_RAG_DE,
    P_CREDITIQ_EN,
    P_FLIGHT_EN,
    P_FLIGHT_DE,
    P_MOVIE_DE,
)


CONFIGS_27AUG = [
    # 1. Cinemo GmbH, Karlsruhe
    # Working Student - GenAI / LLM Evaluation - Agentic AI / NLP (f/m/d)
    # StepStone, posted about 1 week ago, Werkstudent, EN track
    # Tasks: support evaluation and validation of agentic AI systems and
    # GenAI algorithms for NLP powering in-car experiences, build
    # datasets, extend evaluation tooling, contribute to end to end
    # testing workflows for non deterministic AI components across
    # cloud services and in vehicle platforms (AAOS, Linux).
    # Requirements: ongoing Bachelor's or Master's in CS, AI/ML, Data
    # Science or Computational Linguistics, Python, basic ML/NLP,
    # interest in GenAI/LLMs, agentic systems, evaluation of non
    # deterministic AI behavior, dataset creation, testing concepts a
    # plus, good English.
    # Apply: https://www.stepstone.de/stellenangebote--Working-Student-GenAI-LLM-Evaluation-Agentic-AI-NLP-f-m-d-Karlsruhe-Germany-Cinemo-GmbH--13887266-inline.html
    # Apply method: platform-native tentative, StepStone hosted listing,
    # pending OpenClaw on click verification
    {
        "folder": "Cinemo Karlsruhe Working Student GenAI LLM Evaluation Agentic AI NLP",
        "company": "Cinemo GmbH",
        "lang": "en",
        "tag": "Data Science Master's Student | LLM Evaluation and Agentic AI Testing | Python + LangGraph + Eval Harness",
        "role_strip": "Working Student, GenAI / LLM Evaluation, Agentic AI / NLP",
        "cl_date": "27 August 2026",
        "cl_subject": "Working Student, GenAI / LLM Evaluation, Agentic AI / NLP in Karlsruhe",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building and evaluating agentic AI and LLM systems end to end. I built a multi agent RAG system with an LLM as Judge evaluator scoring answers on 5 dimensions in JSON mode at temperature 0, and a paired retrieval and generation evaluation harness computing 9 metrics on a labelled EN and DE eval set. Comfortable across Python, LangGraph, dataset construction, and automated evaluation tooling for non deterministic AI components.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_CREDITIQ_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in GenAI / LLM Evaluation, Agentic AI / NLP at Cinemo in Karlsruhe. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of evaluating agentic AI systems, building evaluation datasets, and contributing to end to end testing of non deterministic AI components maps very closely to the evaluation harness work I have shipped over the last several months.",
            "In my Multi Agent RAG project I built a LangGraph orchestrated agent system and implemented a JudgeAgent that scores answers on 5 dimensions, groundedness, relevance, completeness, citation quality, and language quality, in JSON mode at temperature 0. I eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B, with a self_judged flag propagated into every report and a hard failure on a missing judge model so a silent fallback cannot regress unnoticed. I also built an EvalAgent computing 5 retrieval metrics and 4 generation metrics aggregated overall and per language into JSON and Markdown reports on a paired EN and DE labelled eval set, which is the same category of dataset and evaluation tooling work described in your posting.",
            "In CreditIQ I applied AIF360 mitigation and SHAP driven subgroup analysis to a regulated credit scoring model, and backed the pipeline with unit tests at 100 percent branch coverage plus a full regulatory write up. That discipline of treating a non deterministic or high stakes system as something that must be measured, tested, and documented rather than shipped on vibes is the same mindset your posting describes for ensuring GenAI and agentic components are measurable and reliable before reaching real world automotive environments.",
            "I work comfortably in Python, LangGraph, and basic ML and NLP concepts, and I am comfortable with dataset creation, labelling, preprocessing, and quality checks from my evaluation harness work. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Karlsruhe as a working student and would welcome the chance to discuss how I could contribute to your GenAI / LLM team.",
        ],
    },

    # 2. SAP, Berlin
    # Working Student (f/m/d) - Signavio Next Development - Agentic AI
    # jobs.sap.com career page, live posting, Werkstudent, EN track
    # Tasks: work in a senior engineering team building software with
    # real customer and internal impact on Signavio Next, agentic AI
    # development work area Software-Design and Development.
    # Requirements: student status, limited part time, hybrid, standard
    # SAP working student application documents (cover letter, resume,
    # enrollment certificate, transcript).
    # Apply: https://jobs.sap.com/job/Berlin-Working-Student-%28fmd%29-Signavio-Next-Development-Agentic-AI-10557/1419810733
    # Apply method: company-portal (jobs.sap.com career site)
    {
        "folder": "SAP Berlin Working Student Signavio Next Development Agentic AI",
        "company": "SAP",
        "lang": "en",
        "tag": "Data Science Master's Student | Agentic AI Systems | Python + LangGraph + LLM Tooling",
        "role_strip": "Working Student, Signavio Next Development, Agentic AI",
        "cl_date": "27 August 2026",
        "cl_subject": "Working Student, Signavio Next Development, Agentic AI in Berlin",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building agentic AI systems end to end. I built a multi agent RAG system orchestrated in LangGraph with a LanguageAgent, a JudgeAgent, and an EvalAgent working together over a shared vector space, and delivered a recursive time series pipeline at eRay GmbH with a full orchestrator layer including gate checks and ecological clips. Comfortable across Python, LangGraph, agent orchestration, and production minded software engineering from two years of full time front end experience.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_FLIGHT_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position on Signavio Next Development, Agentic AI at SAP in Berlin. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the opportunity to work in a senior engineering team building agentic AI software with real customer impact maps closely to the multi agent systems I have designed and shipped over the last several months.",
            "In my Multi Agent RAG project I built a LangGraph orchestrated agent system where a LanguageAgent centralises language detection and propagates an output language directive to every downstream agent, a JudgeAgent scores answers on 5 dimensions in JSON mode at temperature 0 using a separate model from the generator to eliminate self preference bias, and an EvalAgent aggregates 9 retrieval and generation metrics into structured reports. I refactored the system with a config.yaml loader and a build_pipeline factory so importing the orchestrator no longer requires external credentials, the same production hygiene that keeps a multi agent system maintainable as it grows.",
            "In my Real Time Flight Tracking pipeline I built Python collectors polling an external API every 30 seconds with PySpark cleaning that joins four data sources into a table of over 128 thousand records, then orchestrated the whole system with Apache Airflow so it refreshes automatically every 15 minutes without operator intervention. That experience building reliable, automated systems that other engineers can extend, alongside a two year full time background in React inside a module federation setup with Playwright end to end tests, is directly transferable to contributing production ready agentic AI features inside an established engineering team.",
            "I work comfortably in Python, LangGraph, SQL, and cloud platforms, and I have prepared the standard application documents including a certificate of enrollment and current transcript. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Berlin as a working student in a hybrid setup and would welcome the chance to discuss how I could contribute to the Signavio Next Agentic AI team.",
        ],
    },

    # 3. Mercedes-Benz Group, Sindelfingen
    # Werkstudent*in Applied AI & Process Automation
    # Xing listing sourced from the company's own Werkstudent programme,
    # start October 2026, hybrid (remote plus on site workshops in
    # Stuttgart), Werkstudent, DE track
    # Tasks: ITO/CA Change Team supporting the worldwide MES rollout,
    # combining AI agents into scalable workflow solutions, driving AI
    # adoption across teams rather than only talking about AI.
    # Requirements: student status, interest in workflow thinking and
    # combining agents into scalable solutions, start from October 2026.
    # Apply: https://www.xing.com/jobs/sindelfingen-werkstudent-applied-ai-process-automation-156857505
    # Apply method: company-portal (resolves to the Mercedes-Benz Group
    # careers portal)
    {
        "folder": "Mercedes-Benz Group Sindelfingen Werkstudent Applied AI Process Automation",
        "company": "Mercedes-Benz Group",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentic AI und Prozessautomatisierung | Python + LangGraph + Workflow Automation",
        "role_strip": "Werkstudent Applied AI und Process Automation",
        "cl_date": "27. August 2026",
        "cl_subject": "Werkstudent Applied AI und Process Automation am Standort Sindelfingen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau agentischer KI Systeme und in der Automatisierung end to end Workflows. Ich habe ein Multi Agent RAG System gebaut, in dem mehrere spezialisierte Agenten zu einer skalierbaren Loesung kombiniert werden, und bei eRay GmbH eine vollautomatisierte Orchestrierungsschicht mit Gate Checks entwickelt. Sicher in Python, LangGraph, Workflow Automatisierung und im Uebersetzen von KI Moeglichkeiten in konkreten Team Impact.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_GOOGLE_DE, CERT_SAS_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Applied AI und Process Automation im Change Team am Standort Sindelfingen ab Oktober 2026. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Denkweise, in Workflows statt in einzelnen Tools zu denken und Agenten zu skalierbaren Loesungen zu kombinieren, weil ich in den letzten Monaten genau an dieser Schnittstelle gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, in dem eine LanguageAgent Komponente zentral die Sprachsteuerung uebernimmt, ein JudgeAgent Antworten auf 5 Dimensionen im JSON Modus bewertet und ein EvalAgent die Ergebnisse aggregiert, und das Ganze ueber ein build_pipeline Factory Pattern von externen Credentials entkoppelt. Genau diese Faehigkeit, mehrere spezialisierte Agenten zu einem robusten Gesamtsystem zu kombinieren, deckt sich mit der in der Ausschreibung beschriebenen Aufgabe, AI effektiv im Team einzusetzen statt nur darueber zu reden.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Medaillon Architektur mit vollautomatisiertem Cloud Scheduler Trigger und 0 manuellen Eingriffen gebaut. Bei eRay GmbH habe ich zusaetzlich eine end to end Orchestrierungsschicht mit Gate Checks und oekologischen Grenzwerten entwickelt, die das Gesamtsystem robust gegen fehlerhafte Eingaben macht. Diese Erfahrung mit automatisierten, unbeaufsichtigt laufenden Systemen deckt sich direkt mit der in der Ausschreibung beschriebenen Skalierung von Manufacturing Execution Systemen ueber Workflow Automatisierung.",
            "Ich arbeite sicher in Python, LangGraph und Workflow Automatisierung und nutze ChatGPT und Claude aktiv im Alltag. Ich halte die AWS Academy Cloud Foundations, Google Data Analytics und SAS Certified Specialist Visual Business Analytics Using SAS Viya Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann die Werkstudententaetigkeit ab Oktober 2026 in einem hybriden Modell mit Praesenztagen in Stuttgart antreten. Gerne bespreche ich meinen Beitrag zum Change Team in einem persoenlichen Gespraech.",
        ],
    },

    # 4. KOSTAL (Leopold KOSTAL GmbH und Co. KG), Luedenscheid
    # Werkstudent fuer KI-Entwicklung / Artificial Intelligence
    # Development (m/w/d)
    # kostal-career.com, live posting, Werkstudent, DE track
    # Tasks: Weiterentwicklung der AI/LLM Landschaft in hybrider Umgebung,
    # Aufbau und Pflege von AI Workflows und internen Assistants,
    # Erstellung, Test und Versionierung von System Prompts und Prompt
    # Templates, Implementierung von Daten und Inferenzpipelines (ETL,
    # Embeddings, Vektorspeicher), Anbindung und Integration zur
    # Entwicklung und Orchestrierung von AI Agenten, Monitoring,
    # Telemetrie und automatisierte Evaluation (Qualitaet, Kosten,
    # Performance).
    # Requirements: laufendes Studium Informatik, Data Science,
    # Elektrotechnik, Mathematik oder vergleichbar, gute Python
    # Kenntnisse, erste Erfahrung mit LLMs/GenAI (Prompting, RAG,
    # Evaluation) und REST APIs, Grundlagen Docker/Kubernetes, Git/CI/CD,
    # gute Englischkenntnisse, gute Deutschkenntnisse willkommen.
    # Pay: 15 EUR/hour for all Werkstudent positions per posting.
    # Apply: https://www.kostal-career.com/en-DE/career/werkstudent-fuer-ki-entwicklung-/-artificial-intelligence-development-m/w/d
    # Apply method: company-portal (kostal-career.com career site)
    {
        "folder": "KOSTAL Luedenscheid Werkstudent KI Entwicklung Artificial Intelligence Development",
        "company": "Leopold KOSTAL GmbH und Co. KG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | LLM Landschaft und KI Agenten | Python + RAG + Evaluation und Monitoring",
        "role_strip": "Werkstudent fuer KI Entwicklung, Artificial Intelligence Development",
        "cl_date": "27. August 2026",
        "cl_subject": "Werkstudent fuer KI Entwicklung, Artificial Intelligence Development am Standort Luedenscheid",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von AI und LLM Landschaften, Prompt Engineering, Inferenzpipelines und automatisierter Evaluation. Ich habe ein Multi Agent RAG System mit Embeddings, Vektorspeicher und einer automatisierten Evaluationsschicht ueber Qualitaet und Kosten gebaut und bei eRay GmbH eine Orchestrierungsschicht mit Monitoring und Gate Checks entwickelt. Sicher in Python, REST APIs, Docker, Git und CI/CD sowie im praktischen Einsatz von LLMs und GenAI Tooling.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI Entwicklung, Artificial Intelligence Development am Standort Luedenscheid. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus der Weiterentwicklung einer AI und LLM Landschaft, dem Aufbau interner AI Workflows und Assistants sowie automatisierter Evaluation von Qualitaet, Kosten und Performance, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich Embeddings und Vektorspeicher in einer paraphrase multilingualen MiniLM L12 v2 Repraesentation aufgebaut und einen JudgeAgent implementiert, der Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet, mit einem EvalAgent, der 9 Retrieval und Generation Metriken pro Sprache in JSON und Markdown Reports aggregiert. Diese praktische Erfahrung mit Daten und Inferenzpipelines, Embeddings und automatisierter Evaluation deckt sich direkt mit der in der Ausschreibung beschriebenen Implementierung von ETL, Embeddings und Vektorspeicher sowie automatisierter Evaluation von KI Systemen.",
            "Bei eRay GmbH habe ich eine end to end Orchestrierungsschicht mit Gate Checks, oekologischen Grenzwerten und einer Geschwindigkeitsbegrenzung entwickelt, die das Gesamtsystem robust gegen fehlerhafte Eingaben und Sensorausfaelle macht, und in meinem Cloud Data Projekt Monitoring und Data Quality Checks in eine vollautomatisierte Pipeline integriert. Diese Erfahrung mit Monitoring, Telemetrie und dem Betrieb von KI Systemen im Produktivbetrieb deckt sich mit der in der Ausschreibung beschriebenen Aufgabe im Bereich DevOps und MLOps.",
            "Ich arbeite sicher in Python, REST APIs, Docker, Git und CI/CD und nutze ChatGPT und Claude aktiv im Alltag beim Prompting und bei der Arbeit mit RAG Systemen. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Ich kann die Werkstudententaetigkeit in Luedenscheid antreten. Gerne bespreche ich meinen Beitrag zu Ihrer AI und LLM Landschaft in einem persoenlichen Gespraech.",
        ],
    },
]
