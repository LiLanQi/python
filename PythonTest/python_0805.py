from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "9f7ac878-d1dd-4281-be90-66488ef606cb",
    "object": {
      "type": "ITEM",
      "id": "#121212",
      "version": 1621219910538,
      "image_id": "A5FNJMJVO7FUEYUUUKQI2LWO",
      "item_data": {
        "name": "chocolate",
        "variations": [
          {
            "type": "ITEM_VARIATION",
            "id": "#1234",
            "item_variation_data": {
              "item_id": "#121212",
              "name": "dilicious chocolate",
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