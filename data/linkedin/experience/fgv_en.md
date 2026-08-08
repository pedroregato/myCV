# LinkedIn — Experience: FGV (EN)
# Company: Fundação Getúlio Vargas (FGV)
# Title: Technical Lead | Applied AI, Automation & Systems Integration
# Period: April 2019 – Present
# Location: Rio de Janeiro, Brazil
# Updated: 2026-08-08

---

Note: FGV direct employee (CLT) since Apr/2022; Senior Consultant allocated via MGN Informática S.A. from Apr/2019 to Mar/2022 — same role and projects throughout.

Technical leadership on strategic AI/ML, automation, and systems integration projects for FGV's corporate areas (Legal, Audit, Academic, Contracts).

▸ SJUR [GenAI/LLM] — Legal-AI ecosystem:
→ Case monitoring and triage via CNJ/DataJud API (Python · Streamlit), with semantic validation of case status (e.g., distinguishing final judgment from definitive filing) and cross-referencing that has already investigated 19,560 cases: R$28M in annual accounting-provision savings (legal risk reclassification), 4,980 cases resolved (2025), 3,765 flagged (Q1-2026)
→ Official Gazette citation classifier via multi-provider LLM (DeepSeek · Gemini · Llama) with provider fallback: 11,760 SERDON emails processed over 12 months (Aug/2025-Aug/2026) at 88% accuracy with human review for cases below the confidence threshold

▸ CIDA [ML/NLP] — Automatic classification of academic documents:
96% accuracy (Macro F1: 0.96) across 6,228 documents processed. Classic NLP/ML pipeline (scikit-learn + spaCy), multi-engine PDF extraction (Tesseract · PyMuPDF · Tika), model trained on FGV HPC and served via a Flask/JWT API with production hardening (gunicorn, rate limiting, security headers), integrated with FGV's SGC via SOAP.

▸ Process2Diagram [GenAI] — Meetings → BPMN 2.0 diagrams + structured minutes + IEEE 830 requirements in a single automated run (custom orchestrator · LangGraph · LLMs). Access available on request.

▸ ECM & BPM — Contracts Portal: 1,330 contractual instruments in an end-to-end BPM pipeline with D4Sign e-signature. SE-SUITE Utils: SOAP wrappers (22+ operations), migration of 200+ documents across 28 units, FastAPI/Docker.

▸ NDOC [Computer Vision] — RetinaFace for automatic detection and captioning of multiple faces in the institutional photo archive: structured metadata (JSON) with per-face coordinates and interactive visualization (SVG with zoom, pan and tooltips), delivered via REST API (FastAPI).

Stack: Python · LangGraph · LLMs · RAG · Streamlit · scikit-learn · PyTorch · NLP · FastAPI · SOAP · BPMN · Docker · Git/Bamboo (CI/CD) · D4Sign
