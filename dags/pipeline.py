from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from dotenv import load_dotenv
import os

from datetime import datetime

with DAG(
    dag_id="lastfm_pipeline",
    start_date=datetime(2026, 5, 22),
    schedule="@daily",
    catchup=False
) as dag:
    
    run_job = DatabricksRunNowOperator(
        task_id="run_databricks_now",
        databricks_conn_id="databricks_default",
        job_id=int(os.getenv("JOB_ID")),
    )