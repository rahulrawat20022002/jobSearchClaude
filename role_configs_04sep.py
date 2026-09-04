"""Ad hoc single role draft, 4 September 2026.

Rah pasted a specific Xing listing URL directly in chat and asked for the
CV and cover letter for it. Sourced via Tavily extract (WebFetch could not
reach xing.com directly), not via the scheduled search step.

1. Beilmann Marketing GmbH, Berlin (remote noted)
   Werkstudent:in KI-Automatisierung & interne Tools (m/w/d)
   Posted "yesterday" per the Xing listing (fetched 4 Sep 2026), Werkstudent,
   DE track (posting body is German; the English "About this job" heading is
   Xing's own UI chrome, not posting content).
   Apply: https://www.xing.com/jobs/berlin-werkstudent-ki-automatisierung-interne-tools-157624793
   Apply method: platform-native, XING Easy Apply (listing shows "Easy apply"
   staying inside xing.com) -> in scope for OpenClaw.

   Tasks: builds and owns automations and KI-Workflows for the internal
   team, extends bausteine inside Milow (the company's own AI agent),
   optimises slow/error-prone existing workflows, is the point of contact
   for colleagues who need an automation, documents how workflows are
   built.
   Requirements: studying Wirtschaftsinformatik, Informatik, Data Science,
   Kuenstliche Intelligenz or comparable; coding experience in Python or
   JavaScript; curiosity and initiative; reliability and precision; very
   good German and English, written and spoken. Nice to have (not
   required): first experience with the Claude or OpenAI API, or serious
   engagement with prompting.
   Salary shown on listing: EUR15 (employer salary) -- matches the standing
   15 EUR/hour salary-field figure exactly; noted as a coincidence, not
   used as a scoring factor per the standing pay-is-not-a-filter rule.

   Language level transparency: posting asks for "sehr gute Deutsch- und
   Englischkenntnisse" (very good German), above Rah's current B1 in
   progress level. Shipped anyway per the standing rule that language
   level does not filter listings; the cover letter is upfront about the
   current B1 level, consistent with how Reply and Kaufland were handled
   on 26 August 2026.

   Dedup check: no existing "Beilmann" row in applied-log.csv or Notion.
   New company, new role, not a duplicate.

   Backlog note: Notion drafted count was 11 (hard-pause zone) going into
   this ad hoc request. This is a specific, user-named listing requested
   directly by Rah in chat, not autonomous sourcing under the scheduled
   search step, so the 28 July 2026 backlog gate (which throttles Cowork's
   own search/draft loop) was not applied to block it; flagged to Rah in
   chat that this pushes the drafted count to 12.

   19 August 2026 CV content rules apply: no hyphens or dashes in CV text,
   no parentheses/brackets in bullets, Languages EN+DE only (no Hindi),
   German level locked to 'Deutsch: B1, laufend' on DE track, no page
   numbers/headers/footers, 2 page hard cap, Ojas style header, Skills
   grouped into functional buckets, positioning tag under the name is a
   pitch not the posting title.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_FLIGHT_DE,
)


CONFIGS_04SEP = [
    # 1. Beilmann Marketing GmbH, Berlin
    # Werkstudent:in KI-Automatisierung & interne Tools (m/w/d)
    # XING, posted 3 Sep 2026 (shown "yesterday"), Werkstudent, DE track
    {
        "folder": "Beilmann Marketing Berlin Werkstudent KI Automatisierung interne Tools",
        "company": "Beilmann Marketing GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | KI Automatisierung und Agentic Workflows | Python + LangGraph",
        "role_strip": "Werkstudent KI Automatisierung und interne Tools",
        "cl_date": "4. September 2026",
        "cl_subject": "Werkstudent:in KI Automatisierung und interne Tools am Standort Berlin",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Bau von Automatisierungen, agentenbasierten KI Workflows und Orchestrierungs Pipelines in Python. Ich habe bei eRay GmbH eine end to end Automatisierungspipeline fuer Zeitreihen Prognosen geliefert und ein Multi Agent RAG System mit generativen LLMs orchestriert und dokumentiert. Sicher in Python, JavaScript nah durch React Erfahrung, und im sauberen Dokumentieren und Uebergeben von Workflows an ein Team.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_FLIGHT_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich als Werkstudent:in KI Automatisierung und interne Tools am Standort Berlin. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung genannte Kombination aus dem Bau eigener Automatisierungen, der Weiterentwicklung von Bausteinen in einem internen KI Agenten und der sauberen Dokumentation von Workflows, weil ich in den letzten Monaten genau an dieser Schnittstelle gearbeitet habe.",
            "Bei eRay GmbH habe ich waehrend einer 6 monatigen Kollaboration mit der SRH Heidelberg eine end to end automatisierte Zeitreihen Pipeline fuer vier Wasserqualitaets Indikatoren geliefert, inklusive Orchestrator mit Gate Checks und Plausibilitaetsgrenzen, die ohne manuelles Eingreifen durchlief. Genau diese Faehigkeit, fehleranfaellige manuelle Schritte in robuste, dokumentierte Automatisierungen zu ueberfuehren, deckt sich mit der in der Ausschreibung beschriebenen Workflow Optimierung.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem mit generativen LLMs Mistral 7B und Qwen2.5 14B gebaut, das eigene Bausteine wie einen LanguageAgent und einen JudgeAgent miteinander verkettet und deren Zusammenspiel dokumentiert. Diese praktische Erfahrung im Bau und in der Erweiterung eigener KI Agenten Bausteine deckt sich direkt mit der Arbeit an Milow, dem hauseigenen KI Agenten.",
            "Ich arbeite sicher in Python und habe durch meine Erfahrung mit React auch JavaScript Grundlagen im produktiven Einsatz. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutsch liegt bei B1 laufend und ich hebe es aktiv weiter, Englisch spreche ich fliessend. Gerne bespreche ich meinen Beitrag zu euren Automatisierungen und KI Workflows in einem persoenlichen Gespraech.",
        ],
    },
]
