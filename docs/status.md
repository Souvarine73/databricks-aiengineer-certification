# Progreso – Databricks GenAI Engineer Associate

## ESTADO – 22-nov-2026 (sesión 7, modo práctica / RAG04 + P2)
Prácticas completadas: **P2 en curso (🟡)**. Notebooks en `src/p2_document_pipeline/`: `01_parse_documents` (leer PDFs `binaryFile` → `ai_parse_document` v2.0 → filtrar ruido → `doc_elements`) y `02_classify_extract` (`ai_classify` v2.1 por documento → `doc_classified`; `ai_extract` v2.1 sobre invoices → `invoice_fields`). `03_chunk` solo con la prueba de `ai_prep_search` (sin tabla `chunks` aún).
Lecciones cubiertas: RAG04 en curso. Teoría + práctica hechas: A1, B1, C (`variant_explode`), C1, C2, D1. Parciales: D2 (granularidad, discutido sin cerrar), D3 (visto en la salida real). Pendientes: E1 (→ P3), E2 (CDF), F, quiz y glosario. Sin preguntas de quiz en la sesión.
Recursos creados en el workspace (y si siguen activos): PDFs `aquapure_3000_manual.pdf` e `invoice_INV-2026-0457.pdf` en la raíz del volume `workspace.genai_cert.docs`; tablas `parsed_docs`, `doc_elements`, `invoice_fields` y, por confirmar, `doc_classified`. Todo sin coste, se mantiene.
Aciertos por dominio: D1 25/27 · D2 3/3 · D3 8/9 · D4 9/10 · D5 4/4 · D6 4/4 (sin cambios)
Puntos débiles: ninguno por fallos. Repaso de RAG01 (Genie Chat vs Agent mode) propuesto al inicio, sin respuesta.
Notas técnicas:
- `variant_explode` es una *table-valued function*: solo va en `FROM`/`LATERAL`, no en `select(F.expr(...))` (da `UNRESOLVED_ROUTINE`). En PySpark: `F.explode`/`F.posexplode` sobre `variant_get(col, '$.document.elements', 'array<variant>')`.
- `ai_parse_document` v2.0: cada elemento tiene `type` (`page_header`, `title`, `section_header`, `text`, `table`, `page_footer`, `page_number`), `content` (las tablas salen como HTML), `bbox`, `confidence`, `description`, `id`. Hay que filtrar `page_header`/`page_footer`/`page_number` como ruido (manual 30 → 21 elementos; invoice 9 → 6).
- Routing: `ai_classify` sobre el texto completo del documento (elementos unidos y ordenados por `pos`) dio manual → `user_manual` 0.85, invoice → `invoice` 0.94. `ai_extract` v2.1 devolvió los 5 campos correctos del invoice, con `total_due` numérico.
- **`ai_prep_search` funciona en Free Edition ✅** (serverless). Doc oficial: firma `ai_prep_search(parsed [, options])`, `parsed` = VARIANT de `ai_parse_document` o STRING; `options` documenta `version` y `schema`; devuelve VARIANT, 1 fila por documento, chunks en `document.contents`; **Beta**, requiere DBR 18.2+. Cada chunk: `chunk_id`, `chunk_position`, `chunk_to_embed` (con cabecera de metadatos, resumen de tablas y "Related questions" generadas), `chunk_to_retrieve`, `pages`.
- Resultado real con el manual (3 págs.): solo **2 chunks**; el chunk 0 es grande (secciones 1–7, ~1000 tokens estimados) y el corte cae **dentro de una tabla** (HTML roto al inicio del chunk 1); una línea corrupta en los metadatos de `chunk_to_embed`. La doc no explica cómo decide el tamaño ni da parámetro para controlarlo (por verificar el listado completo de `options`). Los apuntes dicen "semantic boundaries"; la salida no encaja del todo.
- `gte-large-en` admite hasta 8192 tokens según la doc de GTE (los 512 de los apuntes son solo un ejemplo): el chunk 0 no se trunca, pero es poco granular.
- Convención de código añadida a CLAUDE.md: un notebook por etapa, resultado en tabla Delta, ruta exacta del archivo en cada paso, solo la versión válida del código.
Siguiente paso recomendado: (1) confirmar que `doc_classified` existe; (2) medir los chunks (`F.length` de `chunk_to_retrieve`/`chunk_to_embed`); (3) paso 8: tabla `chunks` con `doc_type` + CDF (`ALTER TABLE … delta.enableChangeDataFeed = true`); (4) decidir si añadimos un chunking propio por `section_header` para comparar estrategias (D2); (5) cerrar RAG04 con quiz y `/glosario`. Índice AI Search (E1) en P3.

