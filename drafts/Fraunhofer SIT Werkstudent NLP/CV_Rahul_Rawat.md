# Rahul Rawat

## NLP and Machine Learning Werkstudent

Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on Natural Language Processing and machine learning work built around LLMs, embeddings, and rigorous evaluation. I have shipped a modular Retrieval Augmented Generation system with a custom decision making router on Llama 3.1 8b via Groq and LangChain with HuggingFace MiniLM L6 v2 embeddings, a fairness by design classification pipeline validated to EU AI Act thresholds, and a recursive time series pipeline at eRay GmbH with strict anti leakage rules. Comfortable in Python, PyTorch style workflows, Transformer architectures, and web interface development with Streamlit, I am the right fit for supporting your NLP research on authorship, style change detection, and AI generated text.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
