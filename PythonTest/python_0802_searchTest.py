from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
#使用Search catalog objects进行前缀查询
result = client.catalog.search_catalog_objects(
  body = {
    "object_types": [
      "ITEM"
    ],
    "query": {
      "prefix_query": {
        "attribute_name": "name",
        "attribute_prefix": "hot"
      }
    }
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)