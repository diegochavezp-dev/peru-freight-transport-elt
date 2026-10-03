# ADR-003: Uso de un enfoque ELT

## Contexto

Los datos del proyecto provienen de archivos CSV correspondientes a diferentes
periodos y requieren procesos de integración, estandarización y control de
calidad.

Se desea conservar inicialmente los datos originales dentro del sistema de
almacenamiento antes de aplicar las reglas de transformación.

## Decisión

Utilizar un enfoque ELT:

**Extract → Load → Transform**

Los archivos originales serán extraídos desde la fuente de datos, cargados en
la capa `raw` de PostgreSQL y transformados posteriormente mediante SQL.

## Razones

- Permite conservar los datos originales antes de transformarlos.
- Facilita repetir las transformaciones sin volver a obtener la fuente.
- Permite aprovechar SQL como herramienta principal de transformación.
- Favorece la trazabilidad entre los datos originales y los datos preparados.
- Permite separar claramente la ingestión de las reglas de negocio y limpieza.

## Flujo general

1. Extraer los archivos de la fuente original.
2. Cargar los datos en el esquema `raw`.
3. Validar que la carga se haya realizado correctamente.
4. Transformar y estandarizar la información en `staging`.
5. Preparar estructuras orientadas al análisis en `analytics`.

## Alternativa considerada

### ETL

Un proceso ETL permitiría transformar los datos antes de cargarlos al sistema
principal.

No se seleccionó como enfoque principal porque este proyecto busca preservar
primero una copia de los datos recibidos y realizar posteriormente las
transformaciones dentro de PostgreSQL.

## Consecuencias

La carga inicial deberá evitar transformaciones innecesarias. Las reglas de
limpieza, estandarización y preparación analítica se implementarán en etapas
posteriores del pipeline.