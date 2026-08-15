# Rahul Rawat

## Working Student, Data Analytics

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on SQL, Python, dashboarding, and end to end data analytics delivery on real operational data. I have shipped a fully automated BigQuery medallion pipeline feeding a five page Looker Studio dashboard for concrete business questions, an interactive two tier Tableau dashboard with dynamic Set Actions and parameter driven analytics on a colour blind safe palette, and a real time cloud pipeline processing more than 128 thousand records on Google Cloud with dbt and Apache Airflow. Proficient in SQL and Python with practical BI experience, I am the right fit for a dynamic, multicultural Data Analytics working student role at TK Elevator in Duesseldorf.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* During a six month eRay GmbH and SRH Heidelberg collaboration to forecast water quality on a German lake, tasked with covering four indicators over rolling horizons, built an end to end recursive time series pipeline for chlorophyll a, turbidity, pH, and dissolved oxygen, delivered as a production ready module the client can rerun on every new sensor drop.
* Faced with model choice ambiguity for the forecasting task and the need to convey uncertainty to non technical stakeholders, benchmarked six candidates head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, then landed on CatBoost multi quantile regression, which produced asymmetric 80 percent prediction intervals that gave the client decision support under uncertainty.
* Concerned that naive time series splits would inflate accuracy, tasked with making the evaluation defensible, enforced strict anti leakage rules across the pipeline, which surfaced the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* With winter readings missing and tree based models flatlining during recursive prediction, needing realistic seasonal shape in the downstream forecasts, reconstructed missing values with MICE imputation and engineered a synthetic winter decay forecast canvas, which restored believable winter behaviour without introducing bias into the training window.
* To prevent bad data cascading downstream through the recursive forecaster, tasked with hardening the run loop, wrapped the pipeline in an orchestrator with gate checks and velocity and ecological bounds, so a failed imputation now halts the run rather than corrupting weeks of downstream predictions.
