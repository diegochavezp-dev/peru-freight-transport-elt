import csv
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


load_dotenv()

CSV_PATH = Path("data/raw/Carga Nacional_22-24.csv")
TABLE_NAME = "raw.transporte_carga_2022_2024"
ENCODING = "latin-1"

EXPECTED_COLUMNS = [
    "ID",
    "RUC",
    "RAZON_SOCIAL",
    "FECHA_RESOLUCION",
    "VIGENCIA_HASTA",
    "PERMISO_OPER",
    "PLACA",
    "ANIO_FAB",
    "N_CHASIS",
    "N_MOTOR",
    "MARCA",
    "SERVICIO",
    "CLASE",
    "COMBUSTIBLE",
    "N_ASIENTOS",
    "N_LLANTAS",
    "N_EJES",
    "CARGA_UTIL",
    "P_SECO",
    "P_BRUTO",
    "LARGO",
    "ANCHO",
    "ALTO",
    "DEPARTAMENTO",
    "FECHA_CORTE",
]


connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)


with open(CSV_PATH, "r", encoding=ENCODING, newline="") as file:
    reader = csv.reader(file, delimiter=";")

    header = next(reader)

    if header != EXPECTED_COLUMNS:
        raise ValueError(
            "Las columnas del CSV no coinciden con las columnas esperadas."
        )

    with connection.cursor() as cursor:
        with cursor.copy(
            f"""
            COPY {TABLE_NAME} (
                id,
                ruc,
                razon_social,
                fecha_resolucion,
                vigencia_hasta,
                permiso_oper,
                placa,
                anio_fab,
                n_chasis,
                n_motor,
                marca,
                servicio,
                clase,
                combustible,
                n_asientos,
                n_llantas,
                n_ejes,
                carga_util,
                p_seco,
                p_bruto,
                largo,
                ancho,
                alto,
                departamento,
                fecha_corte
            )
            FROM STDIN
            """
        ) as copy:
            for row in reader:
                copy.write_row(row)


connection.commit()
connection.close()

print("Carga RAW 2022-2024 completada correctamente.")