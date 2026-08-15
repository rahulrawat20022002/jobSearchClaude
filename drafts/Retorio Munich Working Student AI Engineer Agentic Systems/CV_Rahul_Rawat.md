# Rahul Rawat
Working Student: AI Engineer, Agentic Systems

---

## PERSONAL DETAILS

| | |
|---|---|
| **Address** | C2 16, 68159 Mannheim, Germany |
| **Phone** | 015563603340 |
| **Email** | rahulrawat2r@gmail.com |
| **LinkedIn** | linkedin.com/in/rahulrawat2r |
| **GitHub** | github.com/rahulrawat20022002 |
| **Portfolio** | rah-portfolio.pages.dev |
| **Date of birth** | 20 February 2002 |
| **Nationality** | Indian, student visa with valid work permit |
| **Availability** | Werkstudent 20 hours per week immediately, full time from April 2027 |

---

## PROFILE

M.Sc. Data Science and Analytics student at SRH University of Applied Sciences Heidelberg with production experience building multi-agent AI systems, RAG pipelines, and data science infrastructure. At eRay GmbH I designed and shipped an end to end recursive forecasting pipeline covering four environmental indicators. Personal projects include a fully local multi-agent RAG system with an LLM as Judge evaluation harness and a fairness-by-design credit scoring tool audited against EU AI Act requirements. Excited to apply agentic AI and LangGraph orchestration skills in a product team where real users interact with the system every day.

---

## SKILLS

Python, LangChain, LangGraph, Ollama, Pinecone, BM25, dense vector retrieval, paraphrase-multilingual-MiniLM, spaCy, scikit-learn, CatBoost, LightGBM, XGBoost, Prophet, MICE, SHAP, AIF360, Streamlit, SQL, PySpark, BigQuery, dbt, Apache Airflow, GCP, AWS, Docker, Git, React, Playwright, Pandas, NumPy, Matplotlib

---

## PROFESSIONAL EXPERIENCE

**Data Scientist at eRay GmbH, Heidelberg, Oct 2025 to Mar 2026**
*6-month collaboration with SRH University of Applied Sciences Heidelberg*

- During a 6 month collaboration between eRay GmbH and SRH Heidelberg to forecast lake water quality across **4** target indicators, tasked with designing the end to end recursive time series infrastructure over a **40** feature space; built a per target lag suite covering lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h; delivered a production ready orchestrator with gate checks and ecological clips processing all targets in under **6** hours per forecast cycle.
- With **6** candidate models performing inconsistently on summer ghost spikes in the holdout set, tasked with selecting the most defensible forecaster for asymmetric uncertainty in environmental data; benchmarked Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints at max depth 4 and learning rate 0.05; landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric **80 percent** prediction intervals that hug the 0 floor and chop the top **15 percent** of summer ghost spikes.
- With sparse sensor coverage and concurrent proxy readings contaminating the holdout evaluation, tasked with making the September R squared defensible; implemented a 3 pass outlier system with pH bounds 7.0 to 9.0, seasonal caps of 15.0 on chlorophyll a and 50.0 on turbidity, and a rolling z score at z greater than 2.5 over 48 hours, then excluded **5** sparse sensors and **3** concurrent proxies; surfaced the honest R squared of **0.86** on dissolved oxygen and **0.81** on pH.
- With Oct and Nov gaps in the historical series threatening model integrity, tasked with restoring continuity for the winter forecast canvas; reconstructed gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all **6** lag features, and generated a synthetic winter canvas with a **4** degree Celsius floor and **0.4** degree diurnal amplitude; delivered a gapless 40 feature input ready for recursive forecasting.

**Junior Associate Software Developer at SS Engineers and Contractors, India, Aug 2023 to Aug 2024**

- With SS Engineers and Contractors running internal Data Dashboards, Analytics platforms, and Employee Portals used across the company, tasked with building and maintaining the front end features that day to day teams depended on; contributed React UI components across all three internal products; shipped features that stayed in daily use by internal teams throughout the year in role.
- With a client relying on a legacy AngularJS app that had to coexist inside an existing module federation setup alongside newer React micro frontends, tasked with porting the client screens across without breaking the running product; ported around **8** routes from AngularJS to React inside the module federation shell over **4** months of incremental releases; shipped the migration with no production incidents during rollout.

**Front End Developer Intern at SS Engineers and Contractors, India, Feb 2023 to July 2023**

- During a 6 month internship at SS Engineers and Contractors, tasked with learning the codebase and then taking on small UI work across internal Data Dashboards and Employee Portals under senior review; paired closely with senior developers to walk the codebase then shipped focused UI components including charts, filters, and profile pages, iterating each one on code review feedback until it landed; all contributed code was accepted and remained in production through the end of the internship.

