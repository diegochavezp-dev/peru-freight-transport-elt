-- Creación de tablas de la capa RAW.
-- Los campos originales del MTC se almacenan como TEXT
-- para preservar su representación durante la ingestión.

CREATE TABLE raw.transporte_carga_2022_2024 (
    id TEXT,
    ruc TEXT,
    razon_social TEXT,
    fecha_resolucion TEXT,
    vigencia_hasta TEXT,
    permiso_oper TEXT,
    placa TEXT,
    anio_fab TEXT,
    n_chasis TEXT,
    n_motor TEXT,
    marca TEXT,
    servicio TEXT,
    clase TEXT,
    combustible TEXT,
    n_asientos TEXT,
    n_llantas TEXT,
    n_ejes TEXT,
    carga_util TEXT,
    p_seco TEXT,
    p_bruto TEXT,
    largo TEXT,
    ancho TEXT,
    alto TEXT,
    departamento TEXT,
    fecha_corte TEXT
);

CREATE TABLE raw.transporte_carga_2025 (
    id TEXT,
    ruc TEXT,
    razon_social TEXT,
    fecha_resolucion TEXT,
    vigencia_hasta TEXT,
    permiso_oper TEXT,
    placa TEXT,
    anio_fab TEXT,
    n_chasis TEXT,
    n_motor TEXT,
    marca TEXT,
    servicio TEXT,
    clase TEXT,
    combustible TEXT,
    n_asientos TEXT,
    n_llantas TEXT,
    n_ejes TEXT,
    carga_util TEXT,
    p_seco TEXT,
    p_bruto TEXT,
    largo TEXT,
    ancho TEXT,
    alto TEXT,
    departamento TEXT,
    fecha_corte TEXT
);