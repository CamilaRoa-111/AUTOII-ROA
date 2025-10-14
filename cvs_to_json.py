import pandas as pd

# Nombre del archivo CSV original
csv_file = 'movies_initial.csv'

# Nombre del archivo JSON que se generará
json_file = 'movies.json'

# Leer el CSV
with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
    df = pd.read_csv(f)

# Convertir a JSON
df.to_json(json_file, orient='records', lines=False)

print(f"✅ Archivo '{json_file}' creado correctamente a partir de '{csv_file}'.")
