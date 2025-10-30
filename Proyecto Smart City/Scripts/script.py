import requests
import json

url = "http://localhost:1026/v2/entities"
headers = {"Content-Type": "application/json"}

entities = [
    {
        "id": "SensorCO2",
        "type": "SensorCO2",
        "ph": {
            "value": 80,
            "type": "Float"
        }
    },
    {
        "id": "SensorTemp",
        "type": "SensorTemperatura",
        "temperatura": {
            "value": 80,
            "type": "Float"
        },
        "humedad": {
            "value": 80,
            "type": "Float"
        }
    },
    {
        "id": "SensorCalid",
        "type": "SensorCalidadAgua",
        "ph": {
            "value": 80,
            "type": "Float"
        },
        "chlorine": {
            "value": 80,
            "type": "Float"
        },
        "temperatura": {
            "value": 80,
            "type": "Float"
        }
    }
]

for entity in entities:
    response = requests.post(url, headers=headers, data=json.dumps(entity))
    if response.status_code in (201, 204):
        print(f"✅ {entity['id']} creada correctamente")
    else:
        print(f"❌ Error al crear {entity['id']}: {response.status_code} - {response.text}")
