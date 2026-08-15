"""One-off refresh, 20 July 2026.

Regenerates the CV and cover letter for the Johnson & Johnson Data Science Intern
posting (R-086518, Norderstedt) using the current 19 July template.

Language track: English. The posting is fully bilingual English + German, and per
the 20 July 2026 language match rule the tie breaker for near 50 50 postings is the
stated working language. "Fluency in English" is the explicit required working
language; no German language requirement is stated. English track wins.

Application status: already applied on 18 July 2026. This refresh overwrites the
existing draft folder in place at Rah's explicit request. Neither applied-log.csv
nor the Notion mirror is touched.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_html import build_role
from role_configs import (
    ERAY_BULLETS_EN,
    DIABETES_BULLETS_EN,
    CERT_SAS,
    CERT_GOOGLE,
    CERT_AWS,
    ACH_USAII_EN,
    P_FLIGHT_EN,
    P_MOVIE_EN,
    P_TABLEAU_EN,
)


cfg = {
    "folder": "Johnson and Johnson Data Science Praktikum Norderstedt",
    "company": "Johnson & Johnson",
    "lang": "en",
    "role_strip": "Data Science Intern",
    "cl_date": "20 July 2026",
    "cl_subject": "Data Science Intern, Praktikum m w d, R 086518 in Norderstedt",
    "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on experience in Python and PySpark, dashboard driven analytics, and cross functional data delivery on real production style data. I have shipped a real time flight tracking pipeline processing over 128 thousand records with PySpark on Google Cloud, an automated Bronze to Silver to Gold BigQuery medallion architecture with a leakage free BigQuery ML classifier and a five page Looker Studio dashboard, and an interactive Tableau dashboard with dynamic Set Actions and parameter driven analytics for non technical stakeholders. Comfortable in Python, PySpark, SQL, dashboard tooling that transfers directly to Power BI, and clear stakeholder communication, I am the right fit for the six month Data Science Praktikum at Johnson and Johnson in Norderstedt.",
    "experience_bullets": ERAY_BULLETS_EN,
    "projects": [P_FLIGHT_EN, P_MOVIE_EN, P_TABLEAU_EN],
    "research_bullets": DIABETES_BULLETS_EN,
    "certifications": [CERT_SAS, CERT_GOOGLE, CERT_AWS],
    "achievements": [ACH_USAII_EN],
    "cl_paragraphs": [
        "I am applying for the Data Science Intern role, Praktikant:in m w d, requisition R 086518 at Johnson and Johnson in Norderstedt. The brief on performing data extraction, transformation, and analysis across databases, APIs, and IoT data, designing and building interactive Power BI dashboards, translating business requirements into data driven insights, supporting data modelling and feature engineering, and ensuring data quality through validation and consistency checks, matches the shape of work I have been shipping over the past year.",
        "In my Real Time Flight Tracking Data Pipeline I processed more than 128 thousand records with PySpark on Google Cloud, collecting live flight positions from the OpenSky Network API every 30 seconds and enriching them against airport, aircraft, and weather data across four sources, then shaping the output with dbt into analysis ready tables and orchestrating the whole system with Apache Airflow so batch and real time layers refresh automatically every 15 minutes. That is directly the API, IoT style, and PySpark experience your team is asking for. In my Movie Analytics and ML Pipeline on GCP I built an end to end Bronze to Silver to Gold BigQuery medallion architecture with schema enforcement, safe type casting, deduplication via window functions, and a leakage free BigQuery ML classifier, then delivered a five page Looker Studio dashboard for concrete business questions. Looker Studio is a close cousin of Power BI and my dashboard thinking translates one to one.",
        "In my Fast Food Nutritional Analyzer and Meal Simulator I built a two tier Tableau dashboard combining an executive macro view with a granular detail view, using Set Actions and parameter driven fields so non technical users can explore the data directly and reach insight faster. At eRay GmbH I delivered a recursive time series pipeline with strict anti leakage rules, quantile regression prediction intervals, and an orchestrator with gate checks that halts on failed imputation rather than letting bad data cascade. That combination of dashboarding, ML modelling, and honest data quality is exactly what a healthcare data team needs.",
        "I am proficient in Python and PySpark, comfortable in SQL and relational modelling, and hold the SAS Certified Specialist Visual Business Analytics Using SAS Viya, Google Data Analytics Foundations, and AWS Academy Cloud Foundations certificates. My English is fluent at C1 level in written and spoken form, and my current German level is B1 in progress toward B2. I would be glad to start the six month Praktikum in Norderstedt with a relocation from Mannheim, and to contribute across engineering, operations, and digital teams from the first week.",
    ],
}


if __name__ == "__main__":
    build_role(cfg)
