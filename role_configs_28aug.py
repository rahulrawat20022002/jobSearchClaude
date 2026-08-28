"""Role configurations for the 28 August 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 8 rows in status
'drafted' at run start (Reply Deutschland SE, Rohde und Schwarz, Kaufland,
Volkswagen Group from the 26 Aug run, plus Cinemo GmbH, Leopold KOSTAL,
SAP Signavio, Mercedes-Benz Group Applied AI from a 27 Aug run that had
pushed to an unmerged branch, claude/adoring-dijkstra-lnbu2v, and was
fast-forward merged into this run's branch during reconciliation so the
repo, the source of truth for content, matches what Notion already showed
as drafted). CSV was 4 rows behind Notion for those 27 Aug rows before the
merge; after merging, reconciliation found 0 further Status drift, only a
harmless umlaut normalisation non-match on Ärzteverband Deutscher
Allergologen that both sides already agree is 'applied'. 8 drafted falls
in the 8 to 10 tier under the 28 July 2026 yield based reset rule, which
caps this run at the top 3 newly scored roles.

Platform mix this run:
  - Company Page (Isar Aerospace SE career site via Greenhouse), found via
    general web search, 1
  - LinkedIn (Mercedes-Benz Tech Innovation GmbH posting), 1
  - LinkedIn (Siemens Healthineers AG posting, full text pulled from the
    jobs.siemens.com mirror), 1

Freshness order per 12 July 2026 priority rule within the single Germany
tier:
  1. Isar Aerospace SE, Working Student, AI Platform and Enablement,
     Parsdorf, Bavaria, posted 6 days ago, Werkstudent, EN track
  2. Mercedes-Benz Tech Innovation GmbH, Werkstudent AI Security, Research
     and Evaluation, Ulm and Karlsruhe and Stuttgart and Berlin (hybrid,
     4 locations), posted 1 week ago, Werkstudent, DE track
  3. Siemens Healthineers AG, Werkstudent KI gestuetzte Automatisierung
     bei Research and Development, Kemnath, posted 5 days ago (23 Aug
     2026), Werkstudent, DE track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. Isar Aerospace posting body written in English -> EN track.
  2. Mercedes-Benz Tech Innovation posting body written in German -> DE
     track.
  3. Siemens Healthineers posting body written in German -> DE track,
     even though the posting itself only requires "sehr gute
     Englischkenntnisse, Deutsch ist von Vorteil" (German is a plus, not
     required); the rule keys off the posting's own language, not its
     stated requirement.

Language level transparency: Isar Aerospace states no German requirement
at all (English speaking role). Mercedes-Benz Tech Innovation explicitly
asks for "nachweislich hervorragende Deutsch- und Englischkenntnisse",
provably excellent German AND English, a materially higher bar than
Rah's current B1 in progress level; flagged plainly in the digest and the
cover letter is upfront about the current level. Siemens Healthineers
asks for very good English with German merely a plus, so no German level
mismatch there despite the DE track.

Apply method transparency: Isar Aerospace's apply link is a Greenhouse
job board on the company's own domain (company-portal, out of OpenClaw's
platform-native scope). Mercedes-Benz Tech Innovation's listing was found
on LinkedIn but the underlying application flow is the company's own
Workday portal (MBTI_JOBPORTAL), so this is recorded as company-portal
with the verified LinkedIn URL kept as Apply Link since that is the
confirmed working link pulled this run. Siemens Healthineers' apply link
is the company's own jobs.siemens.com job detail page (company-portal).
All three are out of OpenClaw's automated submission scope; Rah submits
manually. Noted per role below and in the digest.

Dedup check against applied-log.csv and Notion: Isar Aerospace SE is an
entirely new company, never previously logged. Mercedes-Benz Tech
Innovation GmbH already has two prior entries (Werkstudent Data
Engineering and Data Science, rejected; Werkstudent Agentic AI und Multi
Agent Systeme, Not listed Anymore) but not this AI Security Research and
Evaluation role, allowed under the different roles at the same company
rule. Siemens Healthineers AG already has one prior entry (Working
Student, Data Science and AI for X Ray Technology, Forchheim, Not listed
Anymore) but not this KI gestuetzte Automatisierung role at a different
location (Kemnath), also allowed under the same rule.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "German: B1, in progress" on EN track and "Deutsch: B1,
laufend" on DE track, no page numbers or headers or footers, 2 page hard
cap, Ojas style header, Skills grouped into functional buckets,
positioning tag under the name is a pitch not the posting title, and
banned strings on the validation gate are met by the new header.
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
    CERT_SAS_DE,
    CERT_GOOGLE,
    CERT_GOOGLE_DE,
    ACH_USAII_EN,
    ACH_USAII_DE,
    P_RAG_EN,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_MOVIE_EN,
    P_MOVIE_DE,
)


CONFIGS_28AUG = [
    # 1. Isar Aerospace SE, Parsdorf, Bavaria
    # Working Student - AI Platform and Enablement (m/f/d)
    # Company career site via Greenhouse, posted 6 days ago, Werkstudent, EN track
    # Tasks: operate and maintain a self managed open source model inference
    # endpoint on VMs, update and manage deployed models, Docker images and
    # supporting services, configure the model gateway, track and evaluate
    # open source models and inference tooling, evaluate and integrate MCP
    # servers, REST APIs, Microsoft 365 Copilot agents and Copilot Studio.
    # Requirements: enrolled in CS, data science, software engineering,
    # information systems or related; Linux, Docker, basic service ops;
    # REST APIs and MCP server integration; Python or Bash scripting;
    # strong personal interest in AI models, developer tools, agentic
    # best practices.
    # Apply: https://job-boards.eu.greenhouse.io/isaraerospace/jobs/4958455101
    # Apply method: company-portal (Greenhouse job board on isaraerospace.com)
    {
        "folder": "Isar Aerospace Parsdorf Working Student AI Platform Enablement",
        "company": "Isar Aerospace SE",
        "lang": "en",
        "tag": "Master's Student Data Science and Analytics | Agentic AI Infrastructure and Model Evaluation | Python + LangGraph + Docker",
        "role_strip": "Working Student, AI Platform and Enablement",
        "cl_date": "28 August 2026",
        "cl_subject": "Working Student, AI Platform and Enablement in Parsdorf",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience operating self hosted LLM inference, building agentic multi agent systems, and running fully automated cloud pipelines end to end. I run a multi agent RAG system entirely on self managed Ollama inference serving Mistral 7B and Qwen2.5 14B side by side with a hard coded check against silent fallback, and I built a Cloud Run batch pipeline that requires 0 manual intervention. Comfortable with Python, Docker, Linux, REST APIs, and hands on evaluation of open source models and developer tooling.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_RAG_EN, P_MOVIE_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in AI Platform and Enablement at Isar Aerospace in Parsdorf. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the mix of operating a self managed open source model inference endpoint, tracking new models and agentic tooling, and evaluating MCP servers and Copilot style automation maps closely to the infrastructure and evaluation work I have shipped over the last several months.",
            "In my Multi Agent RAG project I stood up the full generation, judging, and evaluation stack on self hosted Ollama inference, running Mistral 7B as the generator and Qwen2.5 14B as an independent LLM as Judge on a separate model to eliminate self preference bias, with a hard failure on a missing judge model so a silent fallback to self judging cannot regress unnoticed. I also refactored the system into a build_pipeline factory so importing the orchestrator no longer requires external credentials, and cached the retriever's encoder across searches instead of reloading per query, the same instincts I would bring to keeping an inference gateway, its Docker images, and its supporting services current, reliable, and well evaluated.",
            "In my Movie Analytics and ML Pipeline project I built an end to end batch pipeline running on GCP Cloud Run behind a fully automated Cloud Scheduler trigger with 0 manual interventions, hardened the Silver layer with schema enforcement and deduplication, and secured the system with a least privilege service account and Secret Manager. That experience keeping an automated system healthy without an operator watching it lines up directly with the ask to keep an internal AI stack current and reliable while exploring new tools and agentic workflows.",
            "I work comfortably in Python, Docker, Linux, and REST APIs, and I am the person on a team who reads the release notes for the newest open source models and inference tooling before being asked to. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics certificates, and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join as a working student in Parsdorf and would welcome the chance to discuss how I could contribute to your AI Platform and Enablement work.",
        ],
    },

    # 2. Mercedes-Benz Tech Innovation GmbH, Ulm (also Karlsruhe, Stuttgart, Berlin)
    # Werkstudent AI Security - Research & Evaluation (d/m/w/x)
    # LinkedIn, posted 1 week ago, Werkstudent, DE track
    # Tasks: Analyse und Bewertung moderner KI Modelle fuer den Einsatz in
    # der Cybersicherheit, Entwicklung automatisierter Evaluierungsmethoden
    # zur Sicherheitsbewertung von KI Systemen und KI Anwendungen, Analyse
    # von Quellcode sowie Identifikation und Bewertung von Sicherheits-
    # luecken in KI basierten Anwendungen, Analyse aktueller KI Technologien
    # fuer offensive und defensive Cybersicherheit, Entwicklung technischer
    # Demonstratoren und Proof of Concepts.
    # Requirements: Studium Informatik, IT Sicherheit, Cyber Security, KI,
    # Data Science, Software Engineering, Wirtschaftsinformatik oder
    # vergleichbar; Python, JavaScript, TypeScript oder Go; Git und GitHub;
    # Grundkenntnisse Webservices, APIs, Auth Konzepte, CI/CD, DevSecOps;
    # nachweislich hervorragende Deutsch und Englischkenntnisse; mind. 15h
    # pro Woche.
    # Apply: https://de.linkedin.com/jobs/view/werkstudent-ai-security-research-evaluation-d-m-w-x-at-mercedes-benz-tech-innovation-4446792270
    # Apply method: company-portal (application flow reaches MBTI's own
    # Workday portal, MBTI_JOBPORTAL, req R0006827)
    {
        "folder": "MBTI Ulm Werkstudent AI Security Research Evaluation",
        "company": "Mercedes-Benz Tech Innovation GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Modell Evaluation und Sicherheitsbewertung | Python + LLM as Judge + SHAP",
        "role_strip": "Werkstudent AI Security, Research und Evaluation",
        "cl_date": "28. August 2026",
        "cl_subject": "Werkstudent AI Security, Research und Evaluation bei Mercedes-Benz Tech Innovation",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in der Entwicklung automatisierter Evaluierungsmethoden fuer KI Systeme sowie in der SHAP gestuetzten Analyse von Sicherheitsluecken und verborgenem Bias in produktiven Machine Learning Modellen. Ich habe eine LLM as Judge Evaluationspipeline gebaut, die KI generierte Antworten auf 5 Dimensionen im JSON Modus bewertet, und in CreditIQ per SHAP Subgruppenanalyse eine verborgene intersektionelle Schwachstelle in einem Kredit Scoring Modell aufgedeckt und korrigiert. Sicher in Python, LangGraph, SHAP und in der Dokumentation technischer Bewertungsergebnisse.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Security, Research und Evaluation bei Mercedes-Benz Tech Innovation. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus der Analyse und Bewertung moderner KI Modelle und der Entwicklung automatisierter Evaluierungsmethoden zur Sicherheitsbewertung von KI Systemen, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich eine LLM as Judge Evaluationspipeline implementiert, die Antworten auf 5 Dimensionen, Groundedness, Relevanz, Vollstaendigkeit, Zitierqualitaet und Sprachqualitaet, im JSON Modus bei Temperatur 0 bewertet, und Self Preference Bias eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft, mit einem harten Fehlschlag bei fehlendem Judge Modell, damit ein stiller Fallback auf Selbstbewertung nicht unbemerkt durchrutscht. Genau diese Disziplin, automatisierte und nachvollziehbare Evaluierungsmethoden fuer KI Systeme zu bauen, deckt sich mit der in der Ausschreibung beschriebenen Kernaufgabe.",
            "In CreditIQ habe ich mit SHAP gestuetzter Subgruppenanalyse eine verborgene intersektionelle Schwachstelle ueber Alter und Geschlecht in einem produktiven Kredit Scoring Modell aufgedeckt und ueber ein vierstufiges Schwellenwert Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen, und den gesamten Regelverstoss in einem Streamlit Tool mit einer Erklaerung in einfacher Sprache fuer den Endbenutzer dokumentiert. Diese Faehigkeit, Quellcode und Modellverhalten systematisch auf Schwachstellen zu untersuchen und die Ergebnisse verstaendlich aufzubereiten, uebertraegt sich direkt auf die in der Ausschreibung beschriebene Identifikation und Bewertung von Sicherheitsluecken in KI basierten Anwendungen.",
            "Ich arbeite sicher in Python, LangGraph, SHAP und mit Git und GitHub im taeglichen Workflow. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Mir ist bewusst, dass die Ausschreibung nachweislich hervorragende Deutschkenntnisse verlangt, die ich noch nicht erreicht habe, und moechte an dieser Stelle offen damit umgehen. Ich kann als Werkstudent mit mindestens 15 Stunden pro Woche einsteigen. Gerne bespreche ich meinen Beitrag zum AI Security Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Siemens Healthineers AG, Kemnath
    # Werkstudent*in (w/m/d) KI-gestuetzte Automatisierung bei Research & Development
    # LinkedIn (full text confirmed via jobs.siemens.com mirror), posted
    # 23 Aug 2026, Werkstudent, DE track, 15 to 20h/week, befristet, hybrid
    # (bis zu 60% mobil innerhalb Deutschlands)
    # Tasks: bestehende Entwicklungsprozesse durch Automatisierung und
    # vorhandene AI Tools effizienter gestalten, den Einsatz von AI Tools
    # wie Microsoft 365 Copilot, GitHub Copilot und Claude Code in
    # konkreten Entwicklungsablaeufen erproben und bewerten, Skripte und
    # Automatisierungen mit Python entwickeln und in Toolchains
    # integrieren, Loesungsansaetze und Best Practices dokumentieren.
    # Requirements: technisches Studium (Informatik, Informationstechnik,
    # Medizintechnik, Data Science, Elektrotechnik oder vergleichbar),
    # mind. 1 Jahr verfuegbar, gute Python Kenntnisse, praktische Erfahrung
    # mit aktuellen AI Tools, Grundverstaendnis generativer AI und LLMs,
    # sehr gute Englischkenntnisse, Deutsch von Vorteil.
    # Apply: https://jobs.siemens.com/en_US/externaljobs/JobDetail/518932
    # Apply method: company-portal (jobs.siemens.com career site)
    {
        "folder": "Siemens Healthineers Kemnath Werkstudent KI Automatisierung Research Development",
        "company": "Siemens Healthineers AG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI gestuetzte Automatisierung und Tool Evaluation | Python + LLM Agenten + Scripting",
        "role_strip": "Werkstudent KI gestuetzte Automatisierung bei Research und Development",
        "cl_date": "28. August 2026",
        "cl_subject": "Werkstudent KI gestuetzte Automatisierung bei Research und Development in Kemnath",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau agentischer KI Systeme sowie in der Automatisierung von Entwicklungsprozessen mit Python Skripten und Toolchain Integration. Ich habe ein Multi Agent RAG System mit LangGraph und lokalen LLMs gebaut und in einem Cloud Data Projekt eine vollautomatisierte Pipeline mit 0 manuellen Eingriffen entwickelt. Sicher in Python, im praktischen Umgang mit KI Tools wie ChatGPT und Claude, und im kritischen Hinterfragen von KI generierten Ergebnissen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI gestuetzte Automatisierung bei Research und Development am Standort Kemnath. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus dem Erproben und Bewerten aktueller AI Tools in konkreten Entwicklungsablaeufen und der Entwicklung von Python Skripten fuer bestehende Toolchains, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit Prompting, Kontextbereitstellung und einem JudgeAgent gebaut, der Antworten kritisch auf 5 Dimensionen bewertet statt Ergebnisse ungeprueft zu uebernehmen, und einen build_pipeline Factory eingefuehrt, der den Import des Orchestrators von externen Credentials entkoppelt. Diese Gewohnheit, KI generierte Ergebnisse kritisch zu hinterfragen und Loesungsansaetze sauber zu dokumentieren, deckt sich direkt mit der in der Ausschreibung beschriebenen Aufgabe, den Einsatz von AI Tools in Entwicklungsablaeufen zu erproben und zu bewerten.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine vollautomatisierte Batch Pipeline auf Cloud Run mit Cloud Scheduler Trigger und 0 manuellen Eingriffen gebaut und den Silver Layer mit Schema Enforcement und sauberer Typkonvertierung gehaertet. Diese Erfahrung, Python Automatisierungen zuverlaessig in eine bestehende Pipeline zu integrieren und die Ergebnisse nachvollziehbar zu dokumentieren, uebertraegt sich direkt auf die in der Ausschreibung beschriebene Entwicklung von Skripten und deren Integration in bestehende Toolchains.",
            "Ich arbeite sicher in Python und nutze ChatGPT und Claude aktiv und kritisch im Alltag, mit einem Grundverstaendnis fuer generative AI, Large Language Models, Prompting und AI Agenten. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, Englisch spreche ich fliessend und sicher. Ich stehe mindestens 1 Jahr mit 15 bis 20 Stunden pro Woche zur Verfuegung und kann in Kemnath oder mobil einsteigen. Gerne bespreche ich meinen Beitrag zum Research und Development Team in einem persoenlichen Gespraech.",
        ],
    },
]
