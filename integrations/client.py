from deeploy import Client

workspace_id = 'b7bb2d93-12b4-49aa-b264-04aa41d09b1e'
deployment_id = '6df12424-dc91-4853-b5f8-d9d57d732be6'

client_options = {
    'deployment_token': 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68',
    # submitting actuals is currenly only
    # supported with the token auth method
    'host': 'fullorbit.deeploy.ml',
    'workspace_id': workspace_id,
}

client = Client(**client_options)


actuals_input = {
  "predictionIds": [
    "46485c7b-42ac-4488-9462-cf873ca396fc",
    "27647937-480f-4d07-b36f-d66f273c4029"
  ],
  "actualValues": [
    {"predictions": 1},
    {"predictions": 2},
  ]
}

client.actuals(deployment_id, actuals_input)