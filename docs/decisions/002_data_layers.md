# ADR-002: Separación de datos por capas

## Contexto

Los archivos correspondientes a distintos periodos presentan diferencias de
formato y valores especiales que requieren tratamiento antes de poder ser
analizados de manera conjunta.

Modificar directamente los datos originales dificultaría la trazabilidad y
podría provocar la pérdida de información necesaria para reprocesar los datos.

## Decisión

Organizar la información dentro de PostgreSQL utilizando tres esquemas:

- `raw`
- `staging`
- `analytics`

## Responsabilidad de cada capa

### raw

Contendrá los datos provenientes de las fuentes originales con la menor
cantidad posible de modificaciones.

Su propósito es conservar una representación cercana al dato recibido y
permitir que el procesamiento pueda repetirse posteriormente si fuese
necesario.

### staging

Contendrá información limpia y estandarizada.

En esta capa se realizarán tareas como:

- normalización de fechas;
- conversión de tipos de datos;
- tratamiento de valores no disponibles;
- estandarización de campos;
- validaciones de calidad;
- integración de los diferentes periodos.

### analytics

Contendrá información preparada para consultas y consumo analítico.

Esta capa evitará que las herramientas de análisis tengan que trabajar
directamente con los datos crudos o repetir reglas de limpieza.

## Razones

La separación permite:

- conservar trazabilidad respecto a los datos originales;
- aislar las reglas de limpieza y transformación;
- facilitar el reprocesamiento;
- evitar que los consumidores analíticos trabajen con datos inconsistentes;
- mantener responsabilidades claras entre las diferentes etapas del pipeline.

## Consecuencias

El procesamiento de la información seguirá un flujo general:

`raw → staging → analytics`

Cada capa tendrá una responsabilidad distinta y las transformaciones deberán
realizarse de forma progresiva.