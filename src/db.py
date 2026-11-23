import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import Json, execute_values


load_dotenv()


def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

def start_run(conn, extracted_at):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO pipeline_runs (extracted_at) " \
            "VALUES (%s) " \
            "RETURNING run_id",
            (extracted_at,),
        )
        run_id = cur.fetchone()[0]
        conn.commit()

        return run_id

def load_bronze_layer_data(conn, run_id, payload):
    values = [(run_id, Json(row)) for row in payload]
    with conn.cursor() as cur:
        execute_values(
            cur,
            """
            INSERT INTO bronze_crypto_markets (run_id, payload) 
            VALUES %s
            """,
            values
        )
    conn.commit()
