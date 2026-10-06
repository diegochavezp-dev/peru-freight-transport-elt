-- Validación de registros cargados en la capa RAW

-- Conteo por fuente
SELECT
    '2022-2024' AS fuente,
    COUNT(*) AS cantidad_filas
FROM raw.transporte_carga_2022_2024

UNION ALL

SELECT
    '2025' AS fuente,
    COUNT(*) AS cantidad_filas
FROM raw.transporte_carga_2025;


-- Conteo total de registros
SELECT
    (
        SELECT COUNT(*)
        FROM raw.transporte_carga_2022_2024
    )
    +
    (
        SELECT COUNT(*)
        FROM raw.transporte_carga_2025
    ) AS total_filas;


-- Muestra de datos RAW 2022-2024
SELECT *
FROM raw.transporte_carga_2022_2024
LIMIT 10;


-- Muestra de datos RAW 2025
SELECT *
FROM raw.transporte_carga_2025
LIMIT 10;