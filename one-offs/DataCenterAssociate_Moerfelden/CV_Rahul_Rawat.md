# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Structured and hands on Data Science and Analytics Master student at SRH Heidelberg, based in Mannheim, with practical experience running end to end data and IT systems that value order, documentation, and clean handover. I have delivered a six month industry collaboration with eRay GmbH, shipped a real time data pipeline on Google Cloud with orchestration and monitoring, and worked with cloud infrastructure, IT tooling, and inventory style tracking systems. Reliable, detail oriented, team oriented, and comfortable in physical and technical environments, I am motivated to contribute to reliable data centre operations and continuous process improvement at Moerfelden-Walldorf.

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

**Real Time Flight Tracking Data Pipeline**: *Python, PySpark, BigQuery, dbt, Apache Airflow, GCP with Dataproc GCE GCS, Tableau, TabPy, OAuth2*

* Set up real time data collection from the OpenSky Network API, polling live flight positions every 30 seconds and enriching each against airport, aircraft, and weather data across four upstream sources.
* Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft's nearest airport along the way for downstream joins.
* Orchestrated the whole system with Apache Airflow so batch and real time layers refresh automatically every 15 minutes with alerting on failure.
* Surfaced findings in Tableau with Python statistics via TabPy, showing that air traffic dropped 4.4 times in heavy rain and clustered around hubs like Frankfurt and Munich.

**Hadoop Based Data Crawling and Processing Platform**: *Python with Selenium BeautifulSoup and Pandas, Docker Swarm, Hadoop HDFS, SQL Server*

* Orchestrated a distributed Hadoop cluster with one Name Node and three Data Nodes on Docker Swarm, enabling automated container management and self healing.
* Built a decoupled web scraping pipeline in Python with Selenium to navigate dynamic paginated e commerce results, saving raw HTML locally for data safety.
* Engineered a robust BeautifulSoup parser handling missing data and decoding sponsored click tracking URLs into clean product links.
* Ingested structured CSVs into HDFS, ran redundancy tests to verify replication across the three Data Nodes, and extracted processed data into SQL Server for downstream analysis.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications

* AWS Academy Graduate, AWS Academy Cloud Foundations: issued July 2025.
* Google Data Analytics, Foundations, Data, Data, Everywhere: issued April 2025 on Coursera.

## Achievements

* USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
