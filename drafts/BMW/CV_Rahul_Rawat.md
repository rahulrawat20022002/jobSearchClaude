# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg with practical experience across SQL, Python, cloud data warehouses, and visualisation tools. My cloud pipeline projects have covered live ingestion, medallion architecture in BigQuery, dbt transformations, and Tableau reporting with statistics served through TabPy, which fits the Cloud Data Hub and dashboard focus of the Programmplanung Antrieb team. I bring a structured analytical mindset and enjoy turning production and capacity data into clear planning support.

## Education

**M.Sc. Data Science and Analytics**  |  Apr 2025 to Present
*SRH University of Applied Sciences Heidelberg*

**Bachelor of Technology in Computer Science**  |  2019 to 2023
*GL Bajaj Institute of Technology and Management*

## Experience

**eRay GmbH**
*Data Scientist · Oct 2025 to Mar 2026*

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.

## Personal Projects

**Real Time Flight Tracking Data Pipeline**: *Python, PySpark, BigQuery, dbt, Apache Airflow, GCP Dataproc, GCE, GCS, Tableau, TabPy, OAuth2*

* Set up real time data collection from the OpenSky Network API, polling live flight positions every 30 seconds and enriching each observation against airport, aircraft, and weather data from four external sources.
* Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft's nearest airport along the way and yielding more than 128 thousand joined records.
* Orchestrated the whole system with Apache Airflow so that the batch and real time layers refresh automatically every 15 minutes with no manual intervention.
* Surfaced findings in Tableau with Python statistics served through TabPy, showing that air traffic dropped by a factor of 4.4 in heavy rain and clustered heavily around hubs such as Frankfurt and Munich.

**Movie Analytics and ML Pipeline, Cloud Native Data Platform**: *GCP BigQuery, Cloud Run, GCS, Cloud Scheduler, BigQuery ML, Python, SQL, Looker Studio*

* Built an end to end batch pipeline pulling movie data from a public API into a GCS data lake, processed through a Bronze to Silver to Gold medallion architecture in BigQuery, and fully automated on a Cloud Scheduler trigger with no manual steps.
* Engineered the Silver layer for trustworthy analytics with schema enforcement, safe type casting, deduplication through window functions, and genre normalisation into a relational model.
* Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage so that only pre release signals feed the model.
* Built Gold layer aggregates and a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing, plus an ML early warning view.
* Secured the system with a least privilege service account and Secret Manager and version controlled all code, SQL, and schemas in a reproducible GitHub repository.

**Fast Food Nutritional Analyzer and Meal Simulator**: *Tableau with Set Actions, Dashboard Actions, parameters, and calculated fields*

* Built a dynamic shopping cart in Tableau using Set Actions, letting users select scatter plot points to instantly total calories, fat, and protein for a simulated meal.
* Implemented parameter driven analytics through a dynamic Y axis tied to a user controlled goal parameter for muscle gain versus weight loss, driven by a CASE statement.
* Authored complex order of operation IF THEN calculated fields for logical grouping and custom flags, for example an Is It A Trap flag for deceptive high fat and high calorie items.
* Designed a two tier layout with an executive macro view and a granular food finder, using a colour blind safe dark mode palette to reduce time to insight.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical diabetes dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
