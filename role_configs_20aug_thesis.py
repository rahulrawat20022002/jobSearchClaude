"""Amprion Masterarbeit initiative application, 20 August 2026 supplemental.

Rah opened the Amprion online form and picked "Ich bin auf der Suche nach:
Einer Abschlussarbeit" and asked for a thesis-tailored CV/CL. Amprion's
careers page confirms Bachelor/Masterarbeit slots are possible but no
dedicated AI Masterarbeit was live on jobs.amprion.net at the time of
this run, so this is an Initiativbewerbung Masterarbeit targeting the
same team (Unternehmensweite IT-Loesungen, Wissens- und
Dokumentenmanagement) as the Werkstudent KI Stellen-ID 7959 posting.

Proposed research question:
  Multi Agent Retrieval Augmented Generation Systeme mit LLM as Judge
  Evaluation fuer Wissens und Dokumentenmanagement in einem
  Uebertragungsnetzbetreiber. Sechsmonatiges Zeitfenster Oktober 2026
  bis Maerz 2027, passend zum Studienende 31.03.2027.

Language track: DE (Amprion careers page and prior posting body in
German). All 19 August 2026 CV content rules apply.
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
)


CONFIGS_20AUG_THESIS = [
    {
        "folder": "Amprion Dortmund Masterarbeit KI Wissensmanagement",
        "company": "Amprion GmbH",
        "lang": "de",
        "tag": "Masterstudent Data Science and Analytics | Masterarbeit RAG und Wissensmanagement | Python + LangGraph + LLM as Judge",
        "role_strip": "Masterarbeit KI und Wissensmanagement",
        "cl_date": "20. August 2026",
        "cl_subject": "Initiativbewerbung Masterarbeit, KI und Wissensmanagement im Team Unternehmensweite IT-Loesungen",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim, voraussichtlicher Studienabschluss 31.03.2027, mit publikationsnaher Forschungserfahrung an der Schnittstelle von Large Language Models, ehrlicher AI Evaluation und regulierten Datenumgebungen. Meine Bachelorarbeit habe ich in einem IEEE Style Paper mit ehrlicher Limitations Sektion abgeschlossen und der Betreuer akzeptierte sie als in der Substanz veroeffentlichungsreif. Aufbauend darauf habe ich ein Multi Agent RAG System mit LLM as Judge Evaluation lokal auf Ollama mit Mistral 7B und Qwen2.5 14B mit voller EN und DE Unterstuetzung gebaut und in CreditIQ ein Kredit Scoring System unter EU AI Act Bedingungen entwickelt. Fuer eine sechsmonatige Masterarbeit in Ihrem Team bringe ich damit einen belastbaren methodischen und praktischen Werkzeugkasten mit.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich initiativ um eine Masterarbeit im Bereich Kuenstliche Intelligenz und Wissensmanagement im Team Unternehmensweite IT-Loesungen am Standort Dortmund, mit einem sechsmonatigen Zeitfenster von Oktober 2026 bis Maerz 2027, passend zu meinem voraussichtlichen Studienende am 31.03.2027. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim reizt mich die Kombination aus Wissens und Dokumentenmanagement, digitalem Arbeitsplatz und Amprions Rolle in der Energiewende.",
            "Als Themenvorschlag skizziere ich Multi Agent Retrieval Augmented Generation Systeme mit LLM as Judge Evaluation fuer Wissens und Dokumentenmanagement in einem Uebertragungsnetzbetreiber. In meinem eigenen Multi Agent RAG Projekt habe ich bereits ein LangGraph orchestriertes Agentensystem gebaut, das Fragen ueber einen 14 Dokumente Policy Korpus in EN und DE end to end beantwortet. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Dieses methodische Geruest laesst sich direkt auf ein Amprion internes Dokumentenkorpus uebertragen und liefert eine belastbare wissenschaftliche Evaluation und einen praktisch nutzbaren Prototyp.",
            "Ich habe bereits eine Abschlussarbeit im Machine Learning Bereich veroeffentlichungsreif abgeschlossen. In meiner Bachelorarbeit zur Diabetesvorhersage habe ich eine end to end Pipeline mit sechs Klassifikatoren und 10 facher Kreuzvalidierung gebaut, biologisch unmoegliche Nullwerte im Quelldatensatz erkannt und durch IQR basierte Ausreisserbehandlung korrigiert, die Leitmetrik von Accuracy auf ROC AUC umgestellt und die Ergebnisse in einem IEEE Style Paper aufgeschrieben, das der Betreuer als veroeffentlichungsreif akzeptierte. Dazu kommt CreditIQ, in dem ich unter EU AI Act und AGG 80 Prozent Fairness Grenze den Disparate Impact von 0,79 auf 0,88 gehoben habe. Beide Arbeiten zeigen, dass ich eine Masterarbeit zwischen Methodik, Codebasis und ehrlicher schriftlicher Auswertung selbststaendig fuehren kann.",
            "Ich arbeite sicher in Python, scikit-learn, LangGraph, pandas, NumPy und Jupyter sowie in AWS und GCP. Ich halte die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Englisch spreche ich fliessend, mein Deutsch liegt bei B1 laufend. Fuer eine Vollzeit Masterarbeit stehe ich ab Oktober 2026 in Dortmund zur Verfuegung; universitaetsseitige Betreuung wird durch die SRH Heidelberg Fakultaet gestellt. Gerne bespreche ich Themenzuschnitt und Rahmen in einem persoenlichen Gespraech.",
        ],
    },
]
