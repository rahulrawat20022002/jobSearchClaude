# Rahul Rawat

Mannheim, Germany | rahulrawat2r@gmail.com | 015563603340 | linkedin.com/in/rahulrawat2r | github.com/rahulrawat20022002

## Profile

Data Science Master's student at SRH Heidelberg with direct experience building and operating data pipelines, including a distributed web scraping platform on Hadoop and Docker Swarm and a real time cloud pipeline orchestrated with Apache Airflow. Comfortable in Python, SQL, and Git based collaborative workflows, with a track record of handling messy, paginated, real world sources and turning them into clean, reliable datasets. Used to working independently on a defined slice of a larger codebase while documenting findings for colleagues outside the team. Looking to bring that data engineering foundation to nexmart's Data Platform team.

## Education

**M.Sc. Data Science and Analytics**  Apr 2025 to Present
*SRH University of Applied Sciences Heidelberg*

**Bachelor's Degree in Computer Science**  2019 to 2023
*GL Bajaj Institute of Technology and Management*

## Experience

**eRay GmbH**  Oct 2025 to Mar 2026
*Data Scientist*

* Built a complete recursive forecasting pipeline covering four water quality indicators for a German lake: chlorophyll a, turbidity, pH, and dissolved oxygen, across a six month academic and industry collaboration.
* Benchmarked six models head to head, including Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, then used CatBoost multi quantile regression to deliver asymmetric 80 percent prediction intervals.
* Enforced strict rules against data leakage, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not predictable without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast curve to stop tree models flatlining during recursive prediction.
* Wrapped the pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade.

## Personal Projects

**Hadoop based Data Crawling and Processing Platform**: Python, Selenium, BeautifulSoup, Pandas, Docker Swarm, Hadoop HDFS, SQL Server
* Orchestrated a distributed Hadoop cluster with one name node and three data nodes using Docker Swarm, enabling automated container management and self healing.
* Built a decoupled web scraping pipeline in Python with Selenium to navigate dynamic, paginated e commerce results, saving raw HTML locally for data safety.
* Engineered a robust BeautifulSoup parser that handles missing data and decodes sponsored click tracking URLs into clean product links.
* Ingested structured CSVs into HDFS, ran redundancy tests to verify replication across all three data nodes, then extracted processed data into SQL Server for downstream analysis.

**Real Time Flight Tracking Data Pipeline**: Python, PySpark, BigQuery, dbt, Apache Airflow, Google Cloud Platform, Tableau
* Set up real time data collection from the OpenSky Network API, polling live flight positions every 30 seconds and enriching each one against airport, aircraft, and weather data from four separate sources.
* Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft's nearest airport along the way.
* Orchestrated the whole system with Apache Airflow so the batch and real time layers refresh automatically every 15 minutes.
* Surfaced findings in Tableau using Python statistics through TabPy, showing that air traffic dropped 4.4 times over in heavy rain and clustered around hubs like Frankfurt and Munich.

**Movie Analytics and ML Pipeline, a Cloud Native Data Platform**: Google Cloud Platform, BigQuery, Cloud Run, Cloud Scheduler, Python, SQL, Looker Studio
* Built a complete batch pipeline that pulls movie data from a public API into a GCS data lake, processes it through Bronze to Silver to Gold medallion architecture in BigQuery, and runs fully automated on a Cloud Scheduler trigger with no manual steps.
* Engineered the Silver layer for trustworthy analytics, covering schema enforcement, safe type casting, deduplication through window functions, and genre normalization into a relational model.
* Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage by using only pre release signals.
* Secured the system with a least privilege service account and Secret Manager, and version controlled all code, SQL, and schemas in a reproducible GitHub repo.

## Research and Thesis

**Bachelor Thesis: Diabetes Prediction Using Machine Learning**
*Python, Scikit Learn, Pandas, Seaborn, Google Colab. Written up as an IEEE style paper.*

* Built a complete machine learning pipeline comparing six classifiers on a clinical dataset of 768 patient records, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values the original authors had overlooked, then applied IQR based outlier removal and proper imputation.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure.
* Wrote up findings as an IEEE style paper, including an honest section on limitations and what to do differently.

## Languages

**English:** fluent, professional working proficiency  
**German:** A2.2, completed through VHS  
