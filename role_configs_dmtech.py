"""Role configuration for dmTECH GmbH, requested ad hoc on 25 August 2026.

Source: jobteaser.com, fetched in full via Tavily extract on 25 Aug 2026.
https://www.jobteaser.com/en/job-offers/14f28e7e-c73b-4c90-913f-07df0c71c2e7-dmtech-gmbh-werkstudent-it-projektmanagement-pmo-w-m-d

Werkstudent IT-Projektmanagement / PMO (w/m/d), dmTECH GmbH (dm-drogerie
markt's IT subsidiary), Karlsruhe. Published 21 Aug 2026. 6 to 12 months,
part time 15-20h/week, hybrid (fully remote possible per the listing, but
regular on-site presence in Karlsruhe expected). Posting in German -> DE
track (20 July 2026 language match rule).

Tasks: support planning, coordination and documentation of a SAP
transformation project in the Controlling area; track tasks, milestones
and open items; help identify and implement AI supported methods and
tools for efficient project work.

Requirements: technical or business degree (e.g. Wirtschaftsinformatik or
BWL with an information systems focus); first experience in project
management or project support; technical understanding, analytical and
organisational skills; ideally first experience with Jira and Confluence
or similar PM tools; secure German at minimum C1, ideally good English.

Honesty note: Rah has no SAP or Controlling background, and no evidenced
Jira/Confluence experience, so neither is claimed. The genuine, evidenced
overlap is (a) delivering multi month projects with staged milestones
(the eRay GmbH collaboration, the SS Engineers client migration) and
(b) real experience with AI supported tooling for project and process
efficiency (the RAG multi agent orchestration, the Movie Analytics
automated pipeline). Language gap flagged transparently in the closing
paragraph: posting wants C1 German, Rah is B1 in progress.

25 August 2026 rule: SHOW_SS_ENGINEERS_EXPERIENCE turned off for this
render only (in process override, build_html.py default unchanged),
matching Rah's explicit request. eRay GmbH still renders as usual.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_AWS_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_RAG_DE,
    P_MOVIE_DE,
)


CONFIGS_DMTECH = [
    {
        "folder": "dmTECH Karlsruhe Werkstudent IT Projektmanagement PMO",
        "company": "dmTECH GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Projektkoordination und KI gestuetzte Effizienz | Python + LangGraph + SQL",
        "role_strip": "Werkstudent IT Projektmanagement und PMO",
        "cl_date": "25. August 2026",
        "cl_subject": "Werkstudent IT Projektmanagement und PMO am Standort Karlsruhe",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Begleiten mehrmonatiger Projekte mit klaren Meilensteinen sowie im Einsatz KI gestuetzter Methoden fuer effizientere Projektarbeit. Ich habe eine sechsmonatige Kooperation zwischen eRay GmbH und der SRH Heidelberg mit gestaffelten Arbeitspaketen mitgetragen und ein Multi Agent System mit LangGraph orchestriert, das komplexe Arbeitsschritte automatisiert nachvollziehbar macht. Sicher in Python, SQL, strukturierter Dokumentation und in der Nachverfolgung von Aufgaben und offenen Punkten ueber mehrere Projektphasen hinweg.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_MOVIE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_AWS_DE, CERT_SAS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit IT Projektmanagement und PMO bei der dmTECH GmbH am Standort Karlsruhe. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die in der Ausschreibung beschriebene Kombination aus Projektkoordination fuer ein SAP Transformationsprojekt und der Identifizierung KI gestuetzter Methoden und Tools zur effizienten Projektgestaltung, weil ich in den letzten Monaten genau an dieser Schnittstelle gearbeitet habe.",
            "Direkte Erfahrung mit SAP oder im Controlling Umfeld habe ich bisher nicht, das moechte ich offen ansprechen. Beruehrungspunkte mit den in der Ausschreibung genannten Themen bringe ich jedoch ueber zwei Wege mit. Erstens habe ich mehrfach mehrmonatige Projekte mit klaren Meilensteinen von der Planung bis zum Abschluss mitgetragen, zum Beispiel die sechsmonatige Kooperation zwischen eRay GmbH und der SRH Heidelberg zur Prognose der Seewasserqualitaet mit gestaffelten Arbeitspaketen, sowie eine Client Migration bei SS Engineers and Contractors, die ueber vier Monate in schrittweisen Releases ohne Produktionsausfaelle geliefert wurde.",
            "Zweitens bringe ich konkrete Erfahrung mit KI gestuetzten Methoden und Tools fuer effizientere Projektarbeit mit. In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Aufgaben zwischen mehreren spezialisierten Agenten koordiniert und den Fortschritt ueber einen EvalAgent nachvollziehbar dokumentiert. In meinem Movie Analytics und ML Pipeline Projekt habe ich eine 3 stufige Bronze Silver Gold Architektur mit einem vollautomatisierten Cloud Scheduler Trigger gebaut, die ohne manuelle Eingriffe laeuft und den gesamten Ablauf von der Rohdatenaufnahme bis zum fertigen Report nachvollziehbar macht. Genau diese Faehigkeit, komplexe mehrstufige Ablaeufe zu strukturieren, zu automatisieren und den Fortschritt sauber zu dokumentieren, laesst sich direkt auf die Nachverfolgung von Aufgaben, Meilensteinen und offenen Punkten im SAP Transformationsprojekt uebertragen.",
            "Ich arbeite sicher in Python, SQL und in der strukturierten Dokumentation von Projektfortschritt, habe ein technisches und analytisches Studium und Freude an eigenverantwortlichem Arbeiten. Ich halte die AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Ich moechte offen ansprechen, dass die Ausschreibung sichere Deutschkenntnisse auf mindestens C1 Niveau nennt, waehrend mein aktuelles Niveau bei B1 laufend liegt und ich es aktiv weiter hebe. Englisch spreche ich fliessend. Mannheim ist mit dem Zug sehr gut an Karlsruhe angebunden, sodass ein regelmaessiger Vor Ort Tag fuer mich gut machbar waere. Gerne bespreche ich meinen Beitrag zum PMO Team in einem persoenlichen Gespraech.",
        ],
    },
]
