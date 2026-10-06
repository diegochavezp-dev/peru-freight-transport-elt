# Estado del proyecto

## Última actualización

05/10/2026

## Estado actual

Se completó la ingestión inicial de los datos del MTC en la capa `raw` de PostgreSQL.

Los dos archivos fuente fueron inspeccionados y cargados sin aplicar reglas de
limpieza, conversión de tipos ni estandarización de negocio. La carga fue
validada mediante conteos de registros y revisión de muestras de los datos almacenados.

## Completado

- Repositorio de GitHub y estructura inicial del proyecto creados.
- README inicial creado.
- PostgreSQL y DBeaver configurados.
- Base de datos `peru_freight` creada.
- Esquemas `raw`, `staging` y `analytics` creados.
- Archivos CSV originales almacenados localmente en `data/raw/` y excluidos del control de versiones.
- Decisiones sobre PostgreSQL, separación por capas y enfoque ELT documentadas.
- Entorno virtual de Python configurado.
- Dependencias del proyecto registradas en `requirements.txt`.
- Conexión entre Python y PostgreSQL validada.
- Tablas de la capa `raw` creadas a partir de las 25 columnas de las fuentes.
- Ambos archivos CSV inspeccionados antes de su carga.
- Carga de los archivos CSV a PostgreSQL implementada mediante Python.
- Datos 2022-2024 cargados en `raw.transporte_carga_2022_2024`.
- Datos 2025 cargados en `raw.transporte_carga_2025`.
- Carga de la capa `raw` validada con 1,394,094 registros en total.
- Scripts SQL para crear las tablas `raw` y validar la carga documentados.

## Fuente de datos

Ministerio de Transportes y Comunicaciones del Perú (MTC).

Dataset:  
Transporte Terrestre de Carga Nacional 2022-2025.

## Próximo paso

Realizar el perfilado de los datos almacenados en la capa `raw` para identificar
valores faltantes, valores especiales, diferencias de formato e inconsistencias
que deberán tratarse posteriormente en `staging`.

## Pendiente

- Perfilar los datos de la capa `raw`.
- Documentar los problemas de calidad identificados.
- Definir reglas de limpieza y estandarización.
- Diseñar la capa `staging`.
- Implementar las transformaciones de `raw` a `staging`.
- Validar los datos transformados.
- Diseñar y construir la capa `analytics`.
- Desarrollar consultas SQL orientadas al análisis.
- Preparar los datos para Excel y Power BI.