# Databricks notebook source
df = spark.read.table("cat_olist.sch_bronze.tbl_olist_order_reviews_dataset")

# COMMAND ----------

df.display()
