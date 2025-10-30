import requests
import json

url = "http://localhost:1026/v2/subscriptions"
headers = {"Content-Type": "application/json"}

subscription = {
    "description": "Suscripción para monitorear sensores de calidad, temperatura y CO2",
    "subject": {
        "entities": [
            {"id": "SensorCO2", "type": "SensorCO2"},
            {"id": "SensorTemp", "type": "SensorTemperatura"},
            {"id": "SensorCalid", "type": "SensorCalidadAgua"}
        ],
        "condition": {
            "attrs": ["ph", "temperatura", "humedad", "chlorine"]
        }
    },
    "notification": {
        "http": { "url": "http://quantumleap:8668/v2/notify" },
        "attrs": ["ph", "temperatura", "humedad", "chlorine"]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}

response = requests.post(url, headers=headers, data=json.dumps(subscription))

if response.status_code in (201, 204):
    print("✅ Suscripción creada correctamente")
else:
    print(f"❌ Error al crear la suscripción: {response.status_code}")
    print(response.text)
