-- Snowflake Stream + Task CDC pattern

-- Create stream to capture changes
CREATE OR REPLACE STREAM bronze_stream ON TABLE bronze.orders
  SHOW_INITIAL_ROWS = FALSE;

-- Create task to process CDC
CREATE OR REPLACE TASK process_bronze_to_silver
  WAREHOUSE = transform_wh
  SCHEDULE = '5 MINUTE'
  WHEN SYSTEM$STREAM_HAS_DATA('bronze_stream')
AS
MERGE INTO silver.orders AS target
USING (
  SELECT
    order_id,
    customer_id,
    order_date,
    total_amount,
    METADATA$ACTION AS dml_action,
    METADATA$ISUPDATE AS is_update
  FROM bronze_stream
  QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY METADATA$ACTION DESC) = 1
) AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.dml_action = 'DELETE' THEN DELETE
WHEN MATCHED AND source.dml_action = 'INSERT' AND source.is_update = TRUE THEN
  UPDATE SET
    customer_id = source.customer_id,
    order_date = source.order_date,
    total_amount = source.total_amount,
    updated_at = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN
  INSERT (order_id, customer_id, order_date, total_amount, created_at)
  VALUES (source.order_id, source.customer_id, source.order_date, source.total_amount, CURRENT_TIMESTAMP());

-- Enable task
ALTER TASK process_bronze_to_silver RESUME;
