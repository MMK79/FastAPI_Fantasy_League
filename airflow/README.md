Create a Bsic DAG within Airflow for better understanding of how we can automate the process of fetching data into the analytics system
* DAG file exist in dag folder
* Others folders are a map folders to docker compose of a Airflow
    * I needed to install Sqlite connection type by my self with executing `docker exec -it sh pip install sqlite_package_name` because the project was implemented on a airflow 2.1 but this is implemented on airflow 3.1
    * There are other differences too because of airflow versioning like there is no `schedule_interval` now it is `schedule`
