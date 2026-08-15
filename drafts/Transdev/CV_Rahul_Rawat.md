# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on experience building and evaluating LLM based platforms end to end. I shipped a modular RAG orchestrator on Llama 3.1 with LangChain, ChromaDB, and a custom intent router that classifies user intent across local retrieval, external web search, and direct conversation. I have also designed an evaluation and bias detection framework in the CreditIQ project and a REST API driven cloud pipeline on GCP, which is the exact toolkit needed to help build and connect the internal KI platform at Transdev.

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

**Hybrid RAG Orchestrator**: *Python, LangChain, Llama 3.1 8b on Groq, ChromaDB, HuggingFace MiniLM L6 v2, Streamlit*

* Designed a modular Retrieval Augmented Generation system using Llama 3.1 8b via Groq for high speed inference and LangChain for orchestration across multiple execution paths, the same architecture Transdev needs for its internal KI platform.
* Engineered a custom decision making router that dynamically classifies user intent into three execution paths, local knowledge retrieval on PDF and vector stores, external web search through DuckDuckGo, and direct conversational logic, ready to plug into new drittsysteme.
* Implemented ChromaDB with local persistence for document storage, using HuggingFace MiniLM L6 v2 for semantic embeddings tuned for retrieval quality across heterogeneous internal documents.
* Built a stateful MemoryAgent that maintains conversational context across multiple turns and integrated it directly into the inference pipeline, plus prompt evaluation and quality testing on performance, accuracy, and usability.
* Shipped the whole system behind a Streamlit interface as a deployed end to end tool, owning the design, implementation, and rollout in full.

**CreditIQ, Fairness by Design Credit Scoring System**: *Python, scikit learn, AIF360, SHAP, Streamlit*

* Designed and defended a full evaluation framework for a real ML system, exactly the discipline needed for Qualitätsanalysen of KI Anwendungen at Transdev.
* Lifted the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold.
* Diagnosed a hidden intersectional bias against younger women using SHAP, then designed a four way age by gender threshold matrix to correct it without over correcting into reverse discrimination.
* Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness accuracy trade off as a deliberate and regulator defensible decision.
* Shipped a Streamlit decision support tool with a human in the loop LLM generated explanation, backed by unit tests at 100 percent branch coverage and a full regulatory write up covering EU AI Act Annex III, GDPR, a model card, and attack vectors.

**Real Time Flight Tracking Data Pipeline**: *Python, PySpark, BigQuery, dbt, Apache Airflow, GCP with Dataproc and GCE and GCS, Tableau, TabPy, OAuth2*

* Set up real time data collection from the OpenSky Network REST API, polling live flight positions every 30 seconds and enriching each against airport, aircraft, and weather data across four sources.
* Cleaned raw data with PySpark on Google Cloud and shaped it into analysis ready tables with dbt, computing each aircraft's nearest airport along the way.
* Orchestrated the whole system with Apache Airflow so batch and real time layers refresh automatically every 15 minutes, showing the same containerised cloud approach a KI platform anbindung needs.
* Surfaced findings in Tableau with Python statistics via TabPy, including that air traffic dropped 4.4 times in heavy rain and clustered around hubs like Frankfurt and Munich.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications

* NVIDIA: Building LLM Applications With Prompt Engineering, issued November 2025.
* AWS Academy Graduate: AWS Academy Cloud Foundations, issued July 2025.

## Achievements

* USAII Global AI Hackathon 2026: Finalist at Graduate Level, event 14 to 21 June 2026, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges. Hackathon ID 830382652.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
