import requests


token = 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/requestLogs/338fb733-5fb9-44d8-a825-3e7f9cacabc4/predictionLogs/838e506f-acf2-4273-ab9e-c8f79f30c96a/validations"

# Example
validation_input = {
    "result": 1,
    "value": {"predictions": [0]},
    "explanation": "example"
}

headers = {
    'Authorization': 'Bearer %s' % token,
}
response = requests.post(deployment_url, headers=headers, json=validation_input)
print(response)
validation_output = response.json()
print(validation_output)


