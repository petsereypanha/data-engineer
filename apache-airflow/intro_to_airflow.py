# Import the DAG object
from airflow import DAG
from datetime import datetime
import requests

# Define the default_args dictionary
default_args = {
  'owner': 'dsmith',
  'start_date': datetime(2023, 1, 14),
  'retries': 2
}


# Instantiate the DAG object
with DAG('example_etl', default_args=default_args) as etl_dag:
  pass

# Import the BashOperator
from airflow.operators.bash import BashOperator

with DAG(dag_id="test_dag", default_args={"start_date": "2024-01-01"}) as analytics_dag:
  # Define the BashOperator
  cleanup = BashOperator(
      task_id="cleanup_task",
      # Define the bash_command
      bash_command="cleanup.sh",
  )

# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh'
    )

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh'
    )


# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command='wget https://salestracking/latestinfo?json'
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data

# Define the method
def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
        f.write(r.content)
    # Use the print method for logging
    print(f"File pulled from {URL} and saved to {savepath}")

# Import the PythonOperator class
from airflow.operators.python import PythonOperator

# Create the task
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable (the function to execute)
    python_callable=pull_file,
    # Define the arguments for the 'pull_file' function using op_kwargs
    op_kwargs={
        'URL': 'http://dataserver/sales.json',
        'savepath': 'latestsales.json'
    }
)

# Add another Python task
parse_file_task = PythonOperator(
    task_id='parse_file',
    # Set the function to call
    python_callable=parse_file,
# Add the arguments
op_kwargs = {'inputfile': 'latestsales.json', 'outputfile': 'parsedfile.json'},
)

# Import the Operator
from airflow.operators.email import EmailOperator

# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task

