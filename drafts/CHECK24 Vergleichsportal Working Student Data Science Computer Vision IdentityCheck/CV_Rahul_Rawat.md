# Rahul Rawat

## Working Student, Data Science and Computer Vision

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning benchmarking, honest evaluation on imbalanced datasets, and end to end ML delivery on real data. I have shipped a fairness by design classification system with SHAP driven subgroup analysis, unit tests at 100 percent branch coverage, and rigorous EU AI Act aligned evaluation, a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain, and a bachelor thesis benchmarking six classifiers on a real clinical dataset with 10 fold cross validation and ROC AUC as the honest headline metric for an imbalanced target. Proficient in Python, scikit learn, and standard ML frameworks, I am the right fit for a Working Student position on Data Science and Computer Vision in the IdentityCheck team at CHECK24.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
