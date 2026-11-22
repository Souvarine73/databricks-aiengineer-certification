# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %run ../00_common/config

# COMMAND ----------

from pyspark.sql import functions as F

labels = '{"invoice": "bill with items, prices, totals, payment terms", "user_manual": "product instructions, safety, installation, troubleshooting", "contract": "legal agreement between parties", "other": "anything else"}'

df_docs = (
    spark.table(f"{CATALOG}.{SCHEMA}.doc_elements")
    .groupBy("path")
    .agg(F.sort_array(F.collect_list(F.struct("pos", "content"))).alias("items"))  # ordena por pos
    .withColumn("full_text", F.concat_ws("\n", F.col("items.content")))            # une los textos
    .drop("items")
)

df_classified = (
    df_docs
    .withColumn("cls", F.expr(f"""ai_classify(full_text, '{labels}', map('version','2.1','enableConfidenceScores','true'))"""))
    .withColumn("doc_type", F.expr("cls:response[0].value::string"))
    .withColumn("confidence", F.expr("cls:response[0].confidence_score::double"))
)
df_classified.select("path", "doc_type", "confidence").display()

df_classified.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.doc_classified")

# COMMAND ----------

display(df_classified)

# COMMAND ----------

schema = ('{"invoice_id": {"type": "string", "description": "invoice number, e.g. INV-2026-0457"}, '
          '"invoice_date": {"type": "string", "description": "date the invoice was issued"}, '
          '"due_date": {"type": "string", "description": "payment due date"}, '
          '"seller": {"type": "string", "description": "company issuing the invoice"}, '
          '"total_due": {"type": "number", "description": "final total amount due, with tax"}}')

df_invoices = (
    df_classified
    .where(F.col("doc_type") == "invoice")       # solo lo que el clasificador envió a "invoice"
    .withColumn("ext", F.expr(f"ai_extract(full_text, '{schema}', map('version','2.1'))"))
)

# Primero vemos la forma real del VARIANT, y después escribimos los paths
df_invoices.select("path", "ext").display()

# COMMAND ----------

df_invoice_fields = (
    df_invoices
    .select(
        "path",
        F.expr("ext:response.invoice_id.value::string").alias("invoice_id"),
        F.expr("ext:response.invoice_date.value::string").alias("invoice_date"),
        F.expr("ext:response.due_date.value::string").alias("due_date"),
        F.expr("ext:response.seller.value::string").alias("seller"),
        F.expr("ext:response.total_due.value::double").alias("total_due"),
    )
)

df_invoice_fields.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.invoice_fields")
df_invoice_fields.display()