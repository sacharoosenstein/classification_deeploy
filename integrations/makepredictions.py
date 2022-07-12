import requests

token = 'yFjkjNUhHmf4I1Z2yZl3n6ZSj7L2G4RyU61wuzwq'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/71099933-bdf5-4765-abed-ccb54a3b5796/predict"

# Example: a batch prediction with two input tensors
model_input = {
    "instances": [
        [6, 3, 5, 1.4],
        [6.2, 3.4, 4.5, 1.6]
        ]
}

headers = {
    'Authorization': 'Bearer %s' % token,
}

response = requests.post(deployment_url, headers=headers, json=model_input)
model_output = response.json()
print(model_output)

deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/71099933-bdf5-4765-abed-ccb54a3b5796/requestLogs"
response = requests.get(deployment_url, headers=headers)
logs = response.json()
print(logs)

