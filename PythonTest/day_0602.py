from square.client import Client

client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "9c70e1ce-8973-4a47-a3a8-264a328072bd",
    "object": {
      "type": "ITEM",
      "id": "#hhhh",
      "present_at_all_locations": True,
      "item_data": {
        "name": "hhhhggg",
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
                "amount": 555,
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
