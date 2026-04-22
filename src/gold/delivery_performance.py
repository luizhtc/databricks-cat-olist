# Databricks notebook source
from utils import read_from_silver
from pyspark.sql.functions import col, countDistinct, avg

# COMMAND ----------

orders = read_from_silver("orders")
order_items = read_from_silver("order_items")

# COMMAND ----------

order_items.join(
    orders,
    on="order_id",
    how="inner"
).select("order_id","seller_id","seller_state","delivery_delay_days","is_late").distinct().count()

# COMMAND ----------

orders.count()

# COMMAND ----------

order_items.groupby("seller_state").agg(
    countDistinct(col("order_id")).alias("total_orders")
).display()

# COMMAND ----------

orders.count()

# COMMAND ----------

order_items.display()

# COMMAND ----------


