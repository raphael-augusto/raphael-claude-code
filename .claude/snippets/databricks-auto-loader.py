"""
Databricks Auto Loader incremental ingestion
"""
from pyspark.sql import functions as F

# Auto Loader com schema inference e checkpoint
df_stream = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "parquet")
    .option("cloudFiles.schemaLocation", "/mnt/schemas/bronze/orders")
    .option("cloudFiles.inferColumnTypes", "true")
    .load("/mnt/landing/orders/")
    .withColumn("_ingestion_timestamp", F.current_timestamp())
    .withColumn("_source_file", F.input_file_name())
)

# Write to Delta Bronze
(
    df_stream.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/mnt/checkpoints/bronze/orders")
    .option("mergeSchema", "true")
    .partitionBy("partition_date")
    .start("/mnt/bronze/orders")
)
