import requests

token = '6A3w8tvW5eH455Xbq7wHsU2UoyPs9CzZhilMzxd1'
deployment_url = "https://api.fullorbit.deeploy.ml/v2/workspaces/b7bb2d93-12b4-49aa-b264-04aa41d09b1e/deployments/4045449e-5545-4168-96d4-2675d3745bf8/requestLogs/<REQUEST_LOG_ID>/predictionLogs/<PREDICTION_LOG_ID>/validations"

# Example
validation_input = {
    "result": 1,
    "value": {"output": [6.8, 2.8, 4.8, 1.4]},
    "explanation": "<YOUR_EXPLANATION>"
}

headers = {
    'Authorization': 'Bearer %s' % token,
}
response = requests.post(deployment_url, headers=headers, json=validation_input)
validation_output = response.json()