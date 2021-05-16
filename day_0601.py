result = client.catalog.upsert_catalog_object(
                body={
                    "idempotency_key": uuid,
                    "object": {
                        "type": "ITEM",
                        "id": "#hhhh",
                        "present_at_all_locations": True,
                        "item_data": {
                            "name": name,
                            "description": "hhyhhhhh",
                            "variations": [
                                {
                                    "type": "ITEM_VARIATION",
                                    "id": "#fgggg111",
                                    "item_variation_data": {
                                        "item_id": "#hhhh",
                                        "name": "gdfgfdgdfg",
                                        "pricing_type": "FIXED_PRICING",
                                        "price_money": {
                                            "amount": price,
                                            "currency": "USD"
                                        }
                                    }
                                }
                            ],
                            "product_type": "REGULAR"
                        }
                    }
                }
            )
    if result.is_success():
      print(result.body)
    elif result.is_error():
      print(result.errors)