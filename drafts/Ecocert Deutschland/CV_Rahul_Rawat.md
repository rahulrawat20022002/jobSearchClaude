# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, looking for a Masterarbeit topic on applied AI for digital innovation. I have shipped a modular Retrieval Augmented Generation system on Llama 3.1 with a routing agent, a fairness aware credit scoring system with a full EU AI Act and GDPR write up, and a Random Forest study translating raw event data into business relevant insight. Fluent in Python and comfortable with modern LLM and cloud tooling, I am ready to write a rigorous applied AI thesis with Ecocert.

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

**Hybrid RAG Orchestrator**: *Python, LangChain, Llama 3.1 8b via Groq, ChromaDB, HuggingFace MiniLM L6 v2, Streamlit*

* Designed a modular Retrieval Augmented Generation system using Llama 3.1 8b via Groq for high speed inference and LangChain for orchestration.
* Engineered a custom decision making router that dynamically classifies user intent into three execution paths, local knowledge retrieval from PDF and vector store, external web search via DuckDuckGo, or direct conversational logic.
* Implemented ChromaDB with local persistence for document storage, using HuggingFace MiniLM L6 v2 for semantic embeddings and a stateful memory agent that maintains conversational context across multiple turns.
* Shipped end to end behind a Streamlit interface with full ownership from prototype to deployed tool.

**CreditIQ, Fairness by Design Credit Scoring System**: *Python, scikit learn, AIF360, SHAP, Streamlit*

* Lifted the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold, an exercise in defensible modelling under EU regulation.
* Diagnosed a hidden intersectional bias where younger women were still being penalised even after single axis age bias was fixed, using SHAP, then designed a four way age by gender threshold matrix to correct it without over correcting into reverse discrimination.
* Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, documenting the fairness accuracy trade off as a deliberate and regulator defensible decision.
* Shipped a Streamlit decision support tool giving finance managers a recommendation plus a plain language LLM generated explanation, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14.
* Backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up covering EU AI Act Annex III, GDPR, a model card, and attack vectors.

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

* NVIDIA Building LLM Applications With Prompt Engineering: issued November 2025.
* Google Data Analytics, Foundations, Data, Data, Everywhere: issued April 2025 on Coursera.

## Achievements

* USAII Global AI Hackathon 2026: Finalist at Graduate Level, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
