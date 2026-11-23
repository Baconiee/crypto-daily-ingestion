from extract import extract_crypto_data
from validate import validate_data
from transform import transform_to_silver_layer
from db import get_connection, start_run, load_bronze_layer_data, load_silver_layer_data
import requests


def main():
    try:
        crypto_data, extracted_at = extract_crypto_data()
        valid_crypto_data, invalid_crypto_data, total_data_amount= validate_data(crypto_data)
        conn = get_connection()
        run_id = start_run(conn, extracted_at)
        load_bronze_layer_data(conn, run_id, valid_crypto_data)
        transformed_data = transform_to_silver_layer(valid_crypto_data, run_id)
        load_silver_layer_data(conn, transformed_data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Hello, World!")
    main()