import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent

carpetas_csv = [
    base_path / "datos",
    base_path / "indicadores"
]

carpetas_parquet = {
    "datos": base_path / "datos_parquet",
    "indicadores": base_path / "indicadores_parquet"
}

for folder in carpetas_parquet.values():
    folder.mkdir(parents=True, exist_ok=True)

for carpeta in carpetas_csv:
    nombre = carpeta.name 
    destino = carpetas_parquet[nombre]

    print(f"\n📂 Buscando CSV en: {carpeta.resolve()}")

    csv_files = list(carpeta.glob("*.csv"))
    print(f"🔎 CSV encontrados en {nombre}: {len(csv_files)}")

    for csv_file in csv_files:
        print(f"\n➡ Convirtiendo: {csv_file.name}")

        try:
            df = pd.read_csv(csv_file)
        except:
            df = pd.read_csv(csv_file, sep=";")

        parquet_path = destino / f"{csv_file.stem}.parquet"
        df.to_parquet(parquet_path, index=False)

        print(f"   ✅ Guardado en: {parquet_path.name}")

print("\n Conversión completada.\n")
