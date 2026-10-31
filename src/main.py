from extract import extract_crypto_data


def main():
    try:
        crypto_data, extracted_at = extract_crypto_data()
        print(extracted_at)
    except:
        print("Some kind of error occured.")


if __name__ == "__main__":
    print("Hello, World!")
    main()