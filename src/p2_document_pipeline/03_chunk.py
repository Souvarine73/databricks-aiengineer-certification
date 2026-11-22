# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %run ../00_common/config

# COMMAND ----------

from pyspark.sql import functions as F

# Solo el manual, para limitar coste mientras probamos
df_manual = (
    spark.table(f"{CATALOG}.{SCHEMA}.parsed_docs")
    .where(F.col("path").contains("manual"))
    .select("path", F.expr("ai_prep_search(parsed_content)").alias("result"))  # VARIANT, 1 fila
)

# Primero vemos la forma real del VARIANT, y después escribimos los paths
df_manual.display()

# COMMAND ----------

chunks = (
    spark.table(f"{CATALOG}.{SCHEMA}.parsed_docs")
    .select("path", F.expr("ai_prep_search(parsed_content)").alias("result"))
    .select(
        "path",
        F.explode(F.expr("variant_get(result, '$.document.contents', 'array<variant>')")).alias("chunk"),  # 1 fila por chunk
    )
    .select(
        "path",
        F.expr("chunk:chunk_id::string").alias("chunk_id"),
        F.expr("chunk:chunk_position::int").alias("chunk_position"),
        F.expr("chunk:chunk_to_embed::string").alias("chunk_to_embed"),
        F.expr("chunk:chunk_to_retrieve::string").alias("chunk_to_retrieve"),
    )
)

# Metadato del paso 4: tipo de documento, para filtrar luego en la búsqueda
doc_type = spark.table(f"{CATALOG}.{SCHEMA}.doc_classified").select("path", "doc_type")
chunks = chunks.join(doc_type, "path", "left")

chunks.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.chunks")

# CDF: requisito para un Delta Sync index (E2). SQL equivalente = esta misma sentencia.
spark.sql(f"ALTER TABLE {CATALOG}.{SCHEMA}.chunks SET TBLPROPERTIES (delta.enableChangeDataFeed = true)")

display(spark.table(f"{CATALOG}.{SCHEMA}.chunks").select("path", "chunk_id", "chunk_position", "doc_type"))