# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %run ../00_common/config

# COMMAND ----------

# Paso 1 · Tabla de tickets (5 filas con temas, idiomas y PII mezclados)
tickets = [
    (1, "I was charged twice for order #4521. Please refund. Contact: john.smith@mail.com"),
    (2, "My package has been stuck in Madrid for 10 days, tracking ES99887766."),
    (3, "The app crashes every time I upload a PDF larger than 5MB on Android 14."),
    (4, "Me han cobrado 49,99 EUR sin haber pedido nada. Mi teléfono es 612 345 678."),
    (5, "Order #7788 arrived damaged and the invoice shows the wrong VAT number."),
]

df = spark.createDataFrame(tickets, ["ticket_id", "body"])  # el esquema se infiere de las tuplas
df.write.mode("overwrite").saveAsTable(f"{CATALOG}.{SCHEMA}.support_tickets")

display(spark.table(f"{CATALOG}.{SCHEMA}.support_tickets"))

# COMMAND ----------

# Paso 2 · ai_classify v2.1 (labels como JSON en un STRING; devuelve VARIANT)
# SQL v1 (legacy, como en los apuntes): SELECT ai_classify(body, ARRAY('billing','shipping','technical')) FROM support_tickets;
from pyspark.sql import functions as F

tickets = spark.table(f"{CATALOG}.{SCHEMA}.support_tickets")

# Labels con descripción (v2.x): ayudan a distinguir categorías ambiguas
labels = '{"billing": "charges, refunds, invoices, VAT", "shipping": "delivery, tracking, damaged packages", "technical": "app errors, crashes, bugs"}'

classified = (tickets
    .withColumn("topic_raw", F.expr(f"""
        ai_classify(body, '{labels}',
                    map('version', '2.1', 'enableConfidenceScores', 'true'))"""))  # VARIANT
    # Path de VARIANT: ':' entra, '.' baja, '[n]' indexa, '::' castea
    .withColumn("topic", F.expr("topic_raw:response[0].value::string"))
    .withColumn("confidence", F.expr("topic_raw:response[0].confidence_score::double"))
)

display(classified.select("ticket_id", "body", "topic", "confidence", "topic_raw"))
# Resultado (19-nov-2026): 1 billing 0.85 · 2 shipping 0.93 · 3 technical 0.92 · 4 billing 0.94 · 5 shipping 0.6 (ambiguo)

# COMMAND ----------

# Paso 3 · ai_extract v2.1 (PENDIENTE: siguiente sesión)
schema = ('{"order_id": {"type": "string", "description": "order number, without #"}, '
          '"amount": {"type": "number", "description": "money amount mentioned, if any"}, '
          '"language": {"type": "enum", "labels": ["en", "es", "other"]}}')

extracted = classified.withColumn("extract_raw", F.expr(f"ai_extract(body, '{schema}', map('version', '2.1'))"))

# Primero ver la forma real del VARIANT, luego escribir los paths
display(extracted.select("ticket_id", "body", "extract_raw"))
