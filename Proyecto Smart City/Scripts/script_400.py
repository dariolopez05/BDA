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

# Rangos realistas por atributo
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
