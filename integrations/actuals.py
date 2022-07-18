import requests

token = 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/actuals"


headers = {
    'Authorization': 'Bearer %s' % token,
}

actuals_input = {
  "predictionIds": ['9bb42469-188b-43d3-adc1-6684f4b17f6f', '05c15be7-60c2-4892-a585-45d0d6f52568', '3d2e1b0c-341d-4725-9703-c088b2c12296', 'ee89dbc1-31f2-4ce9-b941-c912bb562670', '07376d0e-7845-4bc1-8ce6-a70e10dc9c92', '838e506f-acf2-4273-ab9e-c8f79f30c96a'],
  "actualValues": [
    {"predictions": [1]},
    {"predictions": [1]},
    {"predictions": [1]},
    {"predictions": [1]},
    {"predictions": [1]},
    {"predictions": [1]}
  ]
}
response = requests.put(deployment_url, headers=headers, json=actuals_input)
print(response)


