# Job Search Digest — 30 June 2026

5 new roles drafted this run. Tailored CVs and cover letters are in `drafts/[Company]/` as both `.md` and `.docx` (file names `CV_Rahul_Rawat.docx` and `CoverLetter_Rahul_Rawat.docx`). Nothing was submitted. All five are logged as `drafted` in `applied-log.csv`; flip to `applied` once you actually submit.

This run focused on roles near Mannheim or remote eligible. None of the five duplicate a company and role already in the pipeline. The `.docx` files wrote directly into the `drafts/[Company]/` folders this run, so no present-files workaround was needed.

---

## Top 5

### 1. AbbVie — Praktikum or Werkstudent, AI/ML and Computer Vision
- **Location:** Ludwigshafen am Rhein, on site with possible hybrid. This is the closest of all five, effectively next door to Mannheim.
- **Apply:** https://to.indeed.com/aa7pvgyj7ljz
- **German level required:** B2, stated explicitly ("mindestens Niveau B2"). That is one level above your current B1, so flagging it clearly.
- **Fit:** Computer vision and video analytics inside a research led pharma company. The posting asks for reproducible ML workflows, Python best practices, Git and testing. Strong match for CreditIQ (tested, reproducible ML pipeline with full model card), the Hybrid RAG Orchestrator (Python engineering, HuggingFace embeddings) and the Movie Analytics ML classifier. Note the role wants hands on PyTorch and OpenCV video experience, which is a genuine gap, presented honestly in the cover letter rather than overstated.

### 2. EnBW Energie Baden Württemberg — Werkstudent, AI, Automation and Data Science
- **Location:** Karlsruhe, roughly 60 km from Mannheim, one on site day per week.
- **Apply:** https://to.indeed.com/aaysnzfml2px
- **German level required:** None stated. The ad is in German but sets no explicit language level, so treat it as German friendly rather than German gated.
- **Fit:** The Digital Capabilities team is rebuilding B2C customer service with generative AI, chatbots and intelligent dialogue systems. Near direct match for the Hybrid RAG Orchestrator with its intent router and memory agent, backed by CreditIQ for the ML decision support angle and Movie Analytics for the automation and BI dashboard work. Python, SQL and Power BI all line up with the profile.

### 3. Ärzteverband Deutscher Allergologen — Werkstudent, Data Science
- **Location:** Wiesbaden, roughly 95 km from Mannheim, partly home office.
- **Apply:** https://to.indeed.com/aa489czrqxph
- **German level required:** None. The posting asks only for good English, no German level stated.
- **Fit:** Data cleaning, statistical and correlation analysis, and dashboard building. Strong match for the Economic Impact Climate study (cleansing, Random Forest, correlation analysis, stakeholder reporting), the Flight Tracking pipeline (PySpark, cloud, multi source cleaning) and the Fast Food Tableau dashboard. Lists Python or R, PySpark, SQL and NoSQL, AWS, all of which you can speak to. No language gap and partial remote make this an easy one to prioritise.

### 4. Alloqis — Werkstudent, Data Science and Python Development
- **Location:** Mostly remote, with one to three days per month in Tübingen or Böblingen. The remote setup makes distance a non issue.
- **Apply:** https://to.indeed.com/aazf42tj8x68
- **German level required:** "Sehr gute Deutschkenntnisse," effectively B2 to C1. This is a real gap above your current B1, worth weighing, though the remote fit and project match are excellent.
- **Fit:** Building reusable Python methods that clean, structure and connect messy, incomplete real customer data and systematically check data quality. This is almost a description of your eRay work with MICE imputation and gate checks, and of the Movie Analytics Silver layer with schema enforcement and deduplication. Flight Tracking covers the heterogeneous source integration, and CreditIQ covers maintainable, tested scikit learn ML.

