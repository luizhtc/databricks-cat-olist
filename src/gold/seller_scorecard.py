# Databricks notebook source
from utils import read_from_silver
from pyspark.sql.functions import col, countDistinct, sum as _sum

# COMMAND ----------

orders = read_from_silver("order")
order_items = read_from_silver("order_items")
reviews = read_from_silver("reviews")

# COMMAND ----------

order_items.groupby("seller_id","seller_state").agg(
    countDistinct(col("order_id")).alias("total_orders"),
    _sum(col("price")).alias("total_revenue")
).display()

# COMMAND ----------

reviews.display()

# COMMAND ----------


