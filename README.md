# Pipeline de datos para análisis del transporte terrestre de carga en Perú

## Descripción

Este proyecto trabaja con datos públicos del Ministerio de Transportes y
Comunicaciones del Perú (MTC) sobre el parque vehicular habilitado para el
transporte terrestre de mercancías a nivel nacional durante el periodo
2022-2025.

La información contiene datos de empresas y características técnicas de los
vehículos, como año de fabricación, marca, clase vehicular, tipo de combustible,
número de ejes, capacidad de carga, peso, dimensiones y departamento de
inscripción.

## Problema

Los datos se encuentran distribuidos en archivos correspondientes a distintos
periodos y presentan diferencias de formato, valores no disponibles y otros
casos que dificultan su integración y análisis conjunto.

## Objetivo

Construir una fuente de datos unificada, estandarizada y confiable que permita
analizar la evolución y las principales características del parque vehicular
habilitado para transporte terrestre de carga en Perú entre 2022 y 2025.

## Enfoque

Para integrar y preparar la información se utilizará un proceso ELT:

**Extract → Load → Transform**

Los datos originales serán conservados inicialmente en una capa de datos crudos
y posteriormente serán transformados y estandarizados para generar información
preparada para análisis.

## Fuente de datos

**Entidad:** Ministerio de Transportes y Comunicaciones del Perú (MTC)

**Dataset:** Transporte Terrestre de Carga Nacional 2022-2025

**Fuente oficial:**  
https://www.datosabiertos.gob.pe/dataset/transporte-terrestre-de-carga-nacional-2022-2025-ministerio-de-transportes-y-comunicaciones-

**Cobertura:** Perú, 2022-2025

**Formato:** CSV

**Licencia:** Open Data Commons Attribution License

## Estado del proyecto

En desarrollo.
