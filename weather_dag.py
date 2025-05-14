from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from weather_etl import run_openweather_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule=timedelta(days=1),  # fixed key: should be `schedule_interval`
)
run_etl = PythonOperator(
    task_id='complete_openWeather_etl',
    python_callable=run_openweather_etl,
    dag=dag, 
)
run_etl
