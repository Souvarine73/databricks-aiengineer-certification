# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %run ../00_common/config

# COMMAND ----------

df_raw = (
    spark.read.format("binaryFile")
    .option("pathGlobFilter", "*.pdf")
    .load(VOLUME_PATH)
)
df_raw.select("path", "length", "modificationTime").display()

# COMMAND ----------

from pyspark.sql import functions as F

df_parsed = df_raw.select(
    "path",
    F.expr("ai_parse_document(content, map('version', '2.0'))").alias("parsed_content"),  # VARIANT
)

# La guardamos en Delta para no repetir el parseo (cuesta cómputo) en los pasos siguientes
df_parsed.write.mode("overwrite").option("mergeSchema", "true").saveAsTable(f"{CATALOG}.{SCHEMA}.parsed_docs")


# COMMAND ----------

# Inspección: path, nº de elementos y estado de error de cada documento
spark.table(f"{CATALOG}.{SCHEMA}.parsed_docs").select(
    "path",
    F.expr("parsed_content:error_status").alias("error_status"),
    F.expr("variant_get(parsed_content, '$.document.elements', 'array<variant>')").alias("elements"),
).select("path", "error_status", F.size("elements").alias("n_elements")).display()

# COMMAND ----------

elements = (
    spark.table(f"{CATALOG}.{SCHEMA}.parsed_docs")
    .where(F.col("path").contains("invoice"))
    .select(
        "path",
        F.posexplode(
            F.expr("variant_get(parsed_content, '$.document.elements', 'array<variant>')")
        ).alias("pos", "element"),   # una fila por elemento: posición + VARIANT
    )
)
elements.display()

# COMMAND ----------

noise = ["page_header", "page_footer", "page_number"]  # tipos que descartamos

df_elements = (
    spark.table(f"{CATALOG}.{SCHEMA}.parsed_docs")
    .select(
        "path",
        F.posexplode(
            F.expr("variant_get(parsed_content, '$.document.elements', 'array<variant>')")
        ).alias("pos", "element"),
    )
    .select(
        "path",
        "pos",
        F.expr("element:type::string").alias("type"),        # ':' navega el VARIANT, '::' hace cast
        F.expr("element:content::string").alias("content"),
    )
    .where(~F.col("type").isin(noise))                        # filtra el ruido
)

df_elements.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.doc_elements")
df_elements.groupBy("path", "type").count().orderBy("path", "type").display()