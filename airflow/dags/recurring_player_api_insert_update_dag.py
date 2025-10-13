import datetime
import logging

# Enable define the DAG using a @dag decorator
from airflow.decorators import dag

# Enable use predefined operators
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.python import PythonOperator

# another python file with shared_functions between 2 DAGs
from shared_functions import upsert_player_data


# first task of the DAG = verfiy the status of API before proceeding with other tasks
def health_check_response(response):
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response body: {response.text}")
    return response.status_code == 200 and response.json() == {
        "message": "API health check successful"
    }


# will be called by a task
def insert_update_player_data(**context):
    # using XCom to retrieve data from the second task
    player_json = context["ti"].xcom_pull(task_ids="api_player_query")
    if player_json:
        # passes the data from XCom to the shared upsert_player_data function
        upsert_player_data(player_json)
    else:
        logging.warning("No player data found.")


# @dag(schedule=None)
@dag(start_date=datetime.datetime(2024, 8, 7), schedule=None, catchup=False)
def recurring_player_api_insert_update_dag():
    api_health_check_task = HttpOperator(
        task_id="check_api_health_check_endpoint",
        http_conn_id="sportsworldcentral_url",
        endpoint="/",
        method="GET",
        headers={"Content-Type": "application/json"},
        response_check=health_check_response,
    )

    temp_min_last_change_date = "2024-04-01"

    api_player_query_task = HttpOperator(
        task_id="api_player_query",
        http_conn_id="sportsworldcentral_url",
        endpoint=(
            f"/v0/players/?skip=0&limit=100000&minimum_last_changed_date="
            f"{temp_min_last_change_date}"
        ),
        method="GET",
        headers={"Content-Type": "application/json"},
    )

    player_sqlite_upsert_task = PythonOperator(
        task_id="player_sqlite_upsert",
        python_callable=insert_update_player_data,
    )

    # Run order of tasks, set dependency between tasks, using bitshift operators
    api_health_check_task >> api_player_query_task >> player_sqlite_upsert_task


# Instantiate the DAG
dag_instance = recurring_player_api_insert_update_dag()
