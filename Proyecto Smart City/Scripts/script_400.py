import requests, random, time

def update_all(count=400, delay=5):
    URL = "http://localhost:1026/v2/op/update"
    HEADERS = {
        "Content-Type": "application/json",
        # "Fiware-Service": "default",   # ← descomenta si lo usas
        # "Fiware-ServicePath": "/",     # ← descomenta si lo usas
    }

    # Rangos realistas
    rng = {
        "ph": (6.5, 8.5),
        "temperatura": (15.0, 35.0),
        "humedad": (30.0, 90.0),
        "chlorine": (0.0, 5.0),
    }

    print(f"🚀 Enviando {count} lotes (batch) de actualización 'a la vez' para las 3 entidades…\n")

    for i in range(1, count + 1):
        # Valores aleatorios para este lote
        ph1 = round(random.uniform(*rng["ph"]), 2)
        t2  = round(random.uniform(*rng["temperatura"]), 2)
        h2  = round(random.uniform(*rng["humedad"]), 2)
        ph3 = round(random.uniform(*rng["ph"]), 2)
        cl3 = round(random.uniform(*rng["chlorine"]), 2)
        t3  = round(random.uniform(*rng["temperatura"]), 2)

        payload = {
            "actionType": "update",
            "entities": [
                {
                    "id": "SensorCO2",
                    "type": "SensorCO2",
                    "ph": {"value": ph1, "type": "Float"}
                },
                {
                    "id": "SensorTemp",
                    "type": "SensorTemperatura",
                    "temperatura": {"value": t2, "type": "Float"},
                    "humedad": {"value": h2, "type": "Float"}
                },
                {
                    "id": "SensorCalid",
                    "type": "SensorCalidadAgua",
                    "ph": {"value": ph3, "type": "Float"},
                    "chlorine": {"value": cl3, "type": "Float"},
                    "temperatura": {"value": t3, "type": "Float"}
                }
            ]
        }

        r = requests.post(URL, headers=HEADERS, json=payload)
        if r.status_code in (204, 201):
            print(f"[{i}/{count}] ✅ Batch OK | CO2.ph={ph1} | Temp.t={t2},h={h2} | Calid.ph={ph3},cl={cl3},t={t3}")
        else:
            print(f"[{i}/{count}] ⚠️  HTTP {r.status_code}: {r.text[:200]}")

        if delay:
            time.sleep(delay)

    print("\n✅ Listo: batches enviados correctamente.")

# --- Ejecutar ---
if __name__ == "__main__":
    update_all(count=400, delay=5)  # ajusta count/delay si quieres
