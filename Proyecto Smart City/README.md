# 2. Creación de las 3 entidades:

Sensor C02:
{
  "id": "SensorCO2",
  "type": "SensorCO2",
  "ph": {
    "value": 80,
    "type": "Float"
  }
}

Sensor Temperatura:
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
}

Sensor Calidad Agua
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

# 3. Creación de una suscripción:

{
  "description": "Suscripción para monitorear sensores de calidad, temperatura y CO2",
  "subject": {
    "entities": [
      { "id": "SensorCO2", "type": "SensorCO2" },
      { "id": "SensorTemp", "type": "SensorTemperatura" },
      { "id": "SensorCalid", "type": "SensorCalidadAgua" }
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


# 4. Carga de datos: