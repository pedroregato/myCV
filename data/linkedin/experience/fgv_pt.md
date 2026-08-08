# LinkedIn — Experiência: FGV (PT)
# Empresa: Fundação Getúlio Vargas (FGV)
# Cargo: Responsável Técnico | IA Aplicada, Automação & Integração de Sistemas
# Período: abril de 2019 – Atual
# Local: Rio de Janeiro, Brasil
# Atualizado: 2026-08-08

---

Nota: CLT FGV desde abr/2022; Consultor Sênior alocado via MGN Informática S.A. de abr/2019 a mar/2022 — mesma função e projetos durante todo o período.

Liderança técnica em projetos estratégicos de IA/ML, automação e integração de sistemas para áreas corporativas da DTI/FGV (Jurídico, Auditoria, Acadêmico, Contratos).

▸ SJUR [GenAI/LLM] — Ecossistema jurídico-IA:
→ Monitoramento e triagem processual via API DataJud/CNJ (Python · Streamlit), com validação semântica de status processual (ex: distinção entre trânsito em julgado e arquivamento definitivo) e cruzamento que já investigou 19.560 processos: R$ 28M em economia de provisionamento contábil anual (reclassificação de risco jurídico), 4.980 processos saneados (2025), 3.765 sinalizados (1T2026)
→ Classificador de citações em Diários Oficiais via LLM multi-provedor (DeepSeek · Gemini · Llama) com fallback entre provedores: 11.760 e-mails do SERDON processados em 12 meses (ago/2025-ago/2026) com 88% de acurácia e revisão humana para casos abaixo do limiar de confiança

▸ CIDA [ML/NLP] — Classificação automática de documentos acadêmicos:
96% de acurácia (Macro F1: 0,96) sobre 6.228 documentos processados. Pipeline clássico de NLP/ML (scikit-learn + spaCy), extração multi-engine de PDFs (Tesseract · PyMuPDF · Tika), modelo treinado em HPC FGV e servido via API Flask/JWT com hardening de produção (gunicorn, rate limiting, headers de segurança), integrado ao SGC FGV via SOAP.

▸ Process2Diagram [GenAI] — Reuniões → diagramas BPMN 2.0 + atas estruturadas + requisitos IEEE 830 em execução automatizada (Orchestrator próprio · LangGraph · LLMs). Acesso sob solicitação.

▸ ECM & BPM — Portal de Contratos: 1.330 instrumentos contratuais em pipeline BPM end-to-end com assinatura digital D4Sign. SE-SUITE Utils: wrappers SOAP (22+ operações), migração de 200+ documentos para 28 unidades, FastAPI/Docker.

▸ NDOC [Visão Computacional] — RetinaFace para detecção e legendagem automática de múltiplos rostos em acervo fotográfico institucional: metadados estruturados (JSON) com coordenadas de cada face e visualização interativa (SVG com zoom, pan e tooltips), entregue via API REST (FastAPI).

Stack: Python · LangGraph · LLMs · RAG · Streamlit · scikit-learn · PyTorch · NLP · FastAPI · SOAP · BPMN · Docker · Git/Bamboo (CI/CD) · D4Sign
