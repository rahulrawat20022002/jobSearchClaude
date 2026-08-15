# Rahul Rawat
**Master Thesis Student**

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile
Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, looking for a Master Thesis at the intersection of applied computer vision and real time telemetry. My hybrid RAG orchestrator on Llama 3.1, my real time flight tracking pipeline, and my fairness by design CreditIQ system together show that I can design modular AI systems, integrate high frequency sensor streams, and evaluate models honestly. I am well suited to a Master Thesis on computer vision for motorsport video analysis at TOYOTA GAZOO Racing Europe in Köln.

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
**Hybrid RAG Orchestrator**: Python, LangChain, Llama 3.1 8b via Groq, ChromaDB, HuggingFace MiniLM L6 v2, Streamlit
- Designed a modular retrieval augmented generation system using Llama 3.1 8b via Groq for high speed inference and LangChain for orchestration across intent routing and answer synthesis.
- Engineered a custom decision making router that dynamically classifies user intent into three execution paths, local knowledge retrieval over a PDF and vector store, external web search through DuckDuckGo, or direct conversational logic.
- Implemented ChromaDB with local persistence for document storage and HuggingFace MiniLM L6 v2 for semantic embeddings, giving the system a queryable long term knowledge base.
- Built a stateful memory agent that maintains conversational context across multiple turns, integrated directly into the inference pipeline so responses stay coherent across a session.
- Shipped the whole system behind a Streamlit interface with end to end ownership from architecture to deployment.

**Real Time Flight Tracking Data Pipeline**: Python, PySpark, BigQuery, dbt, Apache Airflow, GCP Dataproc GCE GCS, Tableau with TabPy, OAuth2
- Set up real time data collection from the OpenSky Network API, polling live flight positions every 30 seconds, enriching each against airport, aircraft, and weather data across four sources.
- Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft nearest airport along the way.
- Orchestrated the whole system with Apache Airflow so batch and real time layers refresh automatically every 15 minutes without manual intervention.
- Surfaced findings in Tableau with Python statistics through TabPy, showing that air traffic dropped 4.4 times in heavy rain and clustered around hubs such as Frankfurt and Munich.

**CreditIQ, Fairness by Design Credit Scoring System**: Python, scikit learn, AIF360, SHAP, Streamlit
- Lifted the model Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold.
- Diagnosed a hidden intersectional bias where younger women were penalised even after age bias was fixed, using SHAP, then designed a four way age by gender threshold matrix to correct it without over correcting into reverse discrimination.
- Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness accuracy trade off as a deliberate and regulator defensible decision.
- Shipped a Streamlit decision support tool that gives finance managers a recommendation plus a plain language LLM generated explanation, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14.
- Backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up covering EU AI Act Annex III, GDPR, a model card, and attack vectors.

## Research and Thesis
**Bachelor Thesis, Diabetes Prediction Using Machine Learning** at GL Bajaj Institute of Technology and Management, IEEE style paper.
- Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
- Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
- Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
- Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications
- NVIDIA, Building LLM Applications With Prompt Engineering: issued November 2025.
- AWS Academy Graduate, AWS Academy Cloud Foundations: issued July 2025.

## Achievements
- USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges.

## Languages
**English:** fluent, professional working proficiency. **German:** B1, in progress.