from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

from datetime import datetime

with DAG(
    dag_id="lastfm_pipeline",
    start_date=datetime(2026, 5, 15),
    schedule="@daily",
    catchup=False
):
    
    run_job = DatabricksRunNowOperator(
        job_id=""
    )