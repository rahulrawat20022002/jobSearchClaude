# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on experience translating raw operational data into business analytics and dashboards. I have shipped an interactive Tableau dashboard with dynamic parameters, a five page Looker Studio dashboard on top of a BigQuery medallion warehouse, and a Random Forest study on the economic impact of global events. Comfortable with SQL, cloud data platforms, and clean data storytelling, I am well suited to strengthen the Data and Analytics function at PENNY.

## Education

**M.Sc. Data Science and Analytics**  |  Apr 2025 to Present
*SRH University of Applied Sciences Heidelberg*

**Bachelor of Technology in Computer Science**  |  2019 to 2023
*GL Bajaj Institute of Technology and Management*

## Experience

**eRay GmbH**
*Data Scientist · Oct 2025 to Mar 2026*

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction on a limited prediction horizon.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.

## Personal Projects

**Movie Analytics and ML Pipeline, Cloud Native Data Platform**: *GCP BigQuery, Cloud Run, GCS, Cloud Scheduler, BigQuery ML, Python, SQL, Looker Studio*

* Built an end to end batch pipeline pulling data from a public API into a GCS data lake, processed through Bronze to Silver to Gold medallion architecture in BigQuery, fully automated on a Cloud Scheduler trigger with no manual steps.
* Engineered the Silver layer for trustworthy analytics with schema enforcement, safe type casting, deduplication via window functions, and normalisation into a relational model.
* Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage and keeping only pre release signals.
* Built Gold layer aggregates and a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing, plus an ML early warning view.
* Secured the system with a least privilege service account and Secret Manager and version controlled all code, SQL, and schemas in a reproducible GitHub repository.

**Fast Food Nutritional Analyzer and Meal Simulator**: *Tableau with Set Actions Dashboard Actions parameters and calculated fields, data storytelling, UI and UX*

* Built a dynamic shopping cart using Tableau Set Actions, letting users select scatter plot points to instantly total calories, fat, and protein for a simulated meal.
* Implemented parameter driven analytics with a dynamic Y axis via a CASE statement tied to a user controlled goal parameter for muscle gain versus weight loss.
* Authored complex order of operation IF THEN calculated fields for logical grouping and custom flags such as Is It A Trap for deceptive high fat and high calorie items.
* Designed a two tier layout with an executive macro view and a granular food finder, using a colour blind safe dark mode palette to reduce time to insight.

**Economic Impact Analysis of Global Climate Events**: *Python with Pandas and scikit learn, Random Forest, statistical modelling, Matplotlib and Seaborn*

* Executed an end to end data science project transforming raw global event datasets into structured insights for resource allocation and risk assessment.
* Performed advanced data preparation and cleansing across outliers, imputation, and normalisation to build a high quality data foundation before any modelling.
* Developed Random Forest models to analyse correlations between event duration and financial impact, extracting clear business relevant insights on where economic risk concentrates.
* Communicated complex statistical findings to non technical stakeholders through comprehensive visual reports and calibrated confidence statements.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications

* SAS Certified Specialist, Visual Business Analytics Using SAS Viya: issued May 2025.
* Google Data Analytics, Foundations, Data, Data, Everywhere: issued April 2025 on Coursera.

## Achievements

* USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
