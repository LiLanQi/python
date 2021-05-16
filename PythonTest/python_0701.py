from square.client import Client
client = Client(access_token='保密')
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
