# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.genai_cert
# MAGIC   COMMENT 'Laboratorio certificación GenAI Engineer Associate';
# MAGIC
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.genai_cert.docs
# MAGIC   COMMENT 'Documentos fuente (PDF, etc.) para parsing y RAG';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ai_query(
# MAGIC   'databricks-meta-llama-3-3-70b-instruct',   -- endpoint (nombre legacy)
# MAGIC   'Explain in one sentence what RAG is.'       -- request
# MAGIC ) AS respuesta_endpoint;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ai_query(
# MAGIC   'system.ai.meta-llama-3-3-70b-instruct',     -- endpoint (model service)
# MAGIC   'Explain in one sentence what RAG is.'
# MAGIC ) AS respuesta_model_service;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   -- 1) Determinista: misma respuesta en cada ejecución
# MAGIC   ai_query(
# MAGIC     'system.ai.meta-llama-3-3-70b-instruct',
# MAGIC     'Write a one-sentence slogan for a data platform.',
# MAGIC     modelParameters => named_struct('temperature', 0.0, 'max_tokens', 60)
# MAGIC   ) AS temp_0,
# MAGIC
# MAGIC   -- 2) Creativa: debería cambiar en cada ejecución
# MAGIC   ai_query(
# MAGIC     'system.ai.meta-llama-3-3-70b-instruct',
# MAGIC     'Write a one-sentence slogan for a data platform.',
# MAGIC     modelParameters => named_struct('temperature', 1.0, 'max_tokens', 60)
# MAGIC   ) AS temp_1,
# MAGIC
# MAGIC   -- 3) Límite de tokens muy bajo: la respuesta saldrá cortada
# MAGIC   ai_query(
# MAGIC     'system.ai.meta-llama-3-3-70b-instruct',
# MAGIC     'Write a one-sentence slogan for a data platform.',
# MAGIC     modelParameters => named_struct('temperature', 0.0, 'max_tokens', 5)
# MAGIC   ) AS max_5_tokens;

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH reviews AS (                                    -- tabla temporal con 3 reseñas
# MAGIC   SELECT * FROM VALUES
# MAGIC     (1, 'The new X200 headphones are amazing, battery lasts forever!'),
# MAGIC     (2, 'My Z5 blender broke after two days. Terrible support.'),
# MAGIC     (3, 'The K9 keyboard is okay, a bit noisy but does the job.')
# MAGIC   AS t(id, review)
# MAGIC )
# MAGIC SELECT
# MAGIC   id,
# MAGIC   -- A) Solo prompt: le PEDIMOS JSON, pero no se lo imponemos
# MAGIC   ai_query(
# MAGIC     'system.ai.gpt-oss-20b',
# MAGIC     'Return JSON with fields sentiment (positive/negative/neutral) and product. Review: ' || review
# MAGIC   ) AS solo_prompt,
# MAGIC
# MAGIC   -- B) Con responseFormat: el esquema se IMPONE
# MAGIC   ai_query(
# MAGIC     'system.ai.gpt-oss-20b',
# MAGIC     'Extract the sentiment (positive/negative/neutral) and the product name from this review: ' || review,
# MAGIC     responseFormat => 'STRUCT<result:STRUCT<sentiment:STRING, product:STRING>>'
# MAGIC   ) AS con_response_format
# MAGIC FROM reviews;

# COMMAND ----------

from pyspark.sql import functions as F                 # alias estándar para las funciones de Spark

DOCS_PATH = "/Volumes/workspace/genai_cert/docs/"      # carpeta del volume con los PDF

df_raw = (
    spark.read.format("binaryFile")                    # cada archivo se lee como una fila con sus bytes
         .option("pathGlobFilter", "*.pdf")            # solo PDF (ignora otros archivos del volume)
         .load(DOCS_PATH)                              # ruta de la carpeta
)

df_raw.printSchema()                                   # comprueba que content es de tipo binary
display(df_raw.select("path", "length"))               # una fila por PDF (no mostramos content: son bytes)

# COMMAND ----------

# 1) Parsear: añade una columna VARIANT 'parsed' con la estructura de cada documento
df_parsed = (
    df_raw                                                        # DataFrame del paso 2 (path, content…)
    .withColumn(
        "parsed",
        F.expr("ai_parse_document(content, map('version', '2.0'))")  # AI Function SQL llamada desde PySpark
    )
    .select("path", "parsed")                                     # descartamos los bytes: ya no hacen falta
)

# 2) Persistir en Delta para no volver a pagar el parseo
(df_parsed.write
    .mode("overwrite")                                            # re-ejecutable sin duplicar filas
    .saveAsTable("workspace.genai_cert.parsed_docs"))             # tabla gestionada en Unity Catalog

# COMMAND ----------

parsed = spark.table("workspace.genai_cert.parsed_docs")         # leemos de Delta, sin volver a llamar al modelo

display(parsed.select(
    F.element_at(F.split("path", "/"), -1).alias("file"),          # solo el nombre del archivo
    F.expr("json_array_length(to_json(parsed:document:elements))") # cuántos elements ha detectado
        .alias("n_elements"),
    F.expr("parsed:error_status").alias("error_status")            # null o vacío = sin errores
))