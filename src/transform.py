def transform_to_silver_layer(data, run_id):
    transformed_data = []
    for crypto in data:
        transformed_data.append({
            "run_id": run_id,
            "coin_id": crypto["id"],
            "symbol": crypto["symbol"].upper(),
            "name": crypto.get("name"),
            "current_price": crypto.get("current_price"),
            "market_cap": crypto.get("market_cap"),
            "market_cap_rank": crypto.get("market_cap_rank"),
            "fully_diluted_valuation": crypto.get("fully_diluted_valuation"),
            "total_volume": crypto.get("total_volume"),
            "high_24h": crypto.get("high_24h"),
            "low_24h": crypto.get("low_24h"),
            "price_change_24h": crypto.get("price_change_24h"),
            "price_change_percentage_24h": crypto.get("price_change_percentage_24h"),
            "market_cap_change_24h": crypto.get("market_cap_change_24h"),
            "market_cap_change_percentage_24h": crypto.get("market_cap_change_percentage_24h"),
            "circulating_supply": crypto.get("circulating_supply"),
            "total_supply": crypto.get("total_supply"),
            "max_supply": crypto.get("max_supply"),
            "ath": crypto.get("ath"),
            "ath_change_percentage": crypto.get("ath_change_percentage"),
            "ath_date": crypto.get("ath_date"),
            "atl": crypto.get("atl"),
            "atl_change_percentage": crypto.get("atl_change_percentage"),
            "atl_date": crypto.get("atl_date"),
            "last_updated": crypto["last_updated"],
        })

    return transformed_data