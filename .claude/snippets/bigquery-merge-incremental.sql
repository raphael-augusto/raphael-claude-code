-- BigQuery incremental MERGE pattern
-- Bronze → Silver deduplication with SCD Type 2

MERGE `project.dataset.silver_table` AS target
USING (
  SELECT
    business_key,
    attribute1,
    attribute2,
    updated_at,
    ROW_NUMBER() OVER (PARTITION BY business_key ORDER BY updated_at DESC) AS rn
  FROM `project.dataset.bronze_table`
  WHERE DATE(ingestion_timestamp) = CURRENT_DATE()  -- incremental filter
) AS source
ON target.business_key = source.business_key AND source.rn = 1
WHEN MATCHED AND target.updated_at < source.updated_at THEN
  UPDATE SET
    attribute1 = source.attribute1,
    attribute2 = source.attribute2,
    updated_at = source.updated_at
WHEN NOT MATCHED THEN
  INSERT (business_key, attribute1, attribute2, updated_at)
  VALUES (source.business_key, source.attribute1, source.attribute2, source.updated_at);
