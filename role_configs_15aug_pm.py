"""Role configurations for the 15 August 2026 afternoon scheduled run.

Backlog gate check per 14 July 2026 status source of truth rule: Notion
data source fd974369-40b2-48c5-b660-d15256c88f52 returned 5 rows in status
'drafted' at run start (the five drafted earlier today: Retorio,
AssetMetrix GmbH, Phoenix Contact, BSH Home Appliances Group, viadee
Unternehmensberatung AG). CSV in agreement, no drift. 5 drafted rows is
under the 8 row soft cap and the 11 row hard pause, so the normal top 3
to 5 cut applies per the 28 July 2026 yield based reset rule.

Reconciliation step per 11 July 2026 rule: one CSV drift found and fixed
before the search step. HDI AG row showed 'Not listed Anymore' in the CSV
while Notion carried 'applied'; Notion is the source of truth per the 14
July 2026 rule, so the CSV was updated to match. All other CSV rows in
sync with Notion at run start.

Platform mix per 28 July 2026 yield based reset weighting for a top 3
cut, aiming for LinkedIn 2, career page 1 to 2, StepStone 1, Xing 1,
Indeed 0 to 1. Today's earlier run already covered LinkedIn 4 and Xing 1,
so this run tilts toward career page + Xing to fill the balance:
  - Career page: 1 (BMW)
  - Xing: 2 (KfW Bankengruppe, Allianz Insurance)
  - LinkedIn: 0 this run (already fully covered by earlier run today)
  - StepStone: 0 this run (kept for next run to preserve mix over time)
  - Indeed: 0 this run

Freshness order per 12 July 2026 priority rule (freshness first, then
role type, then Best for overlap), within the single Germany tier:
  1. BMW AG Muenchen Werkstudent Data Science und KI Tool Entwicklung
     fuer Qualitaetsanalyse, posted ~2 days ago on bmwgroup.jobs career
     page, Werkstudent, DE track
  2. KfW Bankengruppe Frankfurt Werkstudent im Bereich IT Data Science
     und KI, posted 2 days ago on Xing, Werkstudent, DE track
  3. Allianz Insurance Muenchen Working Student Data Science, posted 3
     days ago on Xing, Werkstudent, EN track

Language track per 20 July 2026 language match hard rule (posting body
language IS deliverable language):
  1. BMW posting body in German at bmwgroup.jobs -> DE track
  2. KfW posting body in German on Xing -> DE track
  3. Allianz posting listed as "Working Student - Data Science (m/f/d)"
     with EN title on Xing, posting body written primarily in English
     (Allianz uses English for cross border DS teams) -> EN track

Dedup check: all three company plus role combinations verified absent
from applied-log.csv and Notion.
  - BMW Group is in the log for other Werkstudent, Master Thesis, and
    Abschlussarbeit roles including the recently applied Data-Analytics
    Qualitaetsmanagement fuer Digitale Dienste, but this is a distinct
    Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse role,
    allowed under the 'different roles at the same company' rule.
  - KfW Bankengruppe is a new company, no prior rows in the log.
  - Allianz has an applied row for "Werkstudent Data Analyst" at Allianz
    Versicherungs-AG. This is a different Working Student Data Science
    role at Allianz Insurance (the sister entity), allowed under the
    'different roles' rule.
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
    P_CREDITIQ_DE,
    P_FLIGHT_EN,
    P_FLIGHT_DE,
    P_MOVIE_EN,
    P_MOVIE_DE,
    P_TABLEAU_EN,
    P_TABLEAU_DE,
    P_CLIMATE_EN,
    P_CLIMATE_DE,
)


CONFIGS_15AUG_PM = [
    # 1. BMW Group Muenchen
    # Werkstudent Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse (w/m/x)
    # bmwgroup.jobs career page, posted ~2 days ago, Werkstudent, DE track
    # Location: Muenchen, hybrid, Teilzeit
    # Apply: https://www.bmwgroup.jobs/de/de/jobfinder.html?query=Werkstudent+Data+Science+KI+Tool+Qualitaetsanalyse
    {
        "folder": "BMW Muenchen Werkstudent Data Science KI Tool Qualitaetsanalyse",
        "company": "BMW Group",
        "lang": "de",
        "role_strip": "Werkstudent Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse",
        "cl_date": "15. August 2026",
        "cl_subject": "Werkstudent Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Machine Learning Pipelines, LLM Werkzeugen und Qualitaets naher Analyse. Ich habe bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile und 80 Prozent Vorhersageintervallen fuer 4 Umweltindikatoren geliefert und ein Multi Agent RAG System mit LangGraph, Ollama Mistral 7B und Qwen2.5 14B sowie einer belastbaren LLM as Judge Evaluation ueber 5 Dimensionen aufgebaut. Sicher in Python, SQL, scikit-learn, LangGraph, Prophet, CatBoost, GCP und AWS.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_RAG_DE, P_CREDITIQ_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit Data Science und KI Tool Entwicklung fuer Qualitaetsanalyse am Standort Muenchen. Die Kombination aus Datenanalyse, Entwicklung eigener KI Werkzeuge zur Qualitaetssicherung und der Uebersetzung von Modellergebnissen in umsetzbare Erkenntnisse deckt sich sehr gut mit dem, was ich in den letzten Monaten praktisch gebaut habe.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes System aufgebaut, das Antworten in Englisch oder Deutsch end to end liefert und dabei ueber einen JudgeAgent auf 5 Dimensionen im JSON Modus bei Temperatur 0 bewertet wird. Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B bewusst auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft, und ein EvalAgent berechnet 5 Retrieval Metriken sowie 4 Generation Metriken pro Sprache in JSON und Markdown Reports auf einem gepaarten EN und DE Labeled Eval Set. Genau dieses Muster laesst sich direkt auf ein KI Werkzeug fuer die Qualitaetsanalyse uebertragen, wo Modelausgaben belastbar und pruefbar bewertet werden muessen, statt auf Bauchgefuehl zu laufen.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und mit SHAP getriebener Subgruppenanalyse eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert. Die False Negative Rate ist von 44 Prozent auf 16,7 Prozent gefallen bei einer stabilen Accuracy von 75 Prozent. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren geliefert und CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen als Shipped Modell gewaehlt, wobei ich die September Evaluation mit einem 3 Pass Outlier System belastbar gemacht habe.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph, CatBoost und Prophet sowie in AWS und GCP fuer die Cloud Ebene. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung Richtung B2, Englisch spreche ich fliessend. Ich kann als Werkstudent in Muenchen mit 15 bis 20 Stunden pro Woche in einem hybriden Setup einsteigen. Gerne bespreche ich meinen Beitrag zu Ihrem Data Science und KI Tool Team fuer Qualitaetsanalyse in einem persoenlichen Gespraech.",
        ],
    },

    # 2. KfW Bankengruppe Frankfurt am Main
    # Werkstudent (w/m/d) im Bereich IT - Data Science & KI
    # Xing, posted 2 days ago, Werkstudent, DE track
    # Location: Frankfurt am Main, hybrid, Teilzeit
    # Apply: https://www.xing.com/jobs/frankfurt-main-werkstudent-it-data-science-ki
    {
        "folder": "KfW Bankengruppe Frankfurt Werkstudent IT Data Science KI",
        "company": "KfW Bankengruppe",
        "lang": "de",
        "role_strip": "Werkstudent im Bereich IT, Data Science und KI",
        "cl_date": "15. August 2026",
        "cl_subject": "Werkstudent im Bereich IT, Data Science und KI",
        "profile": "Masterstudent der Data Science and Analytics an der SRH Heidelberg mit Sitz in Mannheim und praktischer Erfahrung im Aufbau von Data Pipelines, Machine Learning Modellen und LLM Werkzeugen in regulierten Umgebungen. Ich habe in CreditIQ ein Kredit Scoring System entwickelt, das den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent gesenkt hat, und bei eRay GmbH eine end to end rekursive Zeitreihen Pipeline mit CatBoost MultiQuantile fuer 4 Umweltindikatoren geliefert. Sicher in Python, SQL, scikit-learn, LangGraph, BigQuery, Airflow, Tableau und Looker Studio.",
        "experience_bullets": ERAY_BULLETS_DE,
        "projects": [P_CREDITIQ_DE, P_RAG_DE],
        "research_bullets": DIABETES_BULLETS_DE,
        "certifications": [CERT_NVIDIA_DE, CERT_AWS_DE, CERT_GOOGLE_DE],
        "achievements": [ACH_USAII_DE],
        "cl_paragraphs": [
            "hiermit bewerbe ich mich fuer die Werkstudententaetigkeit im Bereich IT, Data Science und KI bei der KfW Bankengruppe am Standort Frankfurt am Main. Als Masterstudent der Data Science and Analytics an der SRH Heidelberg interessiert mich die Kombination aus regulierter Finanzumgebung, angewandter Datenanalyse und produktiven KI Werkzeugen besonders, weil ich in den letzten Monaten genau an dieser Schnittstelle Systeme gebaut habe.",
            "In CreditIQ habe ich unter EU AI Act und AGG 80 Prozent Fairness Grenze ein Kredit Scoring System entwickelt, den Disparate Impact von 0,79 auf 0,88 gehoben und die False Negative Rate von 44 Prozent auf 16,7 Prozent bei einer stabilen Accuracy von 75 Prozent gesenkt. Mit SHAP getriebener Subgruppenanalyse habe ich eine intersektionelle Verzerrung ueber Alter und Geschlecht aufgedeckt und ueber ein vierstufiges Threshold Raster korrigiert, ohne in umgekehrte Diskriminierung zu kippen, und das Modell laeuft als Streamlit Decision Support Tool mit einer plain language LLM generierten Erklaerung fuer den Endbenutzer. Genau dieses Muster, Modellergebnisse in regulator taugliche Entscheidungsunterstuetzung zu ueberfuehren, laesst sich direkt auf KfW Kernfaelle wie Kreditbewertung und Risiko Analyse anwenden.",
            "In meinem Multi Agent RAG Projekt habe ich ein LangGraph orchestriertes Agentensystem gebaut, das Antworten in Englisch oder Deutsch end to end liefert. Der JudgeAgent bewertet Antworten auf 5 Dimensionen im JSON Modus bei Temperatur 0, und Self Preference Bias wurde eliminiert, indem der Judge Qwen2.5 14B auf einem anderen lokalen Modell als der Generator Mistral 7B laeuft. Ein EvalAgent liefert 5 Retrieval Metriken und 4 Generation Metriken pro Sprache in JSON und Markdown Reports, so dass A/B Vergleiche zwischen Modellvarianten belastbar werden. Bei eRay GmbH habe ich zusaetzlich eine end to end rekursive Zeitreihen Pipeline fuer 4 Wasserqualitaets Indikatoren geliefert und CatBoost Multi Quantil Regression mit asymmetrischen 80 Prozent Vorhersageintervallen als Shipped Modell gewaehlt.",
            "Ich arbeite sicher in Python, SQL, scikit-learn, LangGraph, BigQuery, Airflow und den ueblichen Cloud Plattformen AWS und GCP. Ich habe die NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations und Google Data Analytics Zertifikate abgelegt und wurde als Finalist des USAII Global AI Hackathon 2026 auf Graduate Level ausgezeichnet. Mein Deutschniveau ist B1 in Bearbeitung Richtung B2, Englisch spreche ich fliessend. Ich kann als Werkstudent in Frankfurt am Main mit 15 bis 20 Stunden pro Woche einsteigen. Gerne bespreche ich meinen Beitrag zum IT Data Science und KI Team der KfW in einem persoenlichen Gespraech.",
        ],
    },

    # 3. Allianz Insurance Muenchen
    # Working Student - Data Science (m/f/d)
    # Xing, posted 3 days ago, Werkstudent, EN track
    # Location: Muenchen, hybrid, Teilzeit
    # Apply: https://www.xing.com/jobs/muenchen-working-student-data-science
    {
        "folder": "Allianz Insurance Muenchen Working Student Data Science",
        "company": "Allianz Insurance",
        "lang": "en",
        "role_strip": "Working Student, Data Science",
        "cl_date": "15 August 2026",
        "cl_subject": "Working Student, Data Science in Munich",
        "profile": "Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience building machine learning pipelines, LLM tools, and decision support systems in regulated settings. I built CreditIQ, a fairness by design credit scoring system that lifted the Disparate Impact ratio from 0.79 to a compliant 0.88 and cut the false negative rate from 44 percent to 16.7 percent, and delivered a recursive time series pipeline for 4 water quality indicators at eRay GmbH using CatBoost MultiQuantile with 80 percent prediction intervals. Comfortable across Python, SQL, scikit-learn, LangGraph, GCP and AWS.",
        "experience_bullets": ERAY_BULLETS_EN,
        "projects": [P_CREDITIQ_EN, P_RAG_EN],
        "research_bullets": DIABETES_BULLETS_EN,
        "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
        "achievements": [ACH_USAII_EN],
        "cl_paragraphs": [
            "I am writing to apply for the Working Student position in Data Science at Allianz Insurance in Munich. As a Master's student in Data Science and Analytics at SRH Heidelberg based in Mannheim, the combination of applied machine learning inside a regulated financial services environment, honest evaluation, and translating model outputs into actionable insights maps closely to the projects I have shipped in the last several months.",
            "In CreditIQ I built an end to end credit scoring system under the EU AI Act and AGG 80 percent fairness bar, applying AIF360 mitigation and threshold calibration on a real credit dataset, which raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88. I used SHAP driven subgroup analysis to expose a hidden intersectional bias across age and gender and designed a four way threshold matrix that corrected it without over correcting into reverse discrimination, and the false negative rate dropped from 44 percent to 16.7 percent while accuracy held at 75 percent on the held out split. The system runs as a Streamlit decision support tool with a plain language LLM generated explanation, backed by unit tests at 100 percent branch coverage and a full regulatory write up covering GDPR Article 22 and EU AI Act Article 14 human in the loop requirements.",
            "In my Multi Agent RAG project I built a LangGraph orchestrated agent system that answers questions in English or German end to end. I implemented a JudgeAgent that scores answers on 5 dimensions using JSON mode at temperature 0 and eliminated self preference bias by running the judge Qwen2.5 14B on a different local model from the generator Mistral 7B, plus an EvalAgent computing 5 retrieval metrics and 4 generation metrics aggregated per language into JSON and Markdown reports. At eRay GmbH I delivered a recursive time series pipeline for four water quality indicators and chose CatBoost Multi Quantile regression with asymmetric 80 percent prediction intervals as the shipped model, making the September evaluation defensible with a 3 pass outlier system.",
            "I work comfortably in Python, SQL, scikit-learn, LangGraph, and the usual AWS and GCP cloud stacks. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations and Google Data Analytics certificates and was recognised as a Finalist of the USAII Global AI Hackathon 2026 at Graduate Level. I am fluent in English and B1 in progress in German. I can join in Munich as a Working Student for 15 to 20 hours a week in a hybrid setup immediately. I would welcome the chance to discuss how I could contribute to your Data Science team.",
        ],
    },
]
