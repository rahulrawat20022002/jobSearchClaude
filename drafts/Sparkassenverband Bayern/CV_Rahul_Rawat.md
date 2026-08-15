# Rahul Rawat
**Data Analyst**

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile
Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, focused on regulator defensible data analysis, fairness aware machine learning, and clean data storytelling. I have shipped CreditIQ, a fairness by design credit scoring system that clears the EU AI Act 80 percent threshold, a BigQuery medallion pipeline with a five page Looker Studio dashboard, and an interactive Tableau meal simulator. I am well suited to strengthen the audit and Wirtschaftsprüfung function at Sparkassenverband Bayern in München.

## Experience
**eRay GmbH**  
*Data Scientist, Oct 2025 to Mar 2026*
- Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
- Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
- Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
- Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction on a limited prediction horizon.
- Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.

## Education
**M.Sc. Data Science and Analytics**, SRH University of Applied Sciences Heidelberg. Apr 2025 to Present.
**Bachelor of Technology in Computer Science**, GL Bajaj Institute of Technology and Management. 2019 to 2023.

## Personal Projects
**CreditIQ, Fairness by Design Credit Scoring System**: Python, scikit learn, AIF360, SHAP, Streamlit
- Lifted the model Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold.
- Diagnosed a hidden intersectional bias where younger women were penalised even after age bias was fixed, using SHAP, then designed a four way age by gender threshold matrix to correct it without over correcting into reverse discrimination.
- Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness accuracy trade off as a deliberate and regulator defensible decision.
- Shipped a Streamlit decision support tool that gives finance managers a recommendation plus a plain language LLM generated explanation, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14.
- Backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up covering EU AI Act Annex III, GDPR, a model card, and attack vectors.

**Movie Analytics and ML Pipeline, Cloud Native Data Platform**: GCP BigQuery, Cloud Run, GCS, Cloud Scheduler, BigQuery ML, Python, SQL, Looker Studio
- Built an end to end batch pipeline pulling data from a public API into a GCS data lake, processed through Bronze to Silver to Gold medallion architecture in BigQuery, fully automated on a Cloud Scheduler trigger with no manual steps.
- Engineered the Silver layer for trustworthy analytics with schema enforcement, safe type casting, deduplication via window functions, and normalisation into a relational model.
- Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage and keeping only pre release signals.
- Built Gold layer aggregates and a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing, plus an ML early warning view.
- Secured the system with a least privilege service account and Secret Manager and version controlled all code, SQL, and schemas in a reproducible GitHub repository.

**Fast Food Nutritional Analyzer and Meal Simulator**: Tableau with Set Actions Dashboard Actions parameters and calculated fields, data storytelling, UI and UX
- Built a dynamic shopping cart using Tableau Set Actions, letting users select scatter plot points to instantly total calories, fat, and protein for a simulated meal.
- Implemented parameter driven analytics with a dynamic Y axis via a CASE statement tied to a user controlled goal parameter for muscle gain versus weight loss.
- Authored complex order of operation IF THEN calculated fields for logical grouping and custom flags such as Is It A Trap for deceptive high fat and high calorie items.
- Designed a two tier layout with an executive macro view and a granular food finder, using a colour blind safe dark mode palette to reduce time to insight.

## Research and Thesis
**Bachelor Thesis, Diabetes Prediction Using Machine Learning** at GL Bajaj Institute of Technology and Management, IEEE style paper.
- Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
- Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
- Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
- Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications
- SAS Certified Specialist, Visual Business Analytics Using SAS Viya: issued May 2025.
- NVIDIA, Building LLM Applications With Prompt Engineering: issued November 2025.

## Achievements
- USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges.

## Languages
**English:** fluent, professional working proficiency. **German:** B1, in progress.