# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %run ../00_common/config

# COMMAND ----------

import time
from pyspark.sql import functions as F

# Pregunta con trampa: la respuesta intuitiva (0.10) es incorrecta; la correcta es 0.05
prompt = ("A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. "
          "How much does the ball cost? Answer with just the number.")
df = spark.createDataFrame([(prompt,)], ["prompt"])

models = [
    "system.ai.meta-llama-3-3-70b-instruct",   # grande
    "system.ai.qwen3-next-80b-a3b-instruct",   # MoE: 80B totales, ~3B activos por token
    "system.ai.gemma-3-12b",                   # pequeño y barato
]

rows = []
for m in models:
    start = time.time()
    # collect() fuerza la ejecución (Spark es lazy): así medimos la llamada real
    answer = (df.withColumn("answer", F.expr(f"""
                  ai_query('{m}', prompt,
                           modelParameters => named_struct('max_tokens', 50, 'temperature', 0.0))"""))
                .select("answer").collect()[0]["answer"])
    rows.append((m, answer, round(time.time() - start, 1)))

display(spark.createDataFrame(rows, ["model", "answer", "latency_s"]))