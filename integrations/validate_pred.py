import requests


token = 'yFjkjNUhHmf4I1Z2yZl3n6ZSj7L2G4RyU61wuzwq'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/71099933-bdf5-4765-abed-ccb54a3b5796/requestLogs/d5fafece-4e57-47e2-aab8-e5dab4f7d3d5/predictionLogs/c5274b59-1e43-42ec-8d62-0e00b8206a86/validations"

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


