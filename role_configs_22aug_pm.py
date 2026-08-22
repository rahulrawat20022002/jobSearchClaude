"""Role configurations for the 22 August 2026 afternoon supplemental run.

Rah asked Cowork to continue the search after the morning top 3 cut,
focusing specifically on AI Engineer roles, to fill out the remaining
room in the 28 July 2026 yield reset's normal top 3 to 5 band (morning
run drafted 3; this run adds 2 more to reach 5).

Freshness order:
  1. logen.ai, Berlin, Werkstudent AI Agent Developer, posted 2 days
     before draft per Arbeitnow listing, Werkstudent, DE track.
  2. Schaeffler, Herzogenaurach, Werkstudent KI-Agenten-Entwicklung im
     Projektmanagement, live open requisition on jobs.schaeffler.com,
     12 month term starting immediately, Werkstudent, DE track.

Platform mix: Company Page 1 (Schaeffler, jobs.schaeffler.com), Other 1
(logen.ai, sourced via the Arbeitnow aggregator; the posting hosts its
own application form on Arbeitnow rather than redirecting to a company
career page, so the platform is ambiguous and Apply Method is set to
company-portal per the CLAUDE.md default-to-out-of-scope rule when a
listing's platform nature is unclear).

Readability note: a third AI Engineer candidate, Infineon Technologies
Internship AI Engineering and MLOps (Muenchen, LinkedIn, posted 1 day
before draft), was checked and dropped. Its LinkedIn listing rendered
completely blank behind a login wall with no recoverable Aufgaben or
Profil text from any angle tried. Per CLAUDE.md invariant 3, never
fabricate, it was not tailored. Not added to the watchlist table since
it duplicates the already-logged ADAC blocked-readability pattern from
the morning run; noted here for the record instead.

Language track per 20 July 2026 rule: both posting bodies are written in
German, both ship on the DE track.

Dedup check against applied-log.csv and Notion: Schaeffler and logen.ai
are both new companies never previously contacted in this pipeline.

Both are Werkstudent roles, in scope under master-projects.md work
types. Neither is dual-study, apprenticeship, Quereinsteiger, or a
voluntary internship.

19 August 2026 CV content rules apply throughout: no hyphens or dashes
in CV text (the sole allowed exception is the scikit-learn package
name, matching prior runs), no parentheses/brackets in bullets,
Languages EN+DE only, German level locked to 'Deutsch: B1, laufend',
no page numbers/headers/footers, 2 page hard cap, Ojas style header,
Skills grouped into functional buckets, positioning tag under the name
is a pitch not the posting title.

Skill honesty note: the Schaeffler posting mentions Python and
TypeScript. master-projects.md documents React/JavaScript experience
at SS Engineers and Contractors but not TypeScript specifically, so
TypeScript is not claimed anywhere in this CV or cover letter, only
Python, LangGraph, and the React/JavaScript background actually on
record.
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
    P_MOVIE_DE,
)


CONFIGS_22AUG_PM = [
    # 1. logen.ai, Berlin
    # Werkstudent AI Agent Developer
    # Sourced via Arbeitnow aggregator, posted 2 days before draft.
    # KI Startup aus Berlin, Automatisierung im Kundenservice, baut AI
    # Agents, Voicebots und Automatisierungsloesungen fuer den
    # deutschen Mittelstand. Eigenes SaaS Produkt AIdapt.
    # Role is hands on: Code schreiben, APIs debuggen, Conversation
    # Flows implementieren, Systeme integrieren.
    # Apply: https://www.arbeitnow.com/jobs/companies/logenai/werkstudentin-ai-agent-developer-berlin-314047
    {
        "folder": "logen.ai Berlin Werkstudent AI Agent Developer",
        "company": "logen.ai",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Produktionsreife AI Agenten | Python + LangGraph + APIs",
        "role_strip": "Werkstudent AI Agent Developer",
        "cl_date": "22. August 2026",
        "cl_subject": "Werkstudent AI Agent Developer am Standort Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau produktionsreifer KI Agenten statt reiner Proof of Concepts. Ich habe ein Multi Agent RAG System mit LangGraph orchestriert, das ueber mehrere spezialisierte Agenten Anfragen end to end beantwortet, APIs integriert und die Ergebnisse messbar auswertet statt nur zu demonstrieren. Sicher in Python, LangGraph, API Integration und im eigenstaendigen Debuggen laufender Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit AI Agent Developer am Standort Berlin bei logen.ai. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich genau die in der Ausschreibung beschriebene Haltung, keine Proof of Concepts fuer die Schublade zu bauen, sondern Code zu schreiben, APIs zu debuggen, Conversation Flows zu implementieren und Systeme zu integrieren, mit direktem Impact bei echten Kundenprojekten, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen Policy Korpus in Englisch oder Deutsch end to end beantwortet. Ein LanguageAgent zentralisiert die Sprachsteuerung fuer jede nachgelagerte Komponente, ein JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 auf einem separaten Modell zur Vermeidung von Self Preference Bias, und ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports. Genau dieses Muster, mehrere spezialisierte Agenten sauber zu orchestrieren und ihre Ergebnisse messbar statt anekdotisch zu bewerten, deckt sich direkt mit dem Bau von AI Agenten, die tatsaechlich in Produktion gehen.",
            "In meinem Movie Analytics und ML Pipeline Projekt habe ich eine end to end Batch Pipeline gebaut, die ueber eine oeffentliche API Daten in einen GCS Data Lake zieht und durch eine 3 stufige Bronze Silver Gold Medaillon Architektur auf BigQuery und Cloud Run verarbeitet, vollstaendig automatisiert auf einem Cloud Scheduler Trigger ohne manuelle Eingriffe. Die Silver Schicht haerte ich mit Schema Enforcement, sicherer Typkonvertierung und Deduplizierung ueber Window Functions, damit das System nicht nur einmal, sondern zuverlaessig jeden Tag laeuft. Genau diese Zuverlaessigkeit im produktiven Betrieb, nicht nur in der Demo, ist das, was ein AI Agent im Kundenservice braucht.",
            "Ich arbeite sicher in Python, LangGraph und API Integration sowie im eigenstaendigen Debuggen laufender Systeme und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Team vollstaendig auf Deutsch moeglich bleibt. Ich kann als Werkstudent in Berlin einsteigen und sende gerne meinen Lebenslauf sowie dieses Anschreiben als fachlich begruendetes Statement, warum mich diese Rolle interessiert. Gerne bespreche ich meinen Beitrag zu AIdapt in einem persoenlichen Gespraech.",
        ],
    },

    # 2. Schaeffler, Herzogenaurach
    # Werkstudent KI-Agenten-Entwicklung im Projektmanagement (d/m/w)
    # Company career page jobs.schaeffler.com. 12 month term, ab sofort,
    # Teilzeit. Project: Drive to Performance. Stack: Python, TypeScript,
    # Prompt Engineering, technische Dokumentation, KI/LLM Anwendungen,
    # Tests und Analysen, Video Demonstrationen. Requires proof of active
    # enrollment (Immatrikulation) throughout the role.
    # Apply: https://jobs.schaeffler.com/job/Herzogenaurach-Werkstudent-KI-Agenten-Entwicklung-im-Projektmanagement-(dmw)-91074/1423788133
    {
        "folder": "Schaeffler Herzogenaurach Werkstudent KI Agenten Entwicklung Projektmanagement",
        "company": "Schaeffler Technologies AG und Co. KG",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Agenten Entwicklung und Prompt Engineering | Python + LangGraph",
        "role_strip": "Werkstudent KI Agenten Entwicklung im Projektmanagement",
        "cl_date": "22. August 2026",
        "cl_subject": "Werkstudent KI Agenten Entwicklung im Projektmanagement am Standort Herzogenaurach",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung in der Entwicklung von KI Agenten, Prompt Engineering und der messbaren Evaluation von LLM Anwendungen. Ich habe ein Multi Agent RAG System mit LangGraph gebaut, dessen JudgeAgent Antworten strukturiert im JSON Modus bewertet, und dokumentiere Systemaufbau, Datenmodelle und Testergebnisse konsequent nachvollziehbar. Sicher in Python, Prompt Engineering, KI und LLM Anwendungen sowie im Testen und Analysieren produktionsnaher Systeme.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit KI Agenten Entwicklung im Projektmanagement am Standort Herzogenaurach bei der Schaeffler Technologies AG und Co. KG. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die im Projekt Drive to Performance beschriebene Arbeit an KI Agenten, das Erstellen von Prompts sowie technischer Dokumentation und das Sammeln praktischer Erfahrung in KI und LLM Anwendungen, Tests und Analysen, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen Policy Korpus end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0 auf einem separaten Modell zur Vermeidung von Self Preference Bias, und ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in strukturierten JSON und Markdown Reports. Ich habe Systemaufbau, Datenmodelle und eingesetzte Methoden durchgehend dokumentiert, damit die Ergebnisse fuer ein Projektteam nachvollziehbar und pruefbar bleiben. Genau dieses Muster, Prompts zu bauen, Ergebnisse strukturiert zu testen und die Loesung dokumentiert weiterzugeben, deckt sich direkt mit der Arbeit an KI Agenten im Projekt Drive to Performance.",
            "In CreditIQ habe ich unter regulatorischen Anforderungen ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt, abgesichert durch eine Unit Test Suite mit 100 Prozent Branch Coverage und einen vollstaendigen regulatorischen Bericht. Bei eRay GmbH habe ich zusaetzlich sechs Kandidatenmodelle systematisch benchmarkt, bevor ich mich fuer CatBoost MultiQuantile entschied. Diese Gewohnheit, jede Loesung mit Tests abzusichern und den Weg dorthin nachvollziehbar zu dokumentieren, ist genau das, was die Analyse und Verbesserung von KI Loesungen mittels Video Demonstrationen im Projektteam braucht.",
            "Ich arbeite sicher in Python, Prompt Engineering sowie in KI und LLM Anwendungen, im Testen und Analysieren produktionsnaher Systeme und nutze aktiv ChatGPT und Claude als Werkzeuge im Alltag. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend, und ich hebe es aktiv weiter, damit die Zusammenarbeit im Projektteam vollstaendig auf Deutsch moeglich bleibt. Ich bin an der SRH Heidelberg immatrikuliert und kann den Nachweis waehrend der gesamten Taetigkeit erbringen sowie ab sofort fuer die 12 monatige Laufzeit in Herzogenaurach einsteigen. Gerne bespreche ich meinen Beitrag zum Projekt Drive to Performance in einem persoenlichen Gespraech.",
        ],
    },
]
