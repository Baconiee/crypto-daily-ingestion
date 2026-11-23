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

def load_silver_layer_data(conn, silver_rows):
    cols = [
        "run_id", "coin_id", "symbol", "name", "current_price",
        "market_cap", "market_cap_rank", "fully_diluted_valuation",
        "total_volume", "high_24h", "low_24h", "price_change_24h",
        "price_change_percentage_24h", "market_cap_change_24h",
        "market_cap_change_percentage_24h", "circulating_supply",
        "total_supply", "max_supply", "ath", "ath_change_percentage",
        "ath_date", "atl", "atl_change_percentage", "atl_date",
        "last_updated",
    ]

    values = [tuple(row[col] for col in cols) for row in silver_rows]

    with conn.cursor() as cur:
        execute_values(
            cur,
            f"""
            INSERT INTO silver_crypto_market_snapshots ({", ".join(cols)})
            VALUES %s   
            """,
            values
        )

    conn.commit()

