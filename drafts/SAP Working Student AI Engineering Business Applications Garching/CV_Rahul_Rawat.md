# Rahul Rawat

## Working Student, AI Engineering for Business Applications

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on large language model application building, prompt engineering, and cloud backend delivery. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq, LangChain orchestration, ChromaDB, and a stateful memory agent behind a Streamlit interface, a fairness by design credit scoring tool with a plain language LLM generated explanation for finance managers, and a fully automated Bronze to Silver to Gold BigQuery medallion pipeline with BigQuery ML classifier on Google Cloud. Proficient in Python, LangChain, LLM APIs, and cloud platforms, I am the right fit for a Working Student position on AI Engineering for Business Applications in the Cloud ERP Finance Product Services team at SAP.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* During a six month eRay GmbH and SRH Heidelberg collaboration to forecast water quality on a German lake, tasked with covering four indicators over rolling horizons, built an end to end recursive time series pipeline for chlorophyll a, turbidity, pH, and dissolved oxygen, delivered as a production ready module the client can rerun on every new sensor drop.
* Faced with model choice ambiguity for the forecasting task and the need to convey uncertainty to non technical stakeholders, benchmarked six candidates head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, then landed on CatBoost multi quantile regression, which produced asymmetric 80 percent prediction intervals that gave the client decision support under uncertainty.
* Concerned that naive time series splits would inflate accuracy, tasked with making the evaluation defensible, enforced strict anti leakage rules across the pipeline, which surfaced the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* With winter readings missing and tree based models flatlining during recursive prediction, needing realistic seasonal shape in the downstream forecasts, reconstructed missing values with MICE imputation and engineered a synthetic winter decay forecast canvas, which restored believable winter behaviour without introducing bias into the training window.
* To prevent bad data cascading downstream through the recursive forecaster, tasked with hardening the run loop, wrapped the pipeline in an orchestrator with gate checks and velocity and ecological bounds, so a failed imputation now halts the run rather than corrupting weeks of downstream predictions.
