# Rahul Rawat

## AI Working Student

Master student in Data Science and Analytics at SRH Heidelberg based in Mannheim with hands on delivery of generative AI, large language model applications, and computer vision leaning pipelines. I built a Hybrid RAG Orchestrator with agentic routing over Llama 3.1 8b via Groq and LangChain, delivered a fairness by design credit scoring system under the EU AI Act, and ran an end to end recursive time series pipeline at eRay GmbH with strict anti leakage rules. Confident in Python, LangChain, ChromaDB, HuggingFace embeddings, scikit learn, and data scraping with Selenium and BeautifulSoup.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* Built an end to end recursive time series pipeline forecasting chlorophyll a, turbidity, pH, and dissolved oxygen for a German lake, delivered as a six month collaboration with SRH University Heidelberg.
* Benchmarked six models head to head, Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost, and Prophet, and used CatBoost multi quantile regression to produce asymmetric 80 percent prediction intervals for decision support under uncertainty.
* Enforced strict anti leakage rules across the pipeline, surfacing the honest finding that pH and dissolved oxygen are physically predictable while chlorophyll a and turbidity are not without live optical sensors.
* Reconstructed missing winter readings with MICE imputation and engineered a synthetic winter decay forecast canvas so tree based models stopped flatlining during recursive prediction.
* Wrapped the whole pipeline in an orchestrator with gate checks and velocity and ecological bounds that halts on failed imputation rather than letting bad data cascade downstream.
