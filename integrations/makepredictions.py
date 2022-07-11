import requests

token = 'Y9bSXem68DRJOELqMJegvGAiVaMvUQNsgtmygQNb'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/4045449e-5545-4168-96d4-2675d3745bf8/predict"

# Example: a batch prediction with two input tensors
model_input = {
    "instances": [
        [6.8, 2.8, 4.8, 1.4],
        [6.0, 3.4, 4.5, 1.6]
        ]
}

headers = {
    'Authorization': 'Bearer %s' % token,
}

response = requests.post(deployment_url, headers=headers, json=model_input)
model_output = response.json()
print(model_output)

deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/4045449e-5545-4168-96d4-2675d3745bf8/requestLogs"
response = requests.get(deployment_url, headers=headers)
logs = response.json()
print(logs)

