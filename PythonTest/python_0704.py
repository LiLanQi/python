from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
file_to_upload_path = "D:\\180.jpg" # Modify this to point to your desired file.
f_stream = open(file_to_upload_path, "rb")

result = client.catalog.create_catalog_image(
  request = {
    "idempotency_key": "1743bfa0-cc55-41ac-9895-8def9618f0f5",
    "object_id": "ZFVW6BVHWKQIWFRW5C6UPJH2",
    "image": {
      "type": "IMAGE",
      "id": "#12345",
      "image_data": {
        "name": "chocolatePic"
      }
    }
  },
  file = f_stream
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)