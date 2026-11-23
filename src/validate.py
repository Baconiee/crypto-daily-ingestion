from datetime import datetime, timezone


def validate_data(data):
    expected_types = {
        "id": str,
        "symbol": str,
        "name": str,
        "image": str,
    }

    valid_rows = []
    rejected_rows = []

    for row in data:
        reasons = []

        for field, expected_type in expected_types.items():
            value = row.get(field)

            if value is None:
                reasons.append(f"{field} is missing or None")
                rejected_at = datetime.now(timezone.utc)
            elif not isinstance(value, expected_type):
                reasons.append(
                    f"{field} has invalid type. "
                    f"Expected {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
                rejected_at = datetime.now(timezone.utc)

        if reasons:
            rejected_rows.append({
                "raw_payload": row,                
                "reject_reason": "; ".join(reasons),
                "rejected_at": rejected_at
            })
        else:
            valid_rows.append(row)

    return valid_rows, rejected_rows, len(data)