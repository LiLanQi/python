from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "9bb5556a-4505-4259-b955-4d3fa05e0528",
    "object": {
      "type": "ITEM",
      "id": "#123456",
      "item_data": {
        "name": "qixi",
        "variations": [
          {
            "type": "ITEM_VARIATION",
            "id": "#12345",
            "item_variation_data": {
              "item_id": "#123456",
              "name": "baishi",
              "pricing_type": "FIXED_PRICING",
              "price_money": {
                "amount": 100,
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