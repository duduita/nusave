from data_API import DataAPI
import json

api = DataAPI()
x = {
    "ID": "TNWODTCZYPQHMWMFUHAS",
    "feature": "statistics",
    "filter": "Beleza"
}
x = json.dumps(x)

print(json.loads(api.readInstructions(x)))