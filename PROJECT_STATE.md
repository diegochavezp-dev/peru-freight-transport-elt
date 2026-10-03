# Estado del proyecto

## Última actualización

03/10/2026

## Estado actual

Se completó la configuración inicial del entorno, la base de datos y la documentación de las principales decisiones de arquitectura.

## Completado

- Repositorio de GitHub creado.
- README inicial creado.
- PostgreSQL instalado y configurado.
- DBeaver instalado y conectado a PostgreSQL.
- Base de datos `peru_freight` creada.
- Esquemas `raw`, `staging` y `analytics` creados.
- Estructura inicial del proyecto creada.
- Archivos CSV originales almacenados localmente en `data/raw/`.
- Datos originales excluidos del control de versiones mediante `.gitignore`.
- Decisión de utilizar PostgreSQL documentada.
- Separación en capas `raw`, `staging` y `analytics` documentada.
- Enfoque ELT documentado.

## Fuente de datos

Ministerio de Transportes y Comunicaciones del Perú (MTC).

Dataset:  
Transporte Terrestre de Carga Nacional 2022-2025.

## Próximo paso

Diseñar la estructura de la capa `raw` y definir cómo se cargarán los archivos CSV originales a PostgreSQL.

## Pendiente

- Diseñar las tablas de la capa `raw`.
- Implementar la carga de datos.
- Validar cantidad de registros cargados.
- Analizar calidad de datos.
- Diseñar transformaciones de `staging`.
- Construir la capa `analytics`.
- Preparar análisis posteriores.