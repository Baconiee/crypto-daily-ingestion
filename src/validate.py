
def validate_data(data):
    required_fields = ["id", "symbol", "name", "image"]

    expected_types = {
        "id": str,
        "symbol": str,
        "name": str,
        "image": str
    }

    valid_crypto_data = []
    invalid_crypto_data = []

    for crypto_symbol in data:
        reason = ""

        for field in required_fields:
            if field not in crypto_symbol or crypto_symbol[field] is None:
                reason += f"{field} is missing or None\n"
                continue

            if not isinstance(crypto_symbol[field], expected_types[field]):
                reason += (
                    f"{field} has invalid type. "
                    f"Expected {expected_types[field].__name__}, "
                    f"got {type(crypto_symbol[field]).__name__}\n"
                )

        if reason:
            crypto_symbol["reason"] = reason
            invalid_crypto_data.append(crypto_symbol)
        else:
            valid_crypto_data.append(crypto_symbol)

    return valid_crypto_data, invalid_crypto_data, len(data)
