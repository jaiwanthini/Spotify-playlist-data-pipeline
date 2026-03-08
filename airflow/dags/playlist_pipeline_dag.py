from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# allow airflow to import project files
sys.path.append("/opt/airflow")

from src.extract import fetch_playlist_data
from src.transform import transform_data
from src.load import save_raw, save_transformed


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

dag = DAG(
    dag_id="playlist_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
)

# Task 1: Extract
def extract_task(**context):
    df = fetch_playlist_data()
    context["ti"].xcom_push(key="raw_data", value=df.to_json())

# Task 2: Transform
def transform_task(**context):
    import pandas as pd

    raw_json = context["ti"].xcom_pull(key="raw_data")
    df = pd.read_json(raw_json)

    df_transformed = transform_data(df)

    context["ti"].xcom_push(key="transformed_data", value=df_transformed.to_json())

# Task 3: Load
def load_task(**context):
    import pandas as pd

    raw_json = context["ti"].xcom_pull(key="raw_data")
    transformed_json = context["ti"].xcom_pull(key="transformed_data")

    df_raw = pd.read_json(raw_json)
    df_transformed = pd.read_json(transformed_json)

    save_raw(df_raw)
    save_transformed(df_transformed)


extract = PythonOperator(
    task_id="extract_data",
    python_callable=extract_task,
    dag=dag,
)

transform = PythonOperator(
    task_id="transform_data",
    python_callable=transform_task,
    dag=dag,
)

load = PythonOperator(
    task_id="load_data",
    python_callable=load_task,
    dag=dag,
)

extract >> transform >> load