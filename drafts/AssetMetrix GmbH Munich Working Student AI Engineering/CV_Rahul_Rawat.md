# Rahul Rawat
Working Student: AI Engineering

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

M.Sc. Data Science and Analytics student at SRH University of Applied Sciences Heidelberg with hands-on production experience in Python AI engineering, cloud data pipelines, and machine learning systems. At eRay GmbH I shipped a recursive forecasting pipeline for environmental sensor data covering four indicators across a 40 feature input space. Personal projects include a multi-agent RAG system with LLM as Judge evaluation built on LangGraph and Ollama running fully locally, and a cloud native data platform on GCP processing over 128 thousand real time flight records through a medallion architecture. Available 20 hours per week and eager to contribute to an AI engineering team focused on building reliable, production quality systems.

---

## SKILLS

Python, LangChain, LangGraph, Ollama, Pinecone, scikit-learn, CatBoost, LightGBM, XGBoost, Prophet, MICE, SHAP, SQL, PySpark, BigQuery, dbt, Apache Airflow, GCP, Dataproc, GCS, Cloud Run, Cloud Scheduler, AWS, Tableau, TabPy, Docker, Git, React, Playwright, Pandas, NumPy, Matplotlib, Streamlit, FastAPI

---

## PROFESSIONAL EXPERIENCE

**Data Scientist at eRay GmbH, Heidelberg, Oct 2025 to Mar 2026**
*6-month collaboration with SRH University of Applied Sciences Heidelberg*

- During a 6 month collaboration between eRay GmbH and SRH Heidelberg to forecast lake water quality across **4** target indicators, tasked with designing the end to end recursive time series infrastructure over a **40** feature space; built a per target lag suite covering lag_1h, lag_24h, lag_3d, lag_7d, lag_roll_mean_24h and lag_roll_std_24h; delivered a production ready orchestrator with gate checks and ecological clips processing all targets in under **6** hours per forecast cycle.
- With **6** candidate models performing inconsistently on summer ghost spikes in the holdout set, tasked with selecting the most defensible forecaster for asymmetric uncertainty in environmental data; benchmarked Ridge, Gradient Boosting, LightGBM, XGBoost, CatBoost and Prophet with strict tree constraints; landed on CatBoost MultiQuantile at alpha 0.05, 0.5 and 0.85, producing asymmetric **80 percent** prediction intervals that chop the top **15 percent** of summer ghost spikes.
- With sparse sensor coverage and concurrent proxies contaminating the evaluation, tasked with making the September R squared defensible; implemented a 3 pass outlier system and excluded **5** sparse sensors and **3** concurrent proxies; surfaced the honest R squared of **0.86** on dissolved oxygen and **0.81** on pH.
- With Oct and Nov gaps threatening model integrity, tasked with restoring continuity; reconstructed gaps with IterativeImputer MICE, ran full Memory Buffer recalculation across all **6** lag features, and generated a synthetic winter canvas with a **4** degree Celsius floor and **0.4** degree diurnal amplitude.

**Junior Associate Software Developer at SS Engineers and Contractors, India, Aug 2023 to Aug 2024**

- With SS Engineers and Contractors running internal Data Dashboards, Analytics platforms, and Employee Portals used across the company, tasked with building and maintaining the front end features that day to day teams depended on; contributed React UI components across all three internal products; shipped features that stayed in daily use throughout the year in role.
- With a client relying on a legacy AngularJS app inside an existing module federation setup, tasked with porting the client screens across without breaking the running product; ported around **8** routes from AngularJS to React over **4** months of incremental releases; shipped with no production incidents during rollout.

**Front End Developer Intern at SS Engineers and Contractors, India, Feb 2023 to July 2023**

- During a 6 month internship, tasked with taking on UI work across internal platforms under senior review; shipped focused UI components including charts, filters, and profile pages, iterating on code review feedback; all contributed code remained in production through the end of the internship.

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

- With an English-only RAG system over a 14 document policy corpus unable to serve German speakers, tasked with adding multilingual support without duplicating the corpus; migrated embeddings to a shared multilingual vector space and built a LanguageAgent that centralises language detection with a confidence floor and routes preprocessing to language-matched spaCy pipelines; a German query now retrieves English sources and is answered in German end to end.
- To measure answer quality without hand grading, tasked with an automated evaluation harness; implemented an LLM as Judge scoring answers across **5** quality dimensions on a different model from the generator to eliminate self-preference bias, and an EvalAgent computing **5** retrieval metrics and **4** generation metrics per language; all inference runs fully locally with Pinecone as the only external service.
- With the system scaling across multiple agents, tasked with testability and performance; extracted settings into config.yaml, added a build_pipeline factory so importing the orchestrator no longer requires live credentials, and cached the retriever encoder across searches; retrieval latency dropped measurably and the test suite runs offline.

### Real-Time Flight Tracking Data Pipeline
*Built with: Python, PySpark, BigQuery, dbt, Apache Airflow, GCP (Dataproc, GCE, GCS), Tableau, TabPy, OAuth2*

- For a Data Engineering module at SRH needing a real time joined view over live aircraft above Germany, tasked with the collection and enrichment layer; built Python collectors polling the OpenSky Network API every **30 seconds** and PySpark cleaning on GCP joining against airport, aircraft, and weather data across **4** sources, producing a clean joined table covering more than **128 thousand** records.
- With the pipeline running on raw data and no automated refresh, tasked with the modelling and automation layer; shaped data into analysis-ready tables with dbt, computed nearest airport labels with PySpark, and orchestrated the full system with Apache Airflow on GCS backed storage and Dataproc compute so batch and real time layers refresh every **15 minutes** without operator intervention.
- With the pipeline sitting on data but no business insight, tasked with the analytics surface; built a Tableau workbook backed by Python statistics through TabPy on the dbt aggregates, surfacing the finding that air traffic drops **4.4 times** in heavy rain and clusters around hubs like Frankfurt and Munich.

---

## RESEARCH AND THESIS

### Bachelor Thesis: Diabetes Prediction Using Machine Learning
*Built with: Python, scikit-learn, Pandas, Seaborn, Google Colab*

- For a Bachelor thesis on diabetes prediction with a clinical dataset of **768** patients, tasked with building a defensible model comparison; built a full end to end machine learning pipeline comparing **6** classifiers with **10 fold** cross validation and per model confusion matrices; delivered a model comparison that stood up in the thesis defence.
- Spotting biologically impossible zero values in the source data, tasked with restoring data integrity; applied IQR based outlier removal and proper imputation; lifted the dataset from silently broken to a clean training input for every downstream model.
- With a **65 to 35** class imbalance making accuracy misleading, tasked with choosing an evaluation that would not hide errors on the minority class; moved the headline metric from accuracy to ROC AUC and produced an IEEE style paper the supervisor accepted as publishable in substance.

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
