from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

sample_dag = DAG(
    dag_id = 'sample_dag',
    schedule_interval = "0 0 * * *"
)

sample_task = BashOperator(
    task_id='sample',
    bash_command='generate_sample.sh',
    start_date=datetime(2023,2,20),
    dag=sample_dag
)