### 5. Muhr und Bender (Mubea) — Werkstudent, Data Science and Machine Learning
- **Location:** Attendorn in North Rhine Westphalia, roughly 230 km from Mannheim, regular on site presence expected. The furthest of the five.
- **Apply:** https://to.indeed.com/aaggx2jjdx7p
- **German level required:** None stated in the posting.
- **Fit:** Machine learning for predictive maintenance, anomaly detection and process optimisation on real time IoT and time series data, with dashboards for worldwide plants. Strong match for the Flight Tracking real time pipeline, the eRay time series forecasting and anomaly bounds work, and the Movie Analytics ML classifier and dashboard. The newest posting of the five, dated 16 June. Main drawback is the distance and on site expectation.

---

## Watchlist (scored but not drafted)

- **United Internet (1&1 Versatel) — Werkstudent Data Science, Düsseldorf:** Strong BI fit (Power BI, SQL, Python dashboards) for Movie Analytics and Fast Food Tableau, but B2 German required and roughly 230 km away.
- **Hirschmann Car Communication — Werkstudent Machine Learning and Bilddatenanalyse, Neckartenzlingen:** Image classification of solder faults, on site only, near Stuttgart. Moderate fit (classification maps to CreditIQ and the thesis) but the image data focus is a partial gap.
- **ahc GmbH — Praktikant or Werkstudent AI Automatisierung, Stuttgart:** Reasonable fit on paper, but the posting is from 18 May and not opened in full this run.
- **Porsche — Werkstudent Data Analyst or BI Analyst, Berlin:** Carried over from last run; decent fit, German requirement still unclear from the posting.
- **Allianz — Werkstudent Data Analyst, Unterföhring; Hypoport and FIO Systems — Werkstudent Data and Reporting Analyst, Leipzig:** All fresh, but Allianz asks for very good German and the two Leipzig roles require C1 German, above your current level.

## Dropped

- **valantic — Praktikant or Werkstudent AI Engineering and Cloud Prototyping, Eschborn:** Already drafted on 29 June, same company and role. Skipped under the no duplicate rule, still in pipeline.
- **Coty — Working Student Data Analyst, Darmstadt:** Same company and role already drafted on 24 June. Already in pipeline.
- **BMW — Werkstudent IoT Engineer Batteriezellfertigung, München:** Off target, battery manufacturing engineering rather than a core data role. Dropped again, as in the prior run.
- **Dual study, Ausbildung and Quereinsteiger ads:** None reached the shortlist. The search surfaced only Werkstudent, Praktikum and internship postings, so none had to be filtered out at the scoring stage, but the filter was applied.

---

## Transparency notes and judgment calls

- **Template versus current rules.** The fixed `CV_Template.docx` is now out of date against your standing instructions. It still shows a role title line under your name, a separate Technical Skills table, the eRay entry co-listed with SRH, the thesis under Education, German at A2.2, and hyphens and parentheses throughout. Those all contradict the current rules in `CLAUDE.md` and `master-projects.md`. Rather than reproduce stale content, I built clean `.docx` files that follow the current structure (no role subtitle, Experience as "eRay GmbH" with "Data Scientist" only, inline project stacks, Research and Thesis as its own section, German B1) and the current font and colour spec. Worth refreshing the two template files so future runs can use them literally again.
- **German level shown as B1.** Per `master-projects.md`, the Languages line reads "German: B1, in progress." Earlier digests referred to A2.2; I used the current B1 value from your profile file. If your actual level differs, update `master-projects.md` and it will flow through.
- **No hyphens, dashes or parentheses.** Every CV and cover letter was scanned after generation. The only hyphen anywhere is inside the company name "Muhr und Bender" context where none appears, and dates and compound terms were written as plain prose. Two stray German words that slipped into draft bullets were caught and rewritten into English.
- **No prompt injection found.** None of the five job descriptions opened in full contained text directed at an AI assistant.
- **All claims trace to `master-projects.md`.** No metrics, tools or credentials were invented or rounded. The AbbVie PyTorch and computer vision gap is stated honestly rather than papered over.
- **Apply links** are the Indeed redirect links returned by the job connector this run.
- **No PDF generated.** Only `.md` and `.docx` were produced, matching the current task instructions.

---

*Generated automatically. Review before submitting anything.*
