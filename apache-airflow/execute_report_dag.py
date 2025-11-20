from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

# --- Fixes applied here ---
# 1. Define the start date
DAG_START_DATE = datetime(2024, 1, 20)

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *",
    # FIX: Add a start_date to the DAG
    start_date = DAG_START_DATE,
    # BEST PRACTICE FIX: Set catchup=False
    catchup = False
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2024,1,20),
    mode='reschedule', # <-- FIXED: Switched from 'poke' to 'reschedule'
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    # Removed redundant start_date from task, as it inherits from the DAG
    dag=report_dag
)

precheck >> generate_report_task