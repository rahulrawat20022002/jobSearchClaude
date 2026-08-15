# Rahul Rawat

## Mandatory Intern, Data Science and Deep Learning for Energy Systems

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on time series forecasting, deep learning, and cloud data pipeline work on real sensor data. I have shipped a recursive time series pipeline at eRay GmbH forecasting four water quality indicators for a German lake using CatBoost multi quantile regression with asymmetric 80 percent prediction intervals, a real time Google Cloud pipeline processing over 128 thousand flight records enriched against four data sources every 30 seconds, and a fairness by design classification system with rigorous evaluation and unit tests at 100 percent branch coverage. Proficient in Python and deep learning frameworks, comfortable with anti leakage evaluation, I am the right fit for a Mandatory Internship on Data Science and Deep Learning for Energy Systems at Siemens.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
