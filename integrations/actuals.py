from deeploy import Client
from deeploy import DeployOptions
from deeploy.enums import ModelType
from deeploy import Client, DeployOptions

workspace_id = 'b7bb2d93-12b4-49aa-b264-04aa41d09b1e'
deployment_id = '71099933-bdf5-4765-abed-ccb54a3b5796'

client_options = {
    'deployment_token': 'yFjkjNUhHmf4I1Z2yZl3n6ZSj7L2G4RyU61wuzwq',
    'host': 'fullorbit.deeploy.ml',
    'workspace_id': workspace_id,
}
client = Client(**client_options)
print(client)

request_body = {
    "instances": [
        [6.9, 2.8, 4.8, 1.7]
    ]
}

prediction = client.predict(deployment_id, request_body)
explanation = client.explain(deployment_id, request_body)

request_log_id=explanation['requestLogId']
prediction_log_id=explanation['predictionLogIds'][0]

evaluation_input = {
    "result": 2,
    "value": {"predictions": [False]},
    "explanation": "example"
}

client.evaluate(deployment_id, request_log_id, prediction_log_id, evaluation_input)
