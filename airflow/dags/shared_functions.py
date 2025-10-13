# receives the data from the API as a parameter and then loads data in the SQLite database using Airflow connection
import logging
import json
from airflow.hooks.base import BaseHook


def upsert_player_data(player_json):
    # we import here, because Airflow frequently parses DAG code and iwll reload imported libraries that are at the top of the Python file
    import sqlite3
    import pandas as pd

    # Fetch the connection object
    database_conn_id = "analytics_database"
    # Use Airflow connection which we defined in airflow admin connection panel, to retrieve connection
    connection = BaseHook.get_connection(database_conn_id)
    sqlite_db_path = connection.schema
    if player_json:
        player_data = json.loads(player_json)
        # Use a context manager for the SQLite connection
        with sqlite3.connect(sqlite_db_path) as conn:
            # Uses a database curose to execute SQL quieries on your analytics database
            cursor = conn.cursor()
            # Insert each player record into the 'player' table for player in player_data
            for player in player_data:
                try:
                    # Uses database cursor -> execute parameterized SQL query
                    # implemented with upsert capability -> updates a record if it already exists or insert if not
                    # Parameterized SQL query is an important measure to protect against SQL injection
                    cursor.execute(
                        """
                    INSERT INTO player (
                    player_id, gsis_id, first_name, last_name, position, last_changed_date
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(player_id) DO UPDATE SET
                    gsis_id = excluded.gsis_id,
                    first_name = excluded.first_name,
                    last_name = excluded.last_name,
                    position = excluded.position,
                    last_changed_date = excluded.last_changed_date
                    """,
                        (
                            player["player_id"],
                            player["gsis_id"],
                            player["first_name"],
                            player["last_name"],
                            player["position"],
                            player["last_changed_date"],
                        ),
                    )
                except Exception as e:
                    logging.error(f"Failed to insert player {player['player_id']}: {e}")
                    raise
    else:
        logging.warning("No player data found.")
        raise ValueError("No player data found. Task failed due to missing data.")
