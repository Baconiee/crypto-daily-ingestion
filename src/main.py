from extract import extract_crypto_data
from validate import validate_data
import requests


def main():
    try:
        crypto_data, extracted_at = extract_crypto_data()
        valid_crypto_data, invalid_crypto_data, total_data_amount = validate_data(crypto_data)
        print(total_data_amount)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Hello, World!")
    main()