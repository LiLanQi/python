from square.client import Client

client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
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