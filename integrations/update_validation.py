import requests

token = 'ZOCN768pimcCrxWy6VyXiGrQARrzIPfuC7rKWJ68'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/6df12424-dc91-4853-b5f8-d9d57d732be6/requestLogs/dea7dec6-8ea1-41fb-9495-dd8ef2d90f60/predictionLogs/a6328d4e-576f-408b-97c3-872bd7a39eaf/validations/019501fd-30e7-430f-a1fc-23a20c0ceec4"

# Example
validation_input = {
    "result": 0,
    "value": {"predictions": [2]},
    "explanation": "new explanation"
}

headers = {
    'Authorization': 'Bearer %s' % token,
}
response = requests.patch(deployment_url, headers=headers, json=validation_input)
validation_output = response.json()
    