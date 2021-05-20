from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.catalog.upsert_catalog_object(
  body = {
    "idempotency_key": "2b12e0cb-d2fb-497a-af39-80ee0d2d9491",
    "object": {
      "type": "IMAGE",
      "id": "A5FNJMJVO7FUEYUUUKQI2LWO", #
      "version": 1621219910538,
      "image_data": {
        "name": "qixi",
        "url": "https://items-images-production.s3.us-west-2.amazonaws.com/files/e18ff41c6081099c87ac29afca0ecb8e7b2d0e0a/original.jpeg"
      }
    }
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)