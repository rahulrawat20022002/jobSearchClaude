"""Ad-hoc single-role tailoring: Deutsche Telekom AG Flexikum (Data & AI in
Financial Controlling), pasted JD from Rah on 16 August 2026.

Note: JD is a freiwilliges Praktikum ("Flexikum"). Master-projects.md drops
voluntary internships by default. Rah requested this one directly, so it is
tailored ad-hoc outside the scheduled backlog gate. Not added to Notion / CSV
by this script (that's a manual decision).

Language: DE (posting body in German).
Best-fit anchors: #2 CreditIQ (Financial + regulated AI + Streamlit decision
support with LLM-generated explanation) and #8 Climate Economics (Random Forest
Predictive Analytics with business framing -- direct hit on the "Praktische
Erfahrungen mit Predictive Analytics" requirement).
Certifications lead: SAS Visual Business Analytics (BI/Power BI angle) + NVIDIA
LLM Applications (AI angle) + Google Data Analytics.
"""

from role_configs import (
    ERAY_BULLETS_DE,
    DIABETES_BULLETS_DE,
    CERT_NVIDIA_DE,
    CERT_SAS_DE,
    CERT_GOOGLE_DE,
    ACH_USAII_DE,
    P_CREDITIQ_DE,
    P_CLIMATE_DE,
)


CONFIGS_16AUG_TELEKOM = [
    # Deutsche Telekom AG -- Flexikum (Praktikum), Data & AI in Financial
    # Controlling. Start 01.10.2026, 20h/week, Teilzeit moeglich.
    {
        "folder": "Deutsche Telekom Flexikum Data AI Financial Controlling",
        "company": "Deutsche Telekom AG",
        "lang": "de",
        "role_strip": "Flexikum, Data und AI im Financial Controlling",
        "cl_date": "16. August 2026",
        "cl_subject": "Flexikum, Data und AI im Financial Controlling ab 01.10.2026",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Predictive Analytics Modellen, BI Dashboards und KI Werkzeugen in regulierten und finanznahen Kontexten. Ich habe in CreditIQ ein Kredit Scoring System unter EU AI Act Konformitaet gebaut, das als Streamlit Entscheidungsunterstuetzung mit einer plain language LLM generierten Erklaerung laeuft, und in einer Random Forest gestuetzten Wirtschaftsanalyse globaler Klimaereignisse Risiko Konzentrationen fuer die Ressourcenallokation transparent gemacht. Sicher in Python, SQL, scikit-learn, Power BI, Tableau, Looker Studio und in den ueblichen Cloud Stacks AWS und GCP.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_CLIMATE_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_SAS_DE, CERT_NVIDIA_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer das Flexikum im Bereich Data und AI im Financial Controlling bei der Deutschen Telekom AG mit Start zum 1. Oktober 2026. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg interessiert mich die Kombination aus datengetriebener Prozessoptimierung im Controlling, Predictive Analytics, Power BI Dashboards und dem gezielten Einsatz von KI besonders, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut und ausgewertet habe.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent bei stabiler Accuracy von 75 Prozent gefallen, und das System laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer, gestuetzt durch Unit Tests bei 100 Prozent Branch Coverage und einer vollstaendigen regulatorischen Dokumentation zu GDPR Artikel 22 und EU AI Act Artikel 14. Genau dieses Muster, Modellergebnisse in nachvollziehbare Entscheidungsunterstuetzung fuer Finanz und Controlling Teams zu ueberfuehren, laesst sich direkt auf den Einsatz von Data und AI im Financial Controlling der Telekom uebertragen.",
            "In einem Predictive Analytics Projekt zur wirtschaftlichen Auswirkung globaler Klimaereignisse habe ich Random Forest Modelle entwickelt, um Zusammenhaenge zwischen Ereignisdauer und finanzieller Auswirkung zu analysieren, und die Ergebnisse ueber Feature Importance Rankings sowie Residualanalyse in klare wirtschaftliche Aussagen zur Risiko Konzentration ueberfuehrt. Fuer die Daten Grundlage habe ich Ausreisser Bereinigung, Imputation und Skalierung durchgefuehrt und die Modellergebnisse fuer ein nicht technisches Management Publikum in kalibrierten Konfidenz Aussagen und aussagekraeftigen Visualisierungen aufbereitet, die einen Management Review ohne weitere Uebersetzung ueberstanden haben. Diese Kombination aus Predictive Modell, kritischer Datenaufbereitung und geschaeftlicher Interpretation entspricht genau dem, was die Rolle in der Optimierung datengetriebener Finanz und Controlling Prozesse fordert.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, Power BI, Tableau und Looker Studio, habe zusaetzlich in einem Tableau Projekt mit Set Actions und parameter gesteuerten Analysen dynamische Dashboards fuer wechselnde Business Perspektiven umgesetzt und bringe Erfahrung mit Cloud gestuetzten Data Pipelines auf AWS und GCP mit, zum Beispiel BigQuery ML fuer eine leakage freie Klassifikation. Ich habe die SAS Certified Specialist Visual Business Analytics, NVIDIA Building LLM Applications With Prompt Engineering und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung, Englisch spreche ich fliessend. Ich kann als Flexikant zum 1. Oktober 2026 mit 20 Stunden pro Woche einsteigen und stehe fuer ein persoenliches Gespraech gerne zur Verfuegung.",
        ],
    },
]
