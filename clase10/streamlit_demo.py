"""
Clase 10 - Demo del profesor
Dashboard de calidad del aire en Risaralda.

Como se ejecuta (desde la carpeta clase10/demo/):

    streamlit run streamlit_demo.py

Para detenerlo: Ctrl+C en la terminal. Cerrar la pestaña del navegador NO lo apaga.
Si el puerto esta ocupado:

    streamlit run streamlit_demo.py --server.port 8502

Este archivo NO es un notebook. No tiene celdas y no se ejecuta con el boton de play
del editor. Streamlit vuelve a ejecutar el archivo completo cada vez que alguien mueve
un widget: por eso la carga del CSV va dentro de una funcion con @st.cache_data.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# La ruta se arma desde la ubicacion de este archivo, no desde donde se ejecuta la
# terminal. parents[1] es clase10/, y de ahi entramos a data/.
RUTA_DATOS = Path(__file__).resolve().parents[1] / "data" / "calidad_aire_risaralda.csv"

# Limite superior razonable para una medicion de material particulado en ug/m3.
# El dataset trae cuatro valores absurdos (hasta 45.839) que aplastan todos los graficos.
LIMITE_MEDICION = 500

# Guia de la OMS para PM2.5 en 24 horas, en ug/m3. Sirve de ancla para leer las cifras.
GUIA_OMS_PM25 = 15


st.set_page_config(
    page_title="Calidad del aire en Risaralda",
    layout="wide",
)


# PASO 1 - Cargar y limpiar una sola vez.
# @st.cache_data guarda el resultado de la funcion. Sin este decorador, el CSV se
# volveria a leer cada vez que el usuario mueve un filtro.
@st.cache_data
def cargar_datos() -> pd.DataFrame:
    df = pd.read_csv(RUTA_DATOS)

    # Nombres cortos, en minuscula y sin espacios. Se decide aqui y se usa asi en
    # todo el archivo.
    df = df.rename(
        columns={
            "Municipio": "municipio",
            "Estacion": "estacion",
            "Fecha": "fecha",
            "Diametro aerodinamico": "particula",
            "Medicion": "medicion",
        }
    )

    # La fecha llega como texto en formato MM/DD/YYYY hh:mm:ss AM.
    # Especificar el formato evita que pandas adivine fila por fila.
    df["fecha"] = pd.to_datetime(
        df["fecha"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )

    df["medicion"] = pd.to_numeric(df["medicion"], errors="coerce")

    for columna in ["municipio", "estacion", "particula"]:
        df[columna] = df[columna].astype(str).str.strip()

    # Limpieza documentada:
    # - se descartan filas sin fecha o sin medicion
    # - se descartan mediciones en 0 (sensor apagado, no aire limpio)
    # - se descartan las mediciones imposibles por encima del limite
    df = df.dropna(subset=["fecha", "medicion"])
    df = df[(df["medicion"] > 0) & (df["medicion"] <= LIMITE_MEDICION)]

    return df.sort_values("fecha").reset_index(drop=True)


df = cargar_datos()


st.title("Calidad del aire en Risaralda")
st.write(
    "Mediciones de material particulado (PM10 y PM2.5) en cuatro municipios "
    "de Risaralda entre 2007 y 2023. Fuente: datos.gov.co."
)


# PASO 2 - Los tres filtros. Van en la barra lateral para no competir con el contenido.
with st.sidebar:
    st.header("Filtros")

    municipios_disponibles = sorted(df["municipio"].unique())
    particulas_disponibles = sorted(df["particula"].unique())

    municipios_elegidos = st.multiselect(
        "Municipio",
        options=municipios_disponibles,
        default=municipios_disponibles,
    )

    particulas_elegidas = st.multiselect(
        "Tipo de particula",
        options=particulas_disponibles,
        default=particulas_disponibles,
    )

    fecha_min = df["fecha"].min().date()
    fecha_max = df["fecha"].max().date()

    rango_fechas = st.slider(
        "Rango de fechas",
        min_value=fecha_min,
        max_value=fecha_max,
        value=(fecha_min, fecha_max),
    )

    mostrar_tabla = st.checkbox("Mostrar los datos filtrados", value=False)


# PASO 6 - Guardas. Sin esto, deseleccionar todos los municipios revienta la app.
# st.stop() corta la ejecucion del script en este punto.
if not municipios_elegidos:
    st.warning("Selecciona al menos un municipio.")
    st.stop()

if not particulas_elegidas:
    st.warning("Selecciona al menos un tipo de particula.")
    st.stop()


# PASO 3 - Filtrar el DataFrame. isin y between ya se usaron en clases anteriores;
# lo unico nuevo es que ahora los valores vienen de los widgets.
df_filtrado = df[
    df["municipio"].isin(municipios_elegidos)
    & df["particula"].isin(particulas_elegidas)
    & df["fecha"].dt.date.between(rango_fechas[0], rango_fechas[1])
].copy()

if df_filtrado.empty:
    st.error("Ninguna fila cumple los filtros seleccionados. Amplia el rango.")
    st.stop()


# PASO 4 - Los tres KPIs. st.columns(3) devuelve tres contenedores.
col_kpi_1, col_kpi_2, col_kpi_3 = st.columns(3)

promedio = df_filtrado["medicion"].mean()
maximo = df_filtrado["medicion"].max()
registros = len(df_filtrado)

with col_kpi_1:
    st.metric("Medicion promedio (ug/m3)", f"{promedio:,.1f}")

with col_kpi_2:
    st.metric("Pico maximo (ug/m3)", f"{maximo:,.1f}")

with col_kpi_3:
    st.metric("Mediciones en la vista", f"{registros:,}")


# PASO 5 - Los tres graficos. Son exactamente los mismos del notebook.
# Lo unico que cambia es el envase: st.plotly_chart en vez de fig.show().
col_izq, col_der = st.columns(2)

with col_izq:
    # Grafico 1: como evoluciona en el tiempo.
    # px no agrega por ti: el groupby va antes, siempre.
    serie_mensual = (
        df_filtrado.groupby(
            [pd.Grouper(key="fecha", freq="ME"), "particula"], as_index=False
        )["medicion"]
        .mean()
        .sort_values("fecha")
    )

    fig_linea = px.line(
        serie_mensual,
        x="fecha",
        y="medicion",
        color="particula",
        markers=False,
        title="El PM10 duplica al PM2.5, pero solo hay PM2.5 desde 2012",
    )
    fig_linea.update_layout(
        xaxis_title="", yaxis_title="Promedio mensual (ug/m3)", legend_title=""
    )
    st.plotly_chart(fig_linea, use_container_width=True)

with col_der:
    # Grafico 2: quien tiene el aire mas cargado.
    promedio_municipio = (
        df_filtrado.groupby("municipio", as_index=False)["medicion"]
        .mean()
        .sort_values("medicion", ascending=False)
    )

    # El titulo es fijo y el grafico es filtrable: por eso dice "empate tecnico" y no corona a
    # nadie. Con los datos crudos Dosquebradas promedia 78,6 y gana; con la limpieza de arriba
    # promedia 30,2 y queda 0,4 por debajo de Santa Rosa de Cabal. Cuatro filas de 5.047 deciden
    # quien encabeza. Lo que sobrevive a cualquier filtro es el st.info del final, que se calcula.
    fig_barras = px.bar(
        promedio_municipio,
        x="municipio",
        y="medicion",
        title="Santa Rosa de Cabal encabeza por 0,4 ug/m3: un empate tecnico",
    )
    fig_barras.update_layout(
        xaxis_title="", yaxis_title="Promedio (ug/m3)", showlegend=False
    )
    st.plotly_chart(fig_barras, use_container_width=True)


# Grafico 3: cuanto varia cada estacion. El promedio esconde la variabilidad.
fig_caja = px.box(
    df_filtrado,
    x="estacion",
    y="medicion",
    color="particula",
    title="El promedio esconde picos: la variabilidad por estacion",
)
fig_caja.update_layout(xaxis_title="", yaxis_title="Medicion (ug/m3)", legend_title="")
st.plotly_chart(fig_caja, use_container_width=True)


# El insight escrito. Es el puente con la clase 9: el dashboard no termina en el
# grafico, termina en una frase.
peor = (
    df_filtrado.groupby("municipio", as_index=False)["medicion"]
    .mean()
    .sort_values("medicion", ascending=False)
    .iloc[0]
)

pm25 = df_filtrado[df_filtrado["particula"] == "PM2.5"]
if not pm25.empty:
    dias_sobre_guia = (pm25["medicion"] > GUIA_OMS_PM25).mean() * 100
    detalle_pm25 = (
        f" El {dias_sobre_guia:.0f}% de las mediciones de PM2.5 en esta vista "
        f"supera la guia de la OMS ({GUIA_OMS_PM25} ug/m3)."
    )
else:
    detalle_pm25 = ""

st.info(
    f"En la vista actual, {peor['municipio']} registra el promedio mas alto "
    f"({peor['medicion']:.1f} ug/m3).{detalle_pm25}"
)


if mostrar_tabla:
    st.subheader("Datos filtrados")
    st.dataframe(df_filtrado, use_container_width=True)
