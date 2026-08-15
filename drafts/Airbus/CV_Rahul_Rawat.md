# Rahul Rawat

Mannheim, Germany | rahulrawat2r@gmail.com | 015563603340 | linkedin.com/in/rahulrawat2r | github.com/rahulrawat20022002

## Profile

Data Science Master's student at SRH Heidelberg with a strong foundation in classical machine learning, statistical modeling, and rigorous, leakage aware evaluation. Experienced with the Python scientific stack, including Pandas and Scikit Learn, and with orchestration tools such as Apache Airflow, and comfortable translating messy real world data into validated, well documented models. Has shipped fairness audited and unit tested machine learning systems from end to end, with an emphasis on getting the methodology right rather than chasing the flashiest number. Excited to bring that scientific computing mindset to Airbus's Flight Physics Capabilities team.

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

**Economic Impact Analysis of Global Climate Events**: Python, Pandas, Scikit Learn, Matplotlib, Seaborn, Random Forest
* Executed a complete data science project transforming raw global event datasets into structured insights for resource allocation and risk assessment.
* Performed advanced data preparation and cleansing, including outlier handling, imputation, and normalization, to build a high quality data foundation before any modeling began.
* Developed Random Forest models to analyze correlations between disaster duration and financial impact, extracting clear, business relevant insights from noisy real world data.
* Communicated complex statistical findings to non technical stakeholders through comprehensive visual reports, translating model output into plain language.

**CreditIQ, a Fairness by Design Credit Scoring System**: Python, Scikit Learn, AIF360, SHAP, Streamlit
* Lifted the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold.
* Diagnosed a hidden intersectional bias, where younger women were penalized even after age bias was corrected, using SHAP, then designed a four way age by gender threshold matrix to fix it without over correcting into reverse discrimination.
* Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness versus accuracy trade off as a deliberate, defensible decision rather than an accident.
* Backed the pipeline with unit tests at 100 percent branch coverage and a full written regulatory review covering the EU AI Act, GDPR, a model card, and attack vectors.

**Real Time Flight Tracking Data Pipeline**: Python, PySpark, BigQuery, dbt, Apache Airflow, Google Cloud Platform, Tableau
* Set up real time data collection from the OpenSky Network API, polling live flight positions every 30 seconds and enriching each one against airport, aircraft, and weather data from four separate sources.
* Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft's nearest airport along the way.
* Orchestrated the whole system with Apache Airflow so the batch and real time layers refresh automatically every 15 minutes.
* Surfaced findings in Tableau using Python statistics through TabPy, showing that air traffic dropped 4.4 times over in heavy rain and clustered around hubs like Frankfurt and Munich.

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
