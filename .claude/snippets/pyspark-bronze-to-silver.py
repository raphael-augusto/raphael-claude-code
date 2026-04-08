"""
PySpark template Bronze → Silver com deduplicacao e data quality
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import logging
import json

# Structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

spark = SparkSession.builder.appName("bronze_to_silver").getOrCreate()

# AQE enabled
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

def bronze_to_silver(bronze_path: str, silver_path: str, partition_date: str):
    logger.info(json.dumps({
        'event': 'job_start',
        'bronze_path': bronze_path,
        'silver_path': silver_path,
        'partition_date': partition_date
    }))

    # Read bronze with filter (predicate pushdown)
    df_bronze = (
        spark.read
        .format("delta")
        .load(bronze_path)
        .filter(F.col("partition_date") == partition_date)
    )

    # Deduplication
    window_spec = Window.partitionBy("business_key").orderBy(F.col("updated_at").desc())

    df_silver = (
        df_bronze
        .withColumn("row_num", F.row_number().over(window_spec))
        .filter(F.col("row_num") == 1)
        .drop("row_num")
        .withColumn("processing_timestamp", F.current_timestamp())
    )

    # Data quality checks
    total_records = df_silver.count()
    null_keys = df_silver.filter(F.col("business_key").isNull()).count()

    if null_keys > 0:
        raise ValueError(f"Data quality failure: {null_keys} records with null business_key")

    # Write silver (idempotent with overwrite partition)
    (
        df_silver
        .write
        .format("delta")
        .mode("overwrite")
        .partitionBy("partition_date")
        .option("overwriteSchema", "false")
        .save(silver_path)
    )

    logger.info(json.dumps({
        'event': 'job_complete',
        'total_records': total_records,
        'partition_date': partition_date
    }))

if __name__ == "__main__":
    import sys
    bronze_to_silver(sys.argv[1], sys.argv[2], sys.argv[3])
