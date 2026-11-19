# Progreso – Databricks GenAI Engineer Associate

## ESTADO – 19-nov-2026 (reinicio)
Prácticas completadas: ninguna (empezamos de cero)
Lecciones cubiertas: ninguna (ver docs/coverage.md)
Recursos creados en el workspace (y si siguen activos): ninguno (se borra todo lo anterior)
Aciertos por dominio: D1 0/0 · D2 0/0 · D3 0/0 · D4 0/0 · D5 0/0 · D6 0/0
Puntos débiles: –
Siguiente paso recomendado: M01 · briefing de la lección y P1 (setup: schema + volume)

### Notas de entorno descubiertas (válidas aunque reiniciemos)
- ai_query + responseFormat en estilo DDL: el esquema exige un único campo envoltorio (STRUCT<result:STRUCT<...>>), pero la respuesta llega sin el envoltorio y como STRING JSON. Se lee con res:campo o con from_json.
- ai_parse_document funciona en Free Edition (serverless). Llamado desde PySpark con F.expr("ai_parse_document(content, map('version','2.0'))").
- Spark muestra las rutas de volume como dbfs:/Volumes/... (equivale a /Volumes/...).