---

## EDUCATION

**M.Sc. Data Science and Analytics, Apr 2025 to Present**
SRH University of Applied Sciences Heidelberg, GPA 1.9

**Bachelor of Technology in Computer Science, 2019 to 2023**
GL Bajaj Institute of Technology and Management, CGPA 7.3 of 10

---

## PERSONAL PROJECTS

### Multi-Agent RAG with LLM as Judge and Multilingual EN/DE Support
*Built with: Python, LangGraph, Ollama, Mistral 7B, Qwen2.5 14B, Pinecone, paraphrase-multilingual-MiniLM, spaCy, BM25, dense hybrid retrieval*

- With an English-only hybrid BM25 plus dense RAG policy analysis system over a 14 document corpus unable to serve German speakers, tasked with adding multilingual support without duplicating the corpus; migrated embeddings and retrieval to a paraphrase multilingual MiniLM L12 v2 shared vector space and built a LanguageAgent that centralises seeded language detection with a confidence floor; a German query now retrieves English sources and is answered in German end to end, with per chunk language recording enabling slice-by-language evaluation.
- To measure answer quality without hand grading, tasked with building an automated evaluation harness; implemented an LLM as Judge JudgeAgent scoring answers **1 to 5** on **5** dimensions at temperature 0 in JSON mode, eliminated self preference bias by running the judge on a different local model Qwen2.5 14B from the generator Mistral 7B, and built an EvalAgent computing **5** retrieval metrics and **4** generation metrics aggregated per language; all inference runs locally with Pinecone as the only external service.
- With the system scaling across multiple agent types and model calls, tasked with hardening performance and testability; extracted all model, language, index and eval settings into a config.yaml, added a build_pipeline factory so importing the orchestrator no longer requires Pinecone credentials, and cached the retriever encoder across searches instead of reloading per query; retrieval latency dropped measurably and the test suite runs without live credentials.

### CreditIQ: Fairness by Design Credit Scoring System
*Built with: Python, scikit-learn, AIF360, SHAP, Streamlit*

- For an SRH Heidelberg project on regulated credit scoring where the baseline model was failing the EU AI Act and AGG **80 percent** fairness bar, tasked with getting it back into compliance without gutting predictive quality; applied AIF360 mitigation and threshold calibration on a real credit dataset; raised the Disparate Impact ratio from a failing **0.79** to a compliant **0.88**.
- With younger women still being penalised after single axis age bias was corrected, tasked with finding and fixing the hidden intersectional pattern; used SHAP driven subgroup analysis to expose it and designed a **4 way** age by gender threshold matrix; corrected the intersectional bias without over correcting into reverse discrimination.
- With a large false negative rate silently rejecting good applicants, tasked with cutting it while keeping accuracy defensible; brought the false negative rate down from **44 percent** to **16.7 percent** while accuracy held at **75 percent** on the held out test split, then shipped a Streamlit decision support tool with plain language LLM generated explanations and **100 percent** branch coverage unit tests, clearing GDPR Article 22 and EU AI Act Article 14 human in the loop requirements.

---

## RESEARCH AND THESIS

### Bachelor Thesis: Diabetes Prediction Using Machine Learning
*Built with: Python, scikit-learn, Pandas, Seaborn, Google Colab*

- For a Bachelor thesis on diabetes prediction with a clinical dataset of **768** patients, tasked with building a defensible model comparison the examiners could audit; built a full end to end machine learning pipeline comparing **6** classifiers with **10 fold** cross validation and per model confusion matrices; delivered a model comparison that stood up in the thesis defence.
- Spotting biologically impossible zero values that the original authors had overlooked, tasked with restoring data integrity before any model fit; applied IQR based outlier removal and proper imputation; lifted the dataset from silently broken to a clean training input for every downstream model.
- With a **65 to 35** class imbalance making accuracy a misleading headline metric, tasked with choosing an evaluation that would not hide errors on the minority class; moved the headline metric from accuracy to ROC AUC, exposing the real error patterns accuracy had masked; produced an IEEE style paper with an honest limitations section that the supervisor accepted as publishable in substance.

---

## CERTIFICATIONS

**NVIDIA: Building LLM Applications With Prompt Engineering** — Issued 12 November 2025
**AWS Academy Graduate: AWS Academy Cloud Foundations** — Issued 15 July 2025

---

## ACHIEVEMENTS

**USAII Global AI Hackathon 2026, Finalist at Graduate Level** — Awarded by the United States Artificial Intelligence Institute for advancing to the Final Round through innovation, technical creativity, and applied AI on real world challenges.

---

## LANGUAGES

| Language | Level |
|---|---|
| English | Fluent, written and spoken |
| German | B1 in progress toward B2 |
| Hindi | Native |
