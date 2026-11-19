# Databricks notebook source
# Configuración común del proyecto. Úsala en cada notebook con: %run ../00_common/config

CATALOG = "workspace"
SCHEMA = "genai_cert"
VOLUME = "docs"
VOLUME_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"

CHAT_MODEL = "system.ai.meta-llama-3-3-70b-instruct"   # principal
CHEAP_MODEL = "system.ai.gpt-oss-20b"                  # barato
EMBEDDING_MODEL = "system.ai.gte-large-en"
