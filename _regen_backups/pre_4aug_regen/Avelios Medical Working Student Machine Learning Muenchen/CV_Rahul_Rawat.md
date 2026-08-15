# Rahul Rawat

## Working Student, Machine Learning

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on machine learning integration into real clinical and operational data, honest evaluation on imbalanced datasets, and end to end delivery of intelligent systems. I have shipped a bachelor thesis comparing six classifiers on a real clinical dataset with 10 fold cross validation, catching biologically impossible values and choosing ROC AUC over accuracy on an imbalanced target, an end to end recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage rules, and a fairness by design classification system with SHAP driven subgroup analysis and 100 percent branch coverage unit tests. Proficient in Python, scikit learn, and modern ML frameworks, I am the right fit for a Working Student Machine Learning position supporting Avelios' mission to unlock clinical data for better patient care.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
