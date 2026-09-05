"""Role configurations for the 5 September 2026 scheduled job search run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 1 row in status
'drafted' at run start (Beilmann Marketing GmbH, Werkstudent KI
Automatisierung und interne Tools, an ad hoc draft Rah requested directly
via a pasted Xing URL on a prior run while the backlog was at the 11 Aug
hard pause zone). 1 drafted falls under the 8 row floor of the 28 July
2026 yield based reset rule, which allows a normal top 3 to 5 cut.

Reconciliation this run found the repo missing the actual deliverables for
the Beilmann Marketing row even though Notion already shows it as
'drafted' -- no drafts/ folder existed for it in git, the source of truth
for content per the shared invariants. That row is rendered in full below
so git catches up with what Notion already claims, rather than leaving a
false 'drafted' flag standing with nothing behind it. Separately,
reconciliation found the CSV 27 rows behind Notion's Status column across
a long tail of postings that had gone stale, been rejected, or been
applied to since their last CSV sync; the CSV was corrected to match
Notion (the source of truth for status) for all 27, with no reverse writes.

Platform mix this run:
  - Xing (Beilmann Marketing GmbH, ad hoc backfill), 1
  - StepStone (Mercedes-Benz Tech Innovation), 1
  - Other / company direct email via Bundesagentur fuer Arbeit job board
    (ETG-Elektronik GmbH), 1

Freshness order per 12 July 2026 priority rule within the single Germany
tier:
  1. Mercedes-Benz Tech Innovation, Werkstudent AI Agents and Robotics
     Platform, Ulm/Stuttgart/Karlsruhe, posted 14 hours ago, Werkstudent,
     DE track.
  2. Beilmann Marketing GmbH, Werkstudent KI Automatisierung und interne
     Tools, Berlin, originally drafted ad hoc on an earlier date, DE
     track (backfilling deliverables only, not a freshly found posting).
  3. ETG-Elektronik GmbH, Praktikant/Werkstudent AI Systems and
     Generative AI, Weiterstadt, posted 16 days ago, Praktikum or
     Werkstudent, DE track.

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language): all three postings this run have
German language bodies, so all three ship DE track.

Language level transparency: Mercedes-Benz Tech Innovation asks for "gute
Deutsch- oder Englischkenntnisse" (good German OR English), a bar Rah's
current B1 in progress plus fluent English comfortably clears. ETG-
Elektronik asks for "gute Sprachkenntnisse in Deutsch und Englisch" (good
German AND English), a modest step above B1 in progress; shipped per the
standing rule that language level does not filter listings, cover letter
stays upfront about the current level. Beilmann Marketing's original Xing
posting asked for "sehr gute Deutschkenntnisse", above B1 in progress,
already flagged in that row's Notion Notes from the original ad hoc draft.

Apply method transparency: Beilmann Marketing's Apply Link is a Xing
Easy Apply / Schnelle Bewerbung listing, platform-native, in OpenClaw's
automated scope. Mercedes-Benz Tech Innovation's StepStone listing routes
through the company's own careers flow on jobs.mercedes-benz.com,
consistent with prior MBTI listings, so it is recorded as company-portal
with the StepStone URL kept as the confirmed working Apply Link.
ETG-Elektronik GmbH does not have a web application form at all -- the
posting asks candidates to email a CV, cover letter, and a note on past
AI projects directly to personal@etg-gmbh.de. This is recorded as
company-portal since it is entirely outside OpenClaw's platform-native
automated submission scope; Rah sends the email manually.

Dedup check against applied-log.csv and Notion: Beilmann Marketing GmbH
is an entirely new company, not previously logged (its Notion row already
exists in status drafted from the earlier ad hoc request; this run only
adds the matching CSV row and the actual deliverables). Mercedes-Benz
Tech Innovation GmbH already has three prior entries (Werkstudent Data
Engineering and Data Science, rejected; Werkstudent Agentic AI und
Multi-Agent-Systeme, Not listed Anymore; Werkstudent AI Security Research
und Evaluation) but not this AI Agents and Robotics Platform role,
allowed under the different roles at the same company rule. A related
Working Student: AI Engineer, Agentic Systems (m/f/d) role at Retorio
GmbH in Munich was found on StepStone this run but is word for word the
same title as an existing Notion/CSV row already logged as 'Not listed
Anymore'; it was dropped rather than redrafted since it reads as the same
opportunity resurfacing, not a materially different role, and is flagged
in the digest watchlist for Rah to decide manually. ETG-Elektronik GmbH
is an entirely new company, never previously logged.

19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
no parentheses or brackets in bullets, Languages EN and DE only, German
level locked to "Deutsch: B1, laufend" on the DE track used by all three
roles this run, no page numbers or headers or footers, 2 page hard cap,
Ojas style header, Skills grouped into functional buckets, positioning
tag under the name is a pitch not the posting title, and banned strings
on the validation gate are met by the new header.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_AWS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_CREDITIQ_DE,
    P_MOVIE_DE,
    P_FLIGHT_DE,
)


CONFIGS_05SEP = [
    # 1. Mercedes-Benz Tech Innovation, Ulm / Stuttgart / Karlsruhe
    # Werkstudent AI Agents & Robotics Platform (d/m/w/x)
    # StepStone, posted 14 hours ago, Werkstudent, DE track
    # Tasks: multimodal agent systems that understand language, perceive
    # their environment and act autonomously; computer vision and
    # perception components; integrating foundation models, vision
    # language models and agent frameworks into robotics; running and
    # evaluating experiments on real robots and in simulation.
    # Requirements: advanced Bachelor's or Master's in CS, AI, data
    # science, robotics or related; interest in multimodal AI systems,
    # AI agents and physical AI; good German OR English skills; nice to
    # have ML/RL/imitation learning, foundation models/LLMs/VLMs, AI
    # agents/planning systems, computer vision, robotics, Linux.
    # Apply: https://www.stepstone.de/stellenangebote--Werkstudent-AI-Agents-Robotics-Platform-d-m-w-x-Ulm-Stuttgart-Karlsruhe-Mercedes-Benz-Tech-Innovation--14399512-inline.html
    # Apply method: company-portal (routes to Mercedes-Benz's own careers flow)
    {
        "folder": "MBTI Ulm Stuttgart Karlsruhe Werkstudent AI Agents Robotics Platform",
        "company": "Mercedes-Benz Tech Innovation",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Agentische KI und Multi Agent Systeme | Python + LangGraph + LLM as Judge",
        "role_strip": "Werkstudent AI Agents und Robotics Platform",
        "cl_date": "5. September 2026",
        "cl_subject": "Werkstudent AI Agents und Robotics Platform in Ulm, Stuttgart und Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau multimodaler Agentensysteme, die Sprache verstehen und autonom Entscheidungen treffen. Ich habe ein Multi Agent RAG System mit LangGraph orchestriert, das Sprachverstehen, Retrieval und eine unabhaengige LLM as Judge Bewertung end to end verbindet, und in CreditIQ per SHAP gestuetzter Analyse verborgene Muster in einem produktiven Machine Learning System aufgedeckt und korrigiert. Sicher in Python, LangGraph, Agentenarchitekturen und der Evaluation von KI Systemen auf mehreren Dimensionen.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Agents und Robotics Platform bei Mercedes-Benz Tech Innovation an den Standorten Ulm, Stuttgart und Karlsruhe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Verbindung aus Foundation Models, Agentic AI, Computer Vision und Robotik zu intelligenten Physical AI Systemen, weil ich in den letzten Monaten genau an dieser Schnittstelle von Sprache, Wahrnehmung und autonomer Entscheidung gearbeitet habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, in dem ein LanguageAgent zentral die Ausgabesprache fuer jeden nachgelagerten Agenten festlegt und ein JudgeAgent Antworten auf 5 Dimensionen im JSON Modus bewertet, wobei der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft, um Self Preference Bias auszuschliessen, mit einem harten Fehlschlag bei fehlendem Judge Modell, damit ein stiller Fallback nicht unbemerkt durchrutscht. Genau diese Disziplin, mehrere Agenten koordiniert zusammenarbeiten zu lassen und ihre Entscheidungen systematisch zu evaluieren, uebertraegt sich direkt auf den Aufbau multimodaler Agentensysteme fuer reale Robotikplattformen.",
            "In CreditIQ habe ich mit SHAP gestuetzter Subgruppenanalyse eine verborgene intersektionelle Schwachstelle ueber Alter und Geschlecht in einem produktiven Kredit Scoring Modell aufgedeckt und ueber ein vierstufiges Schwellenwert Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen, und dabei gelernt, komplexe Modellentscheidungen systematisch zu hinterfragen statt sie unbesehen zu uebernehmen. Diese Faehigkeit, ein System aus mehreren beweglichen Teilen zu analysieren, Schwachstellen zu identifizieren und die Ergebnisse nachvollziehbar zu dokumentieren, passt gut zur in der Ausschreibung beschriebenen Durchfuehrung, Evaluation und Dokumentation von Experimenten auf realen Robotern und in Simulationsumgebungen.",
            "Ich arbeite sicher in Python und LangGraph und beschaeftige mich aktiv mit aktuellen Forschungstrends rund um Agentic AI und multimodale Systeme. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend, was die in der Ausschreibung genannte Anforderung guter Deutsch oder Englischkenntnisse abdeckt. Ich kann als Werkstudent flexibel an einem der drei Standorte einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Physical AI Team in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Beilmann Marketing GmbH, Berlin
    # Werkstudent KI Automatisierung und interne Tools
    # Xing, ad hoc draft requested directly by Rah (Notion row already
    # exists in status 'drafted' from that earlier request); this run
    # backfills the actual deliverables, DE track
    # Apply: https://www.xing.com/jobs/berlin-werkstudent-ki-automatisierung-interne-tools-157624793
    # Apply method: platform-native (Xing Easy Apply / Schnelle Bewerbung)
    {
        "folder": "Beilmann Marketing Berlin Werkstudent KI Automatisierung interne Tools",
        "company": "Beilmann Marketing GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Automatisierung und interne Tools | Python + LangGraph + Cloud Pipelines",
        "role_strip": "Werkstudent, KI Automatisierung und interne Tools",
        "cl_date": "5. September 2026",
        "cl_subject": "Werkstudent KI Automatisierung und interne Tools in Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau automatisierter KI Workflows und interner Tools ueber Python, LangGraph und vollautomatisierte Cloud Pipelines. Ich habe ein Multi Agent RAG System mit LLM as Judge Evaluation gebaut und in einem Cloud Data Projekt eine Batch Pipeline mit 0 manuellen Eingriffen automatisiert. Sicher in Python, SQL, Automatisierungs Frameworks und der praktischen Integration von KI Modellen in bestehende Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI Automatisierung und interne Tools bei Beilmann Marketing GmbH in Berlin. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim interessiert mich die Aufgabe, KI gestuetzte Automatisierung fuer interne Tools praktisch nutzbar zu machen, weil ich in den letzten Monaten genau solche Systeme von der Idee bis zum lauffaehigen Werkzeug gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Nutzerfragen ueber eine hybride BM25 plus Dense Retrieval Pipeline beantwortet und dessen JudgeAgent Antworten automatisiert auf 5 Dimensionen bewertet, statt Qualitaet manuell zu pruefen. Diese Erfahrung, wiederkehrende Arbeit systematisch zu automatisieren und die Ergebnisse nachvollziehbar zu machen, laesst sich direkt auf interne Tools und Automatisierungs Use Cases uebertragen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine Batch Pipeline gebaut, die vollstaendig automatisiert ueber einen Cloud Scheduler Trigger mit 0 manuellen Eingriffen laeuft, von der Rohdatenerfassung ueber ein 3 stufiges Bronze Silver Gold Modell bis zum fertigen Dashboard. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline orchestriert, die Datenluecken automatisch rekonstruiert und Gate Checks vor jeder Ausgabe durchlaeuft, statt sich auf manuelle Kontrolle zu verlassen.",
            "Ich arbeite sicher in Python, SQL und gaengigen Automatisierungswerkzeugen und habe Freude daran, wiederkehrende manuelle Arbeit in verlaessliche automatisierte Ablaeufe zu ueberfuehren. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend. Mir ist bewusst, dass die Ausschreibung sehr gute Deutschkenntnisse nennt, die ich noch nicht erreicht habe, und moechte an dieser Stelle offen damit umgehen. Ich kann als Werkstudent in Berlin flexibel einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Team in einem persoenlichen Gespraech.",
        ],
    },

    # 3. ETG-Elektronik GmbH, Weiterstadt
    # Praktikant/Werkstudent (m/w/d) AI Systems & Generative AI
    # Found via Bundesagentur fuer Arbeit job board, posted 16 days ago,
    # Praktikum or Werkstudent, DE track, EUR 15/hour, part time
    # Tasks: RAG systems and vector databases, local open source LLM
    # workflows (Llama, Ollama, AnythingLLM, Open WebUI), prompt
    # engineering and evaluation of multi step pipelines, connecting AI
    # models to internal systems via APIs and workflow tools such as
    # n8n, LangChain, LangGraph, and technology scouting on agentic AI
    # and multimodality.
    # Requirements: ongoing studies in CS, information systems, data
    # science, cognitive science or related; strong interest in LLMs,
    # generative AI and modern AI architectures; first experience with
    # Python, REST/JSON APIs, AI frameworks or open source LLM
    # frontends; good German and English.
    # Apply: no web form; send CV, cover letter and a note on past AI
    # projects directly to personal@etg-gmbh.de
    # Apply method: company-portal (direct email application, no web
    # form at all, fully out of OpenClaw's platform-native scope)
    {
        "folder": "ETG-Elektronik Weiterstadt Praktikant Werkstudent AI Systems Generative AI",
        "company": "ETG-Elektronik GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | RAG Systeme und Generative AI Automatisierung | Python + LangGraph + Open Source LLMs",
        "role_strip": "Praktikant oder Werkstudent, AI Systems und Generative AI",
        "cl_date": "5. September 2026",
        "cl_subject": "Praktikant oder Werkstudent AI Systems und Generative AI in Weiterstadt",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von RAG Systemen, lokalen Open Source LLM Workflows und Prompt Engineering Pipelines. Ich habe ein Multi Agent RAG System vollstaendig auf selbst gehosteter Ollama Inferenz mit Mistral 7B und Qwen2.5 14B betrieben und eine hybride BM25 plus Dense Retrieval Pipeline ueber eine mehrsprachige Vektor Datenbank gebaut. Sicher in Python, REST APIs, LangGraph und der praktischen Evaluation von KI generierten Antworten.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Stelle als Praktikant oder Werkstudent AI Systems und Generative AI bei ETG-Elektronik GmbH in Weiterstadt. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim passt die in der Ausschreibung beschriebene Arbeit an RAG Systemen, lokalen Open Source LLM Workflows und Prompt Engineering Pipelines sehr genau zu dem, was ich in den letzten Monaten praktisch gebaut habe. Anbei sende ich meinen Lebenslauf, dieses Anschreiben sowie eine kurze Uebersicht zu meinen bisherigen KI Projekten.",
            "In meinem Multi Agent RAG Projekt habe ich die komplette Generierungs, Bewertungs und Evaluationskette auf selbst gehosteter Ollama Inferenz aufgebaut, mit Mistral 7B als Generator und Qwen2.5 14B als unabhaengigem LLM as Judge auf einem separaten Modell, um Self Preference Bias auszuschliessen. Die Migration auf eine gemeinsame mehrsprachige Vektor Datenbank mit paraphrase multilingual MiniLM L12 v2 erlaubt es, eine deutsche Anfrage gegen englische Quellen zu stellen und die Antwort vollstaendig auf Deutsch zu liefern, ohne den Dokumentenbestand zu duplizieren. Genau diese Kombination aus RAG Architektur, Vektor Datenbanken und Chunking Strategien deckt sich mit der in der Ausschreibung beschriebenen Aufgabe im Bereich RAG und Wissensmanagement.",
            "Ich habe ausserdem einen JudgeAgent implementiert, der Antworten automatisiert im JSON Modus bei Temperatur 0 auf 5 Dimensionen bewertet, mit einem harten Fehlschlag bei fehlendem Judge Modell, damit ein stiller Fallback auf Selbstbewertung nicht unbemerkt durchrutscht, und den Evaluator anschliessend vollstaendig von der HuggingFace API auf Ollama portiert, so dass Generierung, Bewertung und Evaluation lokal laufen. Diese Erfahrung mit Prompt Engineering, Evaluation von KI Antworten und dem Betrieb lokaler Open Source Modelle passt direkt zu den in der Ausschreibung genannten Aufgaben Prompt Engineering und Evaluation sowie Lokale KI und Open Source.",
            "Ich arbeite sicher in Python und mit REST und JSON Schnittstellen und habe ein ausgepraegtes Interesse an aktuellen Entwicklungen rund um Agentic AI und Multimodalitaet. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend, ich hebe es aktiv weiter, und Englisch spreche ich fliessend, was die geforderten guten Sprachkenntnisse in Deutsch und Englisch weitgehend abdeckt. Ich kann ab sofort in Teilzeit in Weiterstadt einsteigen. Gerne bespreche ich meinen Beitrag zu Ihren KI Projekten in einem persoenlichen Gespraech.",
        ],
    },
]
