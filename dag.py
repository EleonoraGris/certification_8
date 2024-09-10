from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

# Определение стандартных аргументов для DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Определение DAG
with DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG with two operators',
    schedule_interval='45 12 * * *',  # Ежедневный запуск в 12:45 по Москве
    start_date=datetime(2024, 9, 10),
    catchup=False,
) as dag:

    # Создание двух операторов (задач)
    task_1 = DummyOperator(
        task_id='start'
    )

    task_2 = DummyOperator(
        task_id='end'
    )

    # Определение последовательности задач
    task_1 >> task_2

