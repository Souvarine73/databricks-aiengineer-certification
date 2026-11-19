# Progreso – Databricks GenAI Engineer Associate

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
