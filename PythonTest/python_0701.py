from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "af3d1afc-7212-4300-b463-0bfc5314a5a1",
    "object": {
      "type": "ITEM",
      "id": "#Cocoa",
      "item_data": {
        "name": "CocCC",
        "description": "Hot chocolate",
        "abbreviation": "Ch"
      }
    }
  }
)
if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)