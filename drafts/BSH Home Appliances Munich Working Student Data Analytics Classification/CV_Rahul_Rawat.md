# Rahul Rawat
Working Student: Engineering Data Analytics and Classification

---

## PERSONAL DETAILS

| | |
|---|---|
| **Address** | C2 16, 68159 Mannheim, Germany |
| **Phone** | 015563603340 |
| **Email** | rahulrawat2r@gmail.com |
| **LinkedIn** | linkedin.com/in/rahulrawat2r |
| **GitHub** | github.com/rahulrawat20022002 |
| **Portfolio** | rah-portfolio.pages.dev |
| **Date of birth** | 20 February 2002 |
| **Nationality** | Indian, student visa with valid work permit |
| **Availability** | Werkstudent 20 hours per week immediately, full time from April 2027 |

---

## PROFILE

M.Sc. Data Science and Analytics student at SRH University of Applied Sciences Heidelberg with practical experience in classification modelling, data analytics pipelines, and BI dashboarding on real-world datasets. At eRay GmbH I built and validated a recursive forecasting pipeline for sensor data covering four quality indicators. Separate projects cover a fully automated cloud data platform processing over 128 thousand records through a medallion architecture on BigQuery, and a six-classifier comparison study for diabetes prediction using leakage-aware evaluation. Available 20 hours per week on site in Munich, eager to contribute data analytics and classification expertise to BSH Home Appliances.

---

## SKILLS

Python, SQL, PySpark, BigQuery, dbt, Apache Airflow, GCP, Dataproc, GCS, Cloud Run, Cloud Scheduler, AWS, scikit-learn, CatBoost, LightGBM, XGBoost, Random Forest, Prophet, MICE, SHAP, SAS Viya, Tableau, Looker Studio, Power BI, TabPy, Pandas, NumPy, Matplotlib, Seaborn, Docker, Git

---

## PROFESSIONAL EXPERIENCE

**Data Scientist at eRay GmbH, Heidelberg, Oct 2025 to Mar 2026**
*6-month collaboration with SRH University of Applied Sciences Heidelberg*

- During a 6 month collaboration between eRay GmbH and SRH Heidelberg to forecast lake water quality across **4** target indicators, tasked with designing the end to end recursive time series infrastructure over a **40** feature space; built a per target lag suite and a production ready orchestrator with ecological validity checks; the system processes all targets in under **6** hours per forecast cycle.
- With **6** candidate models performing inconsistently on summer ghost spikes, tasked with selecting the most defensible model; benchmarked Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints; landed on CatBoost MultiQuantile producing asymmetric **80 percent** prediction intervals that chop the top **15 percent** of summer ghost spikes.
- With sparse sensors and concurrent proxies contaminating the evaluation, tasked with making the R squared defensible; implemented a 3 pass outlier and validation system, excluded **5** sparse sensors and **3** concurrent proxies; surfaced the honest R squared of **0.86** on dissolved oxygen and **0.81** on pH.
- With Oct and Nov gaps threatening model integrity, tasked with data reconstruction; applied IterativeImputer MICE, ran Memory Buffer recalculation across all **6** lag features, and generated a synthetic winter canvas; delivered a gapless 40 feature input for the recursive forecasting step.

**Junior Associate Software Developer at SS Engineers and Contractors, India, Aug 2023 to Aug 2024**

- With SS Engineers and Contractors running internal Data Dashboards, Analytics platforms, and Employee Portals, tasked with building the front end features the teams depended on; contributed React UI components across all three products, which stayed in daily use throughout the year.
- With a client migration from AngularJS to React required inside an existing module federation setup, tasked with porting across without breaking the running product; ported around **8** routes over **4** months; shipped with no production incidents during rollout.

**Front End Developer Intern at SS Engineers and Contractors, India, Feb 2023 to July 2023**

- During a 6 month internship, tasked with delivering UI components for internal dashboards under senior review; shipped charts, filters, and profile pages on code review feedback; all contributed code remained in production through the end of the internship.

---

## EDUCATION

**M.Sc. Data Science and Analytics, Apr 2025 to Present**
SRH University of Applied Sciences Heidelberg, GPA 1.9

**Bachelor of Technology in Computer Science, 2019 to 2023**
GL Bajaj Institute of Technology and Management, CGPA 7.3 of 10

---

## PERSONAL PROJECTS

### Real-Time Flight Tracking Data Pipeline
*Built with: Python, PySpark, BigQuery, dbt, Apache Airflow, GCP (Dataproc, GCE, GCS), Tableau, TabPy, OAuth2*

- For a Data Engineering module at SRH needing a real time joined view over live aircraft above Germany, tasked with the collection and enrichment layer; built Python collectors polling the OpenSky Network API every **30 seconds** and PySpark cleaning on GCP joining against **4** sources; produced a clean joined table covering more than **128 thousand** records.
- With the pipeline needing automated refresh, tasked with orchestration; shaped data into analysis-ready tables with dbt, computed nearest airport labels with PySpark, and orchestrated the full system with Apache Airflow so batch and real time layers refresh every **15 minutes** without operator intervention.
- With stakeholders needing insight rather than raw tables, tasked with the analytics surface; built a Tableau workbook via TabPy surfacing the finding that air traffic drops **4.4 times** in heavy rain and clusters around hubs like Frankfurt and Munich.

### Economic Impact Analysis of Global Climate Events
*Built with: Python (Pandas, scikit-learn), Matplotlib, Seaborn, Random Forest*

- For a data science project turning raw global climate event data into decision support for resource allocation, tasked with the full analytics pipeline; executed end to end from raw CSV ingestion to a management ready output as a single reproducible pipeline.
- With outliers, missing values, and inconsistent scales in the raw data, tasked with building a clean foundation; performed advanced data preparation with outlier removal, imputation, and normalisation; model performance remained stable before and after feature scaling.
- With non-technical stakeholders as the target audience, tasked with communicating results clearly; developed Random Forest models analysed through feature importance rankings and residual analysis, produced visual reports with calibrated confidence statements that survived a management review without further translation.

---

## RESEARCH AND THESIS

### Bachelor Thesis: Diabetes Prediction Using Machine Learning
*Built with: Python, scikit-learn, Pandas, Seaborn, Google Colab*

- For a Bachelor thesis on diabetes prediction with a clinical dataset of **768** patients, tasked with a defensible classifier comparison; built a full end to end pipeline comparing **6** classifiers with **10 fold** cross validation and per model confusion matrices; delivered a model comparison that stood up in the thesis defence.
- Spotting biologically impossible zero values in the source data, tasked with restoring data integrity before any model fit; applied IQR based outlier removal and proper imputation; lifted the dataset to a clean training input for every downstream model.
- With a **65 to 35** class imbalance making accuracy misleading, tasked with choosing the right evaluation metric; moved the headline metric to ROC AUC; produced an IEEE style paper with an honest limitations section that the supervisor accepted as publishable in substance.

---

## CERTIFICATIONS

**SAS Certified Specialist: Visual Business Analytics Using SAS Viya** — Issued 7 May 2025
**Google Data Analytics: Foundations: Data, Data, Everywhere** — Issued 7 April 2025
**AWS Academy Graduate: AWS Academy Cloud Foundations** — Issued 15 July 2025

---

## ACHIEVEMENTS

**USAII Global AI Hackathon 2026, Finalist at Graduate Level** — Awarded by the United States Artificial Intelligence Institute for advancing to the Final Round through innovation, technical creativity, and applied AI on real world challenges.

---

## LANGUAGES

| Language | Level |
|---|---|
| English | Fluent, written and spoken |
| German | B1 in progress toward B2 |
| Hindi | Native |
