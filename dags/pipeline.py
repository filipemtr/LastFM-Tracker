from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from dotenv import load_dotenv
from os import getenv

load_dotenv()


from datetime import datetime

with DAG(
    dag_id="lastfm_pipeline",
    start_date=datetime(2026, 5, 15),
    schedule="@daily",
    catchup=False
) as databricks_dag:
    
    run_job = DatabricksRunNowOperator(
        job_name="run_databricks_now",
        databricks_conn_id="databricks_default",
        job_id= getenv("job_id")
    )