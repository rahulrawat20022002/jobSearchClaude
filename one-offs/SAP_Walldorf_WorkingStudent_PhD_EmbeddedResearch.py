"""One-off draft, 4 August 2026.

Draft for SAP Walldorf Working Student (f/m/d) AI and Data Scientist in PhD
Programs and Embedded Research, requisition 454731, posted 30 July 2026.

Explicit user override outside the current backlog pause. Rah asked for this
listing specifically. The pipeline hard backlog gate does not apply to a
one-off user request.

Language track: English. The SAP posting body is in English, no German
requirement is stated (German is only nice-to-have). Per the 20 July 2026
language match rule, deliverables ship in English.

Best project fit:
- Project #1 Hybrid RAG Orchestrator, direct match for agentic AI, LangChain,
  LLM systems on Llama 3.1 8b via Groq.
- Project #2 CreditIQ, direct match for LLM plain language explanation, SHAP
  driven interpretability, and research to industry translation with full
  regulatory documentation.
Research and Thesis renders the Bachelor thesis on Diabetes Prediction as a
research signal that translates directly to the PhD Programs angle.

Certifications lead with NVIDIA (LLM, prompt engineering), AWS Academy Cloud
Foundations (hyperscalers mentioned as nice-to-have), and Google Data
Analytics Foundations for the reporting workflows piece.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_html import build_role
from role_configs import (
    ERAY_BULLETS_EN,
    DIABETES_BULLETS_EN,
    CERT_NVIDIA,
    CERT_AWS,
    CERT_GOOGLE,
    ACH_USAII_EN,
    P_RAG_EN,
    P_CREDITIQ_EN,
)


cfg = {
    "folder": "SAP Walldorf Working Student AI Data Scientist PhD Programs Embedded Research",
    "company": "SAP",
    "lang": "en",
    "role_strip": "Working Student, AI and Data Scientist in PhD Programs and Embedded Research",
    "cl_date": "4 August 2026",
    "cl_subject": "Working Student AI and Data Scientist in PhD Programs and Embedded Research in Walldorf, requisition 454731",
    "profile": "Data Science and Analytics Master student at SRH Heidelberg based in Mannheim, with hands on delivery of agentic AI systems, classic machine learning, and applied research translation into working prototypes. I have shipped a Hybrid RAG Orchestrator on Llama 3.1 8b via Groq with a custom decision making router and LangChain orchestration, a fairness by design credit scoring system with SHAP driven interpretability, an LLM generated plain language explanation layer, and full regulatory documentation, and a recursive time series pipeline at eRay GmbH benchmarking six models head to head with strict anti leakage evaluation. Proficient in Python, pandas, scikit learn, and comfortable across the modern AI stack from classic machine learning to LLMs, I am the right fit for the Working Student role in PhD Programs and Embedded Research at SAP Walldorf.",
    "experience_bullets": ERAY_BULLETS_EN,
    "projects": [P_RAG_EN, P_CREDITIQ_EN],
    "research_bullets": DIABETES_BULLETS_EN,
    "certifications": [CERT_NVIDIA, CERT_AWS, CERT_GOOGLE],
    "achievements": [ACH_USAII_EN],
    "cl_paragraphs": [
        "I am applying for the Working Student role as AI and Data Scientist in PhD Programs and Embedded Research at SAP in Walldorf, requisition 454731. The brief on optimizing reporting workflows and PhD pipeline analytics with data science, contributing to AI use cases including agentic solutions and research to industry knowledge transfer, and applying AI technologies from classic machine learning to large language models to automate program management tasks, maps directly to the work I have been shipping over the past year.",
        "My Hybrid RAG Orchestrator is a working agentic system that classifies user intent into three execution paths, local knowledge retrieval, external web search, or direct conversational logic, built on Llama 3.1 8b via Groq with LangChain orchestration, a stateful memory agent inside the inference pipeline, and a persistent ChromaDB vector store with HuggingFace MiniLM L6 v2 embeddings, shipped behind a Streamlit interface. That is precisely the agentic AI, LLM, and research to industry translation shape the PhD Graduate Team is asking for, and it maps onto the LangChain and LangGraph nice to have.",
        "In CreditIQ I built a fairness by design credit scoring system that raised the Disparate Impact ratio from a failing 0.79 to a compliant 0.88, used SHAP driven subgroup analysis to expose intersectional bias and correct it through a four way threshold matrix, cut the false negative rate from 44 percent to 16.7 percent while accuracy held at 75 percent, and shipped a Streamlit decision support tool with an LLM generated plain language explanation layer, backed by unit tests at 100 percent branch coverage and a full regulatory write up spanning EU AI Act Annex III, GDPR, model card, and attack vectors. That is directly the explainable AI, interpretability, and research to industry translation the role calls for. At eRay GmbH I benchmarked six models head to head on real sensor data with strict anti leakage rules, exactly the honest research methodology the PhD talent development context needs.",
        "My Bachelor thesis, Diabetes Prediction Using Machine Learning, was written up as an IEEE style paper with a candid limitations section and follow up study notes and was accepted by my supervisor as publishable in substance, which gives me first hand experience at the academia industry interface the role values. I hold the NVIDIA Building LLM Applications With Prompt Engineering, AWS Academy Cloud Foundations, and Google Data Analytics Foundations certificates, and I am comfortable with GitHub, Docker, and the wider data science stack. English is my fluent working language, and my German is currently at B1 in progress. I would be glad to align the exact scope of the reporting workflow and agentic AI use cases with the PhD Graduate Team in Walldorf.",
    ],
}


if __name__ == "__main__":
    build_role(cfg)
