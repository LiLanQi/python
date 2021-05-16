from square.client import Client
client = Client(access_token='保密')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "789b8fa6-ac69-4a59-9063-fc111619e1a2",
    "object": {
      "type": "ITEM",
      "id": "#123456789",
      "item_data": {
        "name": "Chocolate",
        "variations": [
          {
            "type": "ITEM_VARIATION",
            "id": "#1234567890",
            "item_variation_data": {
              "item_id": "#123456789",
              "name": "chocolate",
              "pricing_type": "FIXED_PRICING",
              "price_money": {
                "amount": 100,
                "currency": "USD"
              }
            },
            "image_data": {
              "name": "chocolatePic",
              "url": "https://s.yimg.com/ny/api/res/1.2/hnfLqfNnAXrRxDQO51EUkQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY0MC4zMjtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/rQ3DlO1sy0BiCbV61D2t2Q--~B/aD02Njc7dz0xMDAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/ko/cnews.com.tw/837291da0e9a9bd5c6a9a1ebca8925c7",
              "caption": "dilicious"
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
