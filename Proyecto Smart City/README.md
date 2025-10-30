# 1. Configuración del entorno FIWARE:
Comando para ejecutar docker: docker compose -p PruebaDocker up -d 

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

import requests, time, random

URL = "http://localhost:1026"
HEADERS = {
    "Content-Type": "application/json",
    # "Fiware-Service": "default",   # ← descomenta si lo usas
    # "Fiware-ServicePath": "/",     # ← descomenta si lo usas
}

ENTITIES = {
    "SensorCO2": ["ph"],
    "SensorTemp": ["temperatura", "humedad"],
    "SensorCalid": ["ph", "chlorine", "temperatura"],
}

RANGES = {
    "ph": (6.5, 8.5),             # Agua normal
    "temperatura": (15.0, 35.0),  # Temperatura ambiente
    "humedad": (30.0, 90.0),      # Humedad relativa %
    "chlorine": (0.0, 5.0),       # Cloro residual en mg/L
}

COUNT = 400   # número de updates por atributo
DELAY = 0.2   # segundos entre updates (ajusta según rendimiento)

print("🚀 Iniciando carga masiva de datos aleatorios...\n")

total = 0

for eid, attrs in ENTITIES.items():
    print(f"▶️  Entidad: {eid}")
    for attr in attrs:
        min_v, max_v = RANGES[attr]
        print(f"   • Atributo: {attr} (rango {min_v}–{max_v})")
        for i in range(1, COUNT + 1):
            value = round(random.uniform(min_v, max_v), 2)
            payload = {attr: {"value": value, "type": "Float"}}
            url = f"{URL}/v2/entities/{eid}/attrs"

            try:
                r = requests.patch(url, headers=HEADERS, json=payload)
                if r.status_code in (204, 201):
                    print(f"      [{i}/{COUNT}] ✅ {eid}.{attr} = {value}")
                else:
                    print(f"      [{i}/{COUNT}] ⚠️  Error {r.status_code}: {r.text.strip()[:100]}")
            except Exception as e:
                print(f"      [{i}/{COUNT}] ❌ Error de conexión: {e}")

            total += 1
            if DELAY:
                time.sleep(DELAY)
        print(f"   ✓ Finalizado {attr}: {COUNT} updates\n")

print(f"\n✅ Carga completada con éxito. Total de actualizaciones: {total}")

# 5. Consulta Mongodb
Captura en carpeta img.