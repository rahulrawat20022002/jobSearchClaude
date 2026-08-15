# Rahul Rawat

## Master Thesis, AI Suitability Evaluation for Modelica Physical Models

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on evaluation of open weight and closed source large language models, honest benchmarking of alternative models on real data, and end to end machine learning delivery. I have shipped a modular Retrieval Augmented Generation system on Llama 3.1 8b via Groq with a custom decision making router, a fairness by design credit scoring system with SHAP driven subgroup analysis and full regulatory documentation, and a recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules. Proficient in Python and comfortable with LLM APIs, prompt engineering, and structured evaluation harnesses, I am the right fit for the Master Thesis on AI Suitability Evaluation for Modelica Physical Models at Airbus Hamburg.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
