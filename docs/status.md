# Progreso – Databricks GenAI Engineer Associate

## ESTADO – 18-nov-2026 (sesión 2)
Prácticas completadas: P1 Setup + Foundation Model APIs + ai_query · P2 RAG04 en curso (pasos 1–3 hechos: lectura binaryFile + ai_parse_document v2.0 persistido en Delta)
Lecciones cubiertas: M01 (parcial) · M02 (parcial) · AGT01 C2 · RAG04 (parcial: D1 ai_parse_document, D2 chunk size vs embedding limit + overlap) · EVAL1.1 A (non-determinism ↔ temperature)
Recursos creados en el workspace (y si siguen activos): schema workspace.genai_cert ✅ · volume workspace.genai_cert.docs ✅ con 2 PDF ficticios (aquapure_3000_manual.pdf 3 pág., invoice_INV-2026-0457.pdf 1 pág.) · tabla workspace.genai_cert.parsed_docs ✅ (path, parsed VARIANT; manual 30 elements, factura 9; error_status null) · notebook 02_parsing_chunking · Nada que parar (no hay endpoints ni índices)
Aciertos por dominio: D1 2/3 · D2 1/1 · D3 0/0 · D4 1/1 · D5 0/0 · D6 1/1
Puntos débiles: "Choose two" → mejorado (2/2 hoy con dos letras) · síntoma → parámetro → acertado hoy (repreguntar más adelante para consolidar)
Siguiente paso recomendado: retomar P2 en el paso 4 → explotar parsed:document:elements (variant_explode / explode en PySpark), inspeccionar los tipos de element y filtrar ruido (page_header/page_footer: "Sample document…", "Page N") → ai_classify (manual vs invoice) y ai_extract (invoice_id, date, total) → ai_prep_search → tabla Delta de chunks con CDF (delta.enableChangeDataFeed). Empezar con 1–2 preguntas de repaso.

### Notas de entorno descubiertas
- ai_query + responseFormat en estilo DDL: el esquema exige un único campo envoltorio (STRUCT<result:STRUCT<...>>), pero la respuesta llega sin el envoltorio y como STRING JSON. Se lee con res:campo o con from_json.
- ai_parse_document funciona en Free Edition (serverless). Llamado desde PySpark con F.expr("ai_parse_document(content, map('version','2.0'))").
- Spark muestra las rutas de volume como dbfs:/Volumes/... (equivale a /Volumes/...).
- Preferencia: código en PySpark (AI Functions vía F.expr), con la equivalencia SQL en una línea cuando el examen use SQL. Ya está en las instrucciones del proyecto.

## ESTADO – 18-nov-2026 (sesión 1)
Prácticas completadas: P1 Setup + Foundation Model APIs + ai_query (Playground, modelParameters, responseFormat)
Lecciones cubiertas: M01 (parcial: hallucination, structured output) · M02 (parcial: AI Functions, ai_query, model services/Unity Gateway) · AGT01 C2 (model services vs endpoints)
Recursos creados en el workspace (y si siguen activos): schema workspace.genai_cert ✅ · volume workspace.genai_cert.docs ✅ (no consumen; nada que parar)
Aciertos por dominio: D1 1/2 · D2 0/0 · D3 0/0 · D4 1/1 · D5 0/0 · D6 1/1
Puntos débiles: preguntas "Choose two" (respondí solo una) · relacionar síntoma → parámetro (temperature = variación, max_tokens = truncado)
Siguiente paso recomendado: Práctica 2 – RAG04: ai_parse_document → ai_classify/ai_extract → ai_prep_search → tabla Delta de chunks con CDF. Antes: subir 1–2 PDF pequeños al volume docs y comprobar que ai_parse_document está disponible en Free Edition.
