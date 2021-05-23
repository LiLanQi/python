from square.client import Client
client = Client(access_token='EAAAEIl3awo49_UE8Is_9S0pAp2n_0-fIrDfgDnVoSZYU5_dD4ZhWbnPH534oBGh')
result = client.o_auth.obtain_token(
  body = {
    "client_id": "sandbox-sq0idb-Q3eThRMYq9IjGE3mPXhnGA",
    "client_secret": "sandbox-sq0csb-APPLICATION_SECRET_EXAMPLE",
    "code": "sandbox-AUTHORIZATION_CODE_EXAMPLE",
    "grant_type": "authorization_code"
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)