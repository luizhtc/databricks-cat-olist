# Databricks notebook source
from pyspark.sql.functions import col
from utils import read_from_bronze, parse_timestamp

# COMMAND ----------

reviews = read_from_bronze("tbl_olist_order_reviews_dataset")

# COMMAND ----------

reviews.display()

# COMMAND ----------

reviews_select =\
reviews.select(
    "review_id",
    "order_id",
    "review_score",
    "review_comment_title",
    "review_comment_message",
    parse_timestamp(col("review_creation_date")).alias("review_creation_date"),
    parse_timestamp(col("review_answer_timestamp")).alias("review_answer_timestamp")
)

# COMMAND ----------

reviews_select.display()

# COMMAND ----------


