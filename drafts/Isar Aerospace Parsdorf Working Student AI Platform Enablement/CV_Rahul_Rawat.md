# Rahul Rawat

## Working Student, AI Platform and Enablement

Master's student in Data Science and Analytics at SRH Heidelberg, based in Mannheim, with hands on experience operating self hosted LLM inference, building agentic multi agent systems, and running fully automated cloud pipelines end to end. I run a multi agent RAG system entirely on self managed Ollama inference serving Mistral 7B and Qwen2.5 14B side by side with a hard coded check against silent fallback, and I built a Cloud Run batch pipeline that requires 0 manual intervention. Comfortable with Python, Docker, Linux, REST APIs, and hands on evaluation of open source models and developer tooling.

### Experience

**eRay GmbH**, Data Scientist, Oct 2025 to Mar 2026

* During a 6 month eRay GmbH and SRH Heidelberg collaboration to forecast lake water quality across 4 target indicators chlorophyll a, turbidity, pH and dissolved oxygen, built an end to end recursive time series pipeline over a 40 feature space with a per target lag suite lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h.
* Benchmarked 6 candidates Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints max_depth 4 and learning_rate 0.05, landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric 80 percent prediction intervals that hug the 0 floor and chop the top 15 percent of summer ghost spikes.
* Made the September evaluation defensible with a 3 pass outlier system pH tightened from 0 to 14 down to 7.0 to 9.0, Oct and Nov caps of 15.0 on chlorophyll a and 50.0 on turbidity, and a rolling z-score at z>2.5 over 48 hours, and excluded 5 sparse sensors plus 3 concurrent proxies phycocyanin_abs, phycocyanin_abs_comp and toc, surfacing the honest R squared of 0.86 on dissolved oxygen and 0.81 on pH.
* Reconstructed Oct and Nov gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all 6 lag features, generated a synthetic winter canvas with 4 degree Celsius floor and 0.4 degree diurnal amplitude, then wrapped it all in an orchestrator with gate checks, ecological clips dissolved oxygen 4.0 to 18.0 and pH 6.0 to 9.0 and a 0.003 pH per hour velocity clamp.
