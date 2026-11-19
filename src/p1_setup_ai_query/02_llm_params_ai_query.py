# Databricks notebook source
# MAGIC %md
# MAGIC # P1 · Paso 2 — Parámetros del LLM con `ai_query` (M01 · B2, p. 3)
# MAGIC - `max_tokens`: límite de tokens de salida (el modelo deja de predecir, no "termina la idea").
# MAGIC - `temperature`: 0 = determinista; más alta = más variabilidad. **En `ai_query` el default es 0.0** (en la REST API es 1.0).
# MAGIC - Los valores de `modelParameters` tienen que ser constantes, no dependientes de los datos.
# MAGIC
# MAGIC SQL equivalente:
# MAGIC `SELECT ai_query('system.ai.meta-llama-3-3-70b-instruct', 'Explain...', modelParameters => named_struct('max_tokens', 10))`

# COMMAND ----------

# MAGIC %run ../00_common/config

# COMMAND ----------

from pyspark.sql import functions as F

# DataFrame de una fila con el prompt
df = spark.createDataFrame([("Explain what makes an app agentic.",)], ["prompt"])

result = (
    df
    # a) Corte por max_tokens: el modelo deja de predecir al llegar a 10 tokens
    .withColumn("short_10_tokens", F.expr(f"""
        ai_query('{CHAT_MODEL}', prompt,
                 modelParameters => named_struct('max_tokens', 10))"""))
    # b) temperature 0 dos veces: deberían salir (casi) iguales
    .withColumn("temp0_run1", F.expr(f"""
        ai_query('{CHAT_MODEL}', prompt,
                 modelParameters => named_struct('max_tokens', 60, 'temperature', 0.0))"""))
    .withColumn("temp0_run2", F.expr(f"""
        ai_query('{CHAT_MODEL}', prompt,
                 modelParameters => named_struct('max_tokens', 60, 'temperature', 0.0))"""))
    # c) temperature alta: más variabilidad en la elección del siguiente token
    .withColumn("temp15", F.expr(f"""
        ai_query('{CHAT_MODEL}', prompt,
                 modelParameters => named_struct('max_tokens', 60, 'temperature', 1.5))"""))
)

display(result)
