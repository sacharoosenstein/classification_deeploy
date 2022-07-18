import requests

token = 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/predict"


# Example: a batch prediction with two input tensors
model_input = {
    "instances": [
        [6, 3, 5, 1.4],
        [6.2, 3.4, 4, 1.6],
        [6.2, 3.4, 4.5, 1],
        [6.2, 4, 4.5, 1.6],
        [6.2, 3, 4.5, 1.6],
        [3, 3.4, 4.5, 1.6]
        ]
}

headers = {
    'Authorization': 'Bearer %s' % token,
}

response = requests.post(deployment_url, headers=headers, json=model_input)
model_output = response.json()
print(model_output)

deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/requestLogs"
response = requests.get(deployment_url, headers=headers)
logs = response.json()
print(logs)

deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/explain"

# Example: a batch prediction with two input tensors
model_input = {
"instances": [
    [6, 3, 5, 1.4],
    [6.2, 3.4, 4, 1.6],
    [6.2, 3.4, 4.5, 1],
    [6.2, 4, 4.5, 1.6],
    [6.2, 3, 4.5, 1.6],
    [3, 3.4, 4.5, 1.6]
    ]
}

headers = {
    'Authorization': 'Bearer %s' % token,
}

response = requests.post(deployment_url, headers=headers, json=model_input)
model_output = response.json()