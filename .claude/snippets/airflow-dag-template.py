"""
Airflow DAG template com best practices
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
import logging
import json

# Structured logging
logger = logging.getLogger(__name__)

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=30),
}

def extract(**context):
    logger.info(json.dumps({
        'event': 'extract_start',
        'dag_id': context['dag'].dag_id,
        'run_id': context['run_id'],
        'execution_date': str(context['execution_date'])
    }))
    # extraction logic
    return {'status': 'success', 'records': 1000}

with DAG(
    dag_id='bronze_to_silver_pipeline',
    default_args=default_args,
    description='Incremental pipeline Bronze → Silver',
    schedule_interval='0 2 * * *',  # 2 AM daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bronze', 'silver', 'bigquery'],
    max_active_runs=1,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract,
    )

    transform_task = BigQueryInsertJobOperator(
        task_id='transform_and_load',
        configuration={
            'query': {
                'query': '{% include "sql/bronze_to_silver.sql" %}',
                'useLegacySql': False,
            }
        },
    )

    extract_task >> transform_task
