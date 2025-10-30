import requests
import json

url = "http://localhost:1026/v2/entities/SensorCO2/attrs"
headers = {"Content-Type": "application/json"}

data = {
    "ph": {
        "value": 77,
        "type": "Float"
    }
}

response = requests.patch(url, headers=headers, data=json.dumps(data))

if response.status_code in (204, 201):
    print("✅ Atributo 'ph' actualizado correctamente en SensorCO2")
else:
    print(f"❌ Error al actualizar 'ph': {response.status_code}")
    print(response.text)
