# Rahul Rawat

rahulrawat2r@gmail.com  •  015563603340  •  linkedin.com/in/rahulrawat2r  •  github.com/rahulrawat20022002  •  Mannheim, Germany

## Profile

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, focused on defensible ML systems, regulatory review, and applied KI use cases. My CreditIQ project lifted a credit scoring model's Disparate Impact ratio from 0.79 to 0.88 under the EU AI Act and AGG threshold, and my Hybrid RAG Orchestrator on Llama 3.1 with LangChain and ChromaDB combines retrieval and prompt engineering into a working audit style assistant, both directly supporting Internal Audit's push to identify and prototype KI use cases responsibly.

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
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream, the same discipline needed for audit ready KI systems.

## Personal Projects

**CreditIQ, Fairness by Design Credit Scoring System**: *Python, scikit learn, AIF360, SHAP, Streamlit*

* Lifted the model's Disparate Impact ratio from a failing 0.79 to a compliant 0.88, clearing the EU AI Act and AGG 80 percent fairness threshold, a full case study in defensible ML for regulated audit environments.
* Diagnosed a hidden intersectional bias where younger women were still being penalised even after single axis age bias was fixed, using SHAP for explainability, then designed a four way age by gender threshold matrix to correct it without over correcting into reverse discrimination.
* Cut the false negative rate from 44 percent to 16.7 percent while holding accuracy at 75 percent, and shipped a Streamlit decision support tool with an LLM generated explanation, keeping a human in the loop per GDPR Article 22 and EU AI Act Article 14.
* Backed the pipeline with unit tests at 100 percent branch coverage and a full regulatory write up covering EU AI Act Annex III, GDPR, a model card, and attack vectors, exactly the artefact set an internal audit function needs.

**Hybrid RAG Orchestrator**: *Python, LangChain, Llama 3.1 8b on Groq, ChromaDB, HuggingFace MiniLM L6 v2, Streamlit*

* Designed a modular Retrieval Augmented Generation system using Llama 3.1 8b via Groq for high speed inference and LangChain for orchestration across multiple execution paths, a working prototype for an audit assistant that can search policy documents and generate structured findings.
* Engineered a custom decision making router that dynamically classifies user intent into three execution paths, local knowledge retrieval on PDF and vector stores, external web search through DuckDuckGo, and direct conversational logic.
* Implemented ChromaDB with local persistence for document storage using HuggingFace MiniLM L6 v2 embeddings, and built a stateful MemoryAgent that iteratively tested prompts for accuracy and reliability, the same prompt engineering discipline the Internal Audit brief calls for.
* Shipped the whole system behind a Streamlit interface as a deployed end to end tool, owning the design, implementation, and rollout in full.

**Economic Impact Analysis of Global Climate Events**: *Python with Pandas and scikit learn, Random Forest, statistical modelling, Matplotlib and Seaborn*

* Executed an end to end data science project transforming raw global event datasets into structured insights for resource allocation and risk assessment, with data preparation across outliers, imputation, and normalisation, the kind of Excel and Python work an Internal Audit team needs before drawing conclusions.
* Developed Random Forest models to analyse correlations between event duration and financial impact, and communicated the findings to non technical stakeholders through comprehensive visual reports, mirroring the interne Aufbereitung und Präsentation von Ergebnissen requirement.

## Research and Thesis

**Bachelor Thesis, Diabetes Prediction Using Machine Learning**
*GL Bajaj Institute of Technology and Management, IEEE style paper*

* Built a full end to end machine learning pipeline comparing six classifiers on a clinical dataset of 768 patients, using 10 fold cross validation and per model confusion matrices.
* Caught biologically impossible zero values that the original authors had overlooked, then applied IQR based outlier removal and proper imputation to restore data integrity.
* Chose ROC AUC over accuracy as the headline metric for a 65 to 35 imbalanced dataset, avoiding a misleadingly rosy accuracy figure that would have hidden real error patterns.
* Wrote up findings as an IEEE style paper including an honest section on limitations and what to do differently in a follow up study.

## Certifications

* NVIDIA: Building LLM Applications With Prompt Engineering, issued November 2025.
* SAS Certified Specialist: Visual Business Analytics Using SAS Viya, issued May 2025.
* Google Data Analytics: Foundations, Data, Data, Everywhere, issued April 2025 on Coursera.

## Achievements

* USAII Global AI Hackathon 2026: Finalist at Graduate Level, event 14 to 21 June 2026, awarded by the United States Artificial Intelligence Institute for innovation, technical creativity, and applied AI on real world challenges. Hackathon ID 830382652.

## Languages

English: fluent, professional working proficiency. German: B1, in progress.
