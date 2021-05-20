from square.client import Client
# 图片上传
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
file_to_upload_path = "C:\\Users\\Administrator\\Desktop\\837291da0e9a9bd5c6a9a1ebca8925c7.jpg"
f_stream = open(file_to_upload_path, "rb")

result = client.catalog.create_catalog_image(
  request = {
    "idempotency_key": "708cbe00-32f7-47c8-abc3-aa68d78433d3",
    "image": {
      "type": "IMAGE",
      "id": "#1042520531",
      "image_data": {
        "name": "the picture of qixi",
        "caption": "very dilicious"
      }
    }
  },
  image_file = f_stream
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)