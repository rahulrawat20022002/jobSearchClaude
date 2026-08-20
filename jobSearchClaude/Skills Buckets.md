# Skills Buckets

The 19 August 2026 rules retired the flat comma line under `Skills` and replaced it with five grouped buckets, one row per bucket, rendered as a two column table in HTML and PDF, and as `Label: items` paragraphs in docx. This page documents each bucket's contents as of the current `build_html.py` (see [[build_html.py Overview]]) and explains the four items that were retired.

The bucket labels are localised: EN track uses the left column, DE track uses the right column. Item text is the same in both tracks (product and library names).

## The five buckets

### 1. AI and Agents / KI und Agenten

- LangGraph
- RAG
- LLM as Judge
- Prompt Engineering
- Ollama
- spaCy
- BM25

### 2. Data and ML / Daten und ML

- Python
- SQL
- PySpark
- scikit learn
- CatBoost
- XGBoost
- LightGBM
- Prophet
- MICE

### 3. Cloud and Orchestration / Cloud und Orchestrierung

- GCP, BigQuery, Cloud Run
- AWS
- Docker
- Apache Airflow
- dbt
- Git

### 4. Dashboards

- Tableau
- Looker Studio
- Streamlit
- Power BI

### 5. Web

- React
- module federation
- Playwright
- HTML5
- CSS3

## Where these live in code

`build_html.py` defines `SKILL_BUCKETS_EN` and `SKILL_BUCKETS_DE` at the top of the render module. A per-role override can be passed via `cfg['skill_buckets']` if a specific posting warrants a different arrangement, but the default is always the list above.

A legacy flat `DEFAULT_SKILLS` list is kept for backward compatibility with any external caller of `_skills_line()`, but the current CV render uses `_skill_buckets(cfg)` which reads the grouped structure.

## Why Databricks, Delta Lake, LangChain and PyTorch were removed

Rule 8 of [[19 August 2026 Rules]] explicitly retires these four items because they are not evidenced in any project bullet on the CV, and listing unevidenced skills is keyword stuffing which violates invariant #3 (never fabricate an outcome, see [[Pipeline Overview]]).

- **Databricks** — Rah has used it briefly but no CV bullet demonstrates a Databricks-specific deliverable. Cloud and orchestration bucket instead lists GCP, AWS, Airflow and dbt, all of which are evidenced.
- **Delta Lake** — same as Databricks: no bullet on the CV mentions Delta Lake tables. Removed with Databricks.
- **LangChain** — the agent stack in Rah's projects is LangGraph (which stays), not LangChain. Listing both when only one is evidenced would misrepresent the depth.
- **PyTorch** — the ML work on the CV is gradient boosting (CatBoost, XGBoost, LightGBM), classical scikit learn, and MICE for imputation. Deep-learning framework depth is not there, so listing PyTorch would be aspirational rather than accurate.

## Adding a bucket item

The rule of thumb: add an item to a bucket only when at least one project or experience bullet on the current CV clearly demonstrates the tool. The bar is "an interviewer asking you about it will land on real work you can walk through", not "you have used it once at some point".

Add it in `master-projects.md` first (the source of truth for what the CV can claim), then reflect in `build_html.py`'s `SKILL_BUCKETS_*` lists.

## See also

- [[19 August 2026 Rules]] rule 8 for the grouping rule itself
- [[build_html.py Overview]] for `_skill_buckets(cfg)` and the render paths
- [[CV Rules]] for the full historical rule sequence
