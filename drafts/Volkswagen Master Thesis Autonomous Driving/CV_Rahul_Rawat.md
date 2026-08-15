# Rahul Rawat

## Master Thesis Student

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on deep learning and generative AI work on real production data. I have shipped a Retrieval Augmented Generation system with agentic routing on Llama 3.1 8b via Groq, a fairness by design credit scoring system covering EU AI Act and GDPR, and a recursive time series forecasting pipeline at eRay GmbH built on CatBoost multi quantile regression with anti leakage guarantees. Comfortable in Python, PyTorch style workflows, and scientific evaluation, I am the right fit for a Master Thesis on generating anomalous traffic scenarios and evaluating generated data for autonomous driving.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
