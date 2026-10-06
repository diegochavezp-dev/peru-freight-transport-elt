from pathlib import Path

import pandas as pd


file_path = Path("data/raw/Carga Nacional_22-24.csv")

df = pd.read_csv(
    file_path,
    sep=";",
    encoding="utf-8",
    dtype=str,
    keep_default_na=False,
    nrows=5
)
print("Cantidad de columnas:", len(df.columns))

print("\nColumnas:")
for column in df.columns:
    print(column)

print("\nPrimeras 5 filas:")
print(df)