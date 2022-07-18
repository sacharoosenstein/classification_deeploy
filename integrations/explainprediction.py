import requests

token = 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/explain"

# Example: a batch prediction with two input tensors
model_input = {
    "instances": [
        [6, 3, 5, 1.4]
        ]
}

headers = {
    'Authorization': 'Bearer %s' % token,
}
response = requests.post(deployment_url, headers=headers, json=model_input)
model_output = response.json()

print(model_output)