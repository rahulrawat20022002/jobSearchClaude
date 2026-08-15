# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on experience building hybrid cloud and on premise data pipelines. My Real Time Flight Tracking pipeline joins live positions to airport, aircraft, and weather data every 15 minutes through PySpark and dbt on Google Cloud with Apache Airflow orchestration. My Movie Analytics platform runs a Bronze to Silver to Gold medallion architecture on BigQuery with Cloud Scheduler automation, and my Hadoop cluster on Docker Swarm shows I can also engineer on premise style distributed systems, which is a good fit for a Data Fabric that connects cloud and on premise sources for a brewery.

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

* Built an end to end batch pipeline pulling movie data from a public API into a GCS data lake, processed through Bronze to Silver to Gold medallion architecture in BigQuery, fully automated on a Cloud Scheduler trigger with no manual steps.
* Engineered the Silver layer for trustworthy analytics with schema enforcement, safe type casting, deduplication via window functions, and genre normalisation into a relational model.
* Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage and keeping only pre release signals.
* Built Gold layer aggregates and a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing, plus an ML early warning view.
* Secured the system with a least privilege service account and Secret Manager and version controlled all code, SQL, and schemas in a reproducible GitHub repository.

**Hadoop Based Data Crawling and Processing Platform**: *Python, Selenium, BeautifulSoup, Pandas, Docker Swarm, Hadoop HDFS, SQL Server*

* Orchestrated a distributed Hadoop cluster with one Name Node and three Data Nodes on Docker Swarm, enabling automated container management and self healing across the cluster.
* Built a decoupled web scraping pipeline in Python with Selenium to navigate dynamic paginated e commerce results, saving raw HTML locally for data safety before downstream parsing.
* Engineered a robust BeautifulSoup parser handling missing data and decoding sponsored click tracking URLs into clean product links suitable for analytics.
* Ingested structured CSVs into HDFS, ran redundancy tests to verify replication across the three Data Nodes, and extracted processed data into SQL Server for downstream analysis.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical diabetes dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.