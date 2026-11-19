# Databricks notebook source
# MAGIC %md
# MAGIC # P1 · Paso 1 — Schema + Volume
# MAGIC Estructura de trabajo del proyecto: schema para tablas/funciones/modelos y volume para documentos no estructurados.

# COMMAND ----------

# MAGIC %run ../00_common/config

# COMMAND ----------

# Schema dentro del catálogo 'workspace' (en Free Edition no podemos crear catálogos)
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")

# Volume gestionado (managed): UC decide la ubicación física de los archivos
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")

# COMMAND ----------

# Comprobación: debe aparecer una fila con volume_name = docs
display(spark.sql(f"SHOW VOLUMES IN {CATALOG}.{SCHEMA}"))