## ESTADO – 22-nov-2026 (sesión 6, modo práctica/lección M02 + RAG01)
Prácticas completadas: **P1 ✅** (schema, volume, `ai_query`, 3 modelos, AI Functions).
Lecciones cubiertas: **M01, M02 y RAG01 completas** en teoría + glosario + quiz de cierre (M02 5/5, RAG01 4/5). Las prácticas de RAG01 (C1 Genie Agent, E1 Lakebase Search) quedan para P3.
Recursos creados en el workspace (y si siguen activos): ninguno nuevo (schema, volume y support_tickets se mantienen, sin coste).
Aciertos por dominio: D1 25/27 · D2 3/3 · D3 8/9 · D4 9/10 · D5 4/4 · D6 4/4
Puntos débiles: (1) **Genie Chat vs Agent mode**: estructurados en ambos, no estructurados (PDF en Volumes) solo en Agent mode. (2) **Elegir modo Lakebase Search**: significado + término exacto + JOIN = hybrid (fallé keyword-only, acerté la repregunta). (3) no-code vs code-first: acertado en RAG01, mantener en `/repaso`. Nota: DASF es marco/catálogo de riesgos, no control en runtime. Pendiente de verificar en docs: judge Correctness y ground truth (EVAL2.1); disponibilidad de Genie Agents y Lakebase en Free Edition (antes de P3).
Siguiente paso recomendado: RAG04 (Document Parsing and Chunking, p. 33) y P2. Mini-simulacro tras 3–4 lecciones (tras RAG06).

## ESTADO – 22-nov-2026 (sesión 5, modo teoría)
Prácticas completadas: sin cambios (P1 sigue 🟡; no se tocó el workspace).
Lecciones cubiertas: sin cambios en coverage.md (M02 · E1–F1 y cierre de lección siguen pendientes). Repregunta de no-code vs code-first (Genie Agent vs Agent Framework) acertada. Preguntas 11–13 del simulacro externo, todas acertadas.
Recursos creados en el workspace (y si siguen activos): ninguno nuevo.
Aciertos por dominio: D1 17/19 · D2 2/2 · D3 8/8 · D4 7/7 · D5 1/1 · D6 1/1
Puntos débiles: no-code vs code-first (repregunta acertada, mantener en `/repaso`). Conceptos nuevos a consolidar, **fuera de los apuntes** (verificar en docs.databricks.com): `resources` en `mlflow.pyfunc.log_model` (`DatabricksVectorSearchIndex`, `DatabricksServingEndpoint`) y automatic authentication passthrough (valida permisos al desplegar, service principal efímera) vs OBO `UserAuthPolicy` (valida por petición); MLflow Prompt Registry (versión inmutable vs alias mutable, `set_prompt_alias` para rollback inmediato, `register_prompt` no mueve alias).
Notas técnicas: Delta Sync index TRIGGERED → `VectorSearchClient().get_index(endpoint_name, index_name).sync()` como última tarea del job (`depends_on` la escritura de chunks); CDF es requisito previo, no sincroniza solo. `pipeline_type` se fija al crear el índice (por confirmar en la doc). Firmas de `get_index` y `log_model(name=...)` por verificar.
Siguiente paso recomendado: volver a modo práctica/teoría con M02 · E1 (Data leakage, prompt injection, misuse; D5), cierre de M02 con `/glosario` + quiz, y pasar a RAG01.

## ESTADO – 21-nov-2026 (sesión 4, modo práctica)
Prácticas completadas: P1 en curso (🟡). Notebook `04_ai_functions` completo: ai_classify, ai_extract (v2.1, con `description` en el campo `language` para evitar nulls), ai_summarize, ai_translate, ai_mask.
Lecciones cubiertas: M02 A1–D1 completo (B1 AI Functions, B2 Compound, B3–B4 Platform, C1 Organizational shifts, D1 Roadmap). Falta M02 · E1 (seguridad, D5) y el cierre de lección (glosario + quiz de 5). P1 sigue 🟡 hasta cerrar M02.
Recursos creados en el workspace (y si siguen activos): ninguno nuevo (schema, volume y support_tickets se mantienen, sin coste).
Aciertos por dominio: D1 16/18 · D2 1/1 · D3 8/8 · D4 5/5 · D5 1/1 · D6 1/1
Puntos débiles: **no-code vs code-first** (Genie / Agent Bricks vs Agent Framework): fallé dos en B3 y luego acerté la repregunta. Repasar en `/repaso`.
Notas técnicas: ai_extract devuelve `null` si el dato no está literal; mejorar la `description` del schema. Confundió tracking number con order_id (también depende de la description). En los apuntes, B3 pone Serving endpoints en etapa 4 y B4 pone Model Serving en etapa 3 (inconsistencia). Pendiente verificar en docs.databricks.com la firma y los idiomas de `ai_summarize` (max_words, por defecto 50) y `ai_translate`.
Siguiente paso recomendado: M02 · E1 (Data leakage, prompt injection, misuse, D5), cierre de M02 con `/glosario` + quiz, y pasar a RAG01. Repregunta de no-code vs code-first.

## ESTADO – 20-nov-2026 (sesión 3, cierre, modo teoría)
Prácticas completadas: sin cambios (P1 sigue en curso 🟡; no se tocó el workspace).
Lecciones cubiertas: sin cambios en coverage.md. Preguntas 9–10 del simulacro externo, ambas acertadas (P9 Supervisor Agent: Examples/Guidelines + descripciones; P10 clasificación con `ai_query` en ingesta + cuarentena). Se dio un ejemplo PySpark del patrón P10 (`ai_query` batch → quarantine/cleared).
Recursos creados en el workspace (y si siguen activos): ninguno nuevo.
Aciertos por dominio: D1 10/10 · D2 1/1 · D3 8/8 · D4 4/4 · D5 0/0 · D6 1/1
Puntos débiles: ninguno por fallos. Dudoso de sintaxis resuelto: `concat('{prompt}', substr(text,1,4000))` dentro de `F.expr` (f-string lo resuelve Python, `text` lo resuelve Spark). Fuera de los apuntes: patrón de cuarentena con sign-off humano.
Siguiente paso recomendado: volver a práctica: ejecutar el paso 3 de `04_ai_functions` (`ai_extract`), seguir con ai_summarize, ai_translate, ai_mask y cerrar M02 · B1.

## ESTADO – 20-nov-2026 (sesión 3, modo teoría)
Prácticas completadas: sin cambios (P1 sigue en curso 🟡; no se tocó el workspace).
Lecciones cubiertas: sin cambios en coverage.md. Sesión de 6 preguntas sueltas de simulacro externo (capturas, preguntas 3–8 de un test de 45), todas acertadas.
Recursos creados en el workspace (y si siguen activos): ninguno nuevo.
Aciertos por dominio: D1 9/9 · D2 0/0 · D3 7/7 · D4 4/4 · D5 0/0 · D6 1/1
Puntos débiles: ninguno por fallos. Temas **fuera de los apuntes** que cayeron y conviene verificar en docs.databricks.com: MLflow Prompt Registry (`prompts:/…@alias`, `to_single_brace_format()`), data profiling (`MonitorInferenceLog` / `MonitorTimeSeries` / `MonitorSnapshot`), `VectorSearchRetrieverTool`, `mlflow.models.set_retriever_schema`, `RunnableParallel` para devolver fuentes.
Siguiente paso recomendado: volver a práctica: ejecutar el paso 3 de `04_ai_functions` (`ai_extract`), seguir con ai_summarize, ai_translate, ai_mask y cerrar M02 · B1.
Notas de procedimiento: en modo teoría las preguntas llegan como capturas; el procedimiento está en CLAUDE.md (explicar cada opción sin revelar, referencia a apuntes o "no aparece", preguntas guía).

## ESTADO – 19-nov-2026 (sesión 2)
Prácticas completadas: P1 en curso (🟡). Notebook `04_ai_functions`: paso 1 tabla `support_tickets` ✅ · paso 2 `ai_classify` v2.1 ✅ · paso 3 `ai_extract` escrito pero sin ejecutar. Faltan ai_extract, ai_summarize, ai_translate, ai_mask.
Lecciones cubiertas: M01 completa. M02: briefing ✅, A1–A2 ✅ (teoría + quiz), B1 🟡.
Recursos creados en el workspace (y si siguen activos): schema workspace.genai_cert, volume workspace.genai_cert.docs, tabla workspace.genai_cert.support_tickets (5 filas; sin coste, se mantienen).
Aciertos por dominio: D1 8/8 · D2 0/0 · D3 7/7 · D4 0/0 · D5 0/0 · D6 0/0
Puntos débiles: ninguno detectado. Repasado a petición: `map()` para options, `version` de las AI Functions y sintaxis de path de VARIANT (`:` `.` `[n]` `::`).
Siguiente paso recomendado: ejecutar el paso 3 (`ai_extract`), pegar un `extract_raw` y escribir los paths; luego ai_summarize, ai_translate, ai_mask → cerrar B1 con quiz y seguir con M02 · B2.

## ESTADO – 19-nov-2026 (sesión 1)
Prácticas completadas: P1 en curso (🟡): paso 1 schema + volume ✅ · paso 2 max_tokens/temperature con ai_query ✅ · paso 3 comparación de 3 modelos ✅. Falta M02 · B1 (AI Functions).
Lecciones cubiertas: M01 completa (teoría + quiz + glosario).
Recursos creados en el workspace (y si siguen activos): schema workspace.genai_cert, volume workspace.genai_cert.docs (sin coste, se mantienen). Git folder del repo.
Aciertos por dominio: D1 7/7 · D2 0/0 · D3 7/7 · D4 0/0 · D5 0/0 · D6 0/0
Puntos débiles: ninguno detectado aún. Recordar: temperature por defecto 0.0 en ai_query vs 1.0 en la REST API.
Siguiente paso recomendado: M02 · briefing y B1 AI Functions (P1 · notebook 04_ai_functions).

## ESTADO – 19-nov-2026 (reinicio)
Prácticas completadas: ninguna (empezamos de cero)
Lecciones cubiertas: ninguna (ver docs/coverage.md)
Recursos creados en el workspace (y si siguen activos): ninguno (se borra todo lo anterior)
Aciertos por dominio: D1 0/0 · D2 0/0 · D3 0/0 · D4 0/0 · D5 0/0 · D6 0/0
Puntos débiles: –
Siguiente paso recomendado: M01 · briefing de la lección y P1 (setup: schema + volume)

### Notas de entorno descubiertas (válidas aunque reiniciemos)
- Git folder del repo creada en el workspace (19-nov-2026): el código vive en `src/` (estructura por práctica P1–P9, config común en `src/00_common/config.py`). No hace falta volver a pedir que se cree.
- AI Playground: no se encuentra cómo cambiar max_tokens/temperature en la UI → los parámetros se prueban con `ai_query(..., modelParameters => named_struct(...))`.
- ai_query + responseFormat en estilo DDL: el esquema exige un único campo envoltorio (STRUCT<result:STRUCT<...>>), pero la respuesta llega sin el envoltorio y como STRING JSON. Se lee con res:campo o con from_json.
- ai_parse_document funciona en Free Edition (serverless). Llamado desde PySpark con F.expr("ai_parse_document(content, map('version','2.0'))").
- Spark muestra las rutas de volume como dbfs:/Volumes/... (equivale a /Volumes/...).
- ai_classify funciona en Free Edition (serverless). Doc actual (nov-2026): versión recomendada 2.1 → labels como JSON en STRING, options `map('version','2.1', ...)`, devuelve VARIANT `{"response":[{"value", "confidence_score"}]}`. Los apuntes usan la sintaxis v1 (`ARRAY(...)` → STRING). Lo mismo aplica a ai_extract (v2.1: schema JSON con tipos, cada campo `{"value": ...}`).
- Las AI Functions de tarea no permiten elegir modelo (lo gestiona Databricks). Facturación: ai_classify/ai_extract/ai_parse_document → AI_FUNCTIONS; ai_summarize/ai_translate/ai_mask → MODEL_SERVING (batch inference).
