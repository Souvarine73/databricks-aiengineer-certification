# Progreso – Databricks GenAI Engineer Associate

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
