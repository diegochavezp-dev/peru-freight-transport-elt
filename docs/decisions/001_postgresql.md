# ADR-001: Uso de PostgreSQL

## Contexto

El proyecto trabaja con datos estructurados del Ministerio de Transportes y
Comunicaciones del Perú correspondientes al transporte terrestre de carga
durante el periodo 2022-2025.

La fuente se distribuye en archivos CSV y contiene atributos claramente
definidos sobre empresas y vehículos. El análisis posterior requerirá
filtrado, agregaciones, cruces entre datos y transformaciones mediante SQL.

## Decisión

Utilizar PostgreSQL como sistema principal de almacenamiento y procesamiento
relacional del proyecto.

## Razones

- Los datos poseen una estructura principalmente tabular.
- El proyecto requiere realizar transformaciones mediante SQL.
- PostgreSQL permite utilizar tipos de datos definidos y restricciones.
- Facilita la organización de la información mediante bases, esquemas y tablas.
- Permite realizar agregaciones, joins, funciones de ventana y otras consultas
  necesarias para el análisis.
- Puede integrarse posteriormente con herramientas de análisis y visualización.

## Alternativas consideradas

### MongoDB

MongoDB permite trabajar con documentos y estructuras flexibles, pero el
dataset utilizado en este proyecto no presenta una estructura documental
altamente variable que justifique utilizar una base orientada a documentos.

El modelo relacional resulta más adecuado para las características de la
fuente y para las operaciones analíticas previstas.

## Consecuencias

Las transformaciones principales podrán realizarse mediante SQL y la
información podrá organizarse en diferentes esquemas según su nivel de
procesamiento.