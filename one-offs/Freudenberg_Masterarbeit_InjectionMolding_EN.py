"""One-off draft, 4 August 2026.

Draft for Freudenberg Technology Innovation SE & Co. KG, Master's Thesis in
the Field of Data Science / Machine Learning in Injection Molding (f/m/d),
Weinheim, on-site. Contact: Julia Henrich, julia.henrich@freudenberg.com.

Explicit user override outside the current backlog pause. Rah asked for this
listing specifically from the Freudenberg career page URL.

Same role as the existing 7/26/26 drafted row in applied-log.csv, which was
tailored in German off the StepStone posting body. This one-off ships the
English variant off the Freudenberg career page body, which is written in
English. Per the 20 July 2026 language match hard rule, deliverables ship in
English. Rah can pick either draft to apply with; the CSV row already exists,
so no new CSV or Notion entry is added.

Best project fit:
- Project #5 Movie Analytics on GCP, leakage free BigQuery ML classifier plus
  Bronze to Silver to Gold pipeline and Looker Studio dashboards. Direct
  match for the classification and honest evaluation ask.
- Project #3 Real Time Flight Tracking Pipeline, PySpark on GCP joining live
  sensor data across four sources with dbt and Airflow. Direct match for
  preparing production and process data.
Research and Thesis renders the Bachelor thesis on Diabetes Prediction as a
research writeup signal.

Certifications lead with AWS Academy Cloud Foundations, SAS Visual Business
Analytics for the visualization angle, and Google Data Analytics Foundations
for the reporting workflow piece.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_html import build_role
from role_configs import (
    ERAY_BULLETS_EN,
    DIABETES_BULLETS_EN,
    CERT_AWS,
    CERT_SAS,
    CERT_GOOGLE,
    ACH_USAII_EN,
    P_MOVIE_EN,
    P_FLIGHT_EN,
)


cfg = {
    "folder": "Freudenberg Masterarbeit Data Science ML Injection Molding EN",
    "company": "Freudenberg Technology Innovation",
    "lang": "en",
    "role_strip": "Master Thesis, Data Science and Machine Learning in Injection Molding",
    "cl_date": "4 August 2026",
    "cl_subject": "Master's Thesis in Data Science and Machine Learning in Injection Molding in Weinheim",
    "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on delivery of machine learning pipelines on real sensor and process data, honest leakage aware evaluation, and end to end analytics for technical stakeholders. At eRay GmbH I built a recursive time series pipeline forecasting four water quality indicators, benchmarking six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and shipped it with strict anti leakage rules and asymmetric 80 percent prediction intervals. Proficient in Python, pandas, scikit learn, and comfortable across the wider ML stack, I am the right fit for the Master's Thesis in Data Science and Machine Learning in Injection Molding at Freudenberg Technology Innovation in Weinheim.",
    "experience_bullets": ERAY_BULLETS_EN,
    "projects": [P_MOVIE_EN, P_FLIGHT_EN],
    "research_bullets": DIABETES_BULLETS_EN,
    "certifications": [CERT_AWS, CERT_SAS, CERT_GOOGLE],
    "achievements": [ACH_USAII_EN],
    "cl_paragraphs": [
        "I am applying for the Master's Thesis in the Field of Data Science and Machine Learning in Injection Molding at Freudenberg Technology Innovation in Weinheim. The brief on analyzing and preparing production and process data from injection molding systems, identifying influencing factors on part quality, cycle time, and scrap rates, developing regression, classification, and anomaly detection models, and translating results into actionable process optimization recommendations for technical stakeholders, maps directly to the work I have been shipping over the past year.",
        "At eRay GmbH I built an end to end recursive time series pipeline forecasting four water quality indicators, chlorophyll a, turbidity, pH, and dissolved oxygen, and benchmarked six models head to head including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, using CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty. I enforced strict anti leakage rules across the pipeline and surfaced the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors. That leakage aware and honest evaluation mindset is exactly what a Master's Thesis on injection molding process data needs, where cycle time, part quality, and scrap rates all depend on getting the evaluation right rather than reading a plausible looking accuracy number.",
        "In my Movie Analytics and ML Pipeline on GCP I trained a leakage free BigQuery ML classifier that predicts a target before release, deliberately splitting features into two tables so only pre release signals feed the model, and delivered a five page Looker Studio dashboard for concrete business questions. In my Real Time Flight Tracking Pipeline I processed over 128 thousand records with PySpark on Google Cloud, collecting live positions from an API every 30 seconds and joining them against airport, aircraft, and weather data across four sources with dbt, orchestrated by Apache Airflow so batch and real time layers refresh every 15 minutes. Both projects show I can build the ingestion, preparation, modelling, and visualization layers a manufacturing analytics thesis needs, end to end.",
        "I am proficient in Python and comfortable with pandas, scikit learn, and PyTorch, and I hold the AWS Academy Cloud Foundations, SAS Certified Specialist Visual Business Analytics Using SAS Viya, and Google Data Analytics Foundations certificates. My English is fluent working proficiency and my current German level is B1 in progress toward B2, and I meet the very good German or English requirement in English. I am interested in continuing into an industrial PhD after the thesis and would be glad to align the exact scope of the injection molding data set and evaluation criteria with the Weinheim team.",
    ],
}


if __name__ == "__main__":
    build_role(cfg)
