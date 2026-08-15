# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, focused on LLMs, agent frameworks, and rapid prototyping of KI ideas. I shipped a modular RAG orchestrator on Llama 3.1 with LangChain, an intent classification router, ChromaDB, and MiniLM embeddings, plus a CreditIQ decision support tool and a Random Forest driven Economic Impact study. I enjoy testing new tools such as LangChain, AutoGen, and CrewAI hands on and translating findings into small demonstrators that non technical stakeholders can actually try.

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

* Designed a modular Retrieval Augmented Generation system using Llama 3.1 8b via Groq for high speed inference and LangChain for orchestration across multiple execution paths, a working example of the LangChain, AutoGen, and CrewAI style tooling Geiger evaluates.
* Engineered a custom decision making router that dynamically classifies user intent into three execution paths, local knowledge retrieval on PDF and vector stores, external web search through DuckDuckGo, and direct conversational logic, a lightweight agent coordinator.
* Implemented ChromaDB with local persistence for document storage, using HuggingFace MiniLM L6 v2 for semantic embeddings, ready to plug into new open source frameworks with minimal glue code.
* Built a stateful MemoryAgent that maintains conversational context across multiple turns and integrated it directly into the inference pipeline, exactly the kind of prototype and demonstrator Geiger wants students to build.
* Shipped the whole system behind a Streamlit interface as a deployed end to end tool, owning the design, implementation, and rollout in full.

**CreditIQ, Fairness by Design Credit Scoring System**: *Python, scikit learn, AIF360, SHAP, Streamlit*

* Lifted the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold, and translating a technical trade off into a business defensible position.
* Diagnosed a hidden intersectional bias where younger women were still being penalised even after single axis age bias was fixed, using SHAP, then designed a four way age by gender threshold matrix to correct it.
* Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness accuracy trade off as a deliberate and regulator defensible decision.
* Shipped a Streamlit decision support tool with LLM generated explanations for finance managers, a clear example of turning KI findings into an accessible internal tool.
* Backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up covering the EU AI Act Annex III and GDPR.

**Movie Analytics and ML Pipeline, Cloud Native Data Platform**: *GCP BigQuery, Cloud Run, GCS, Cloud Scheduler, BigQuery ML, Python, SQL, Looker Studio*

* Built an end to end batch pipeline pulling movie data from a public API into a GCS data lake, processed through Bronze to Silver to Gold medallion architecture in BigQuery, fully automated on a Cloud Scheduler trigger with no manual steps.
* Engineered the Silver layer for trustworthy analytics with schema enforcement, safe type casting, deduplication via window functions, and normalisation into a relational model.
* Trained a BigQuery ML classifier to predict whether a film will be a hit before release, deliberately splitting features into two tables to prevent data leakage and keeping only pre release signals.
* Built Gold layer aggregates and a five page Looker Studio dashboard answering concrete business questions on genre ROI, foreign language growth, and release season timing, plus an ML early warning view, and secured the system with a least privilege service account and Secret Manager.

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
