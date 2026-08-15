# Rahul Rawat

## Data Science Intern

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on experience in Python and PySpark, dashboard driven analytics, and cross functional data delivery on real production style data. I have shipped a real time flight tracking pipeline processing over 128 thousand records with PySpark on Google Cloud, an automated Bronze to Silver to Gold BigQuery medallion architecture with a leakage free BigQuery ML classifier and a five page Looker Studio dashboard, and an interactive Tableau dashboard with dynamic Set Actions and parameter driven analytics for non technical stakeholders. Comfortable in Python, PySpark, SQL, dashboard tooling that transfers directly to Power BI, and clear stakeholder communication, I am the right fit for the six month Data Science Praktikum at Johnson and Johnson in Norderstedt.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
