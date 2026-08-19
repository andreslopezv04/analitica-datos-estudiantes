"""
Clase 10 - Reto: adapta este dashboard al dataset de tu equipo.

Como se ejecuta (desde la carpeta clase10/reto/):

    streamlit run streamlit_app_starter.py

Tal como esta, el archivo levanta con el dataset de calidad del aire del demo.
Tu trabajo es cambiarlo por el tuyo. Hay tres cosas que hacer, en este orden:

  1. Ajustar el bloque CONFIGURACION de abajo para que apunte a tu CSV y a tus columnas.
  2. Completar las tres celdas marcadas con "TU CODIGO AQUI".
  3. Reescribir los titulos de los graficos para que sean mensajes, no etiquetas
     (clase 9: el titulo de la slide es el mensaje; aqui aplica igual).

Minimo exigido: 3 filtros, 3 KPIs, 3 graficos. Maximo razonable: 5 y 5.

Si algo falla:
- "command not found: streamlit" -> pip install streamlit
- "Port 8501 is already in use" -> streamlit run streamlit_app_starter.py --server.port 8502
- Editaste el archivo y no cambia nada -> guarda con Cmd+S y usa el boton "Rerun"
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------------------------------------------------------------------
# CONFIGURACION - esto es lo primero que tienes que cambiar
# ---------------------------------------------------------------------------

# TODO: apunta a tu propio CSV.
# Si tu dataset esta en clase10/data/, deja el patron de parents[1].
# Si esta en otra carpeta, escribe la ruta relativa desde clase10/reto/.
RUTA_DATOS = Path(__file__).resolve().parents[1] / "data" / "calidad_aire_risaralda.csv"

# TODO: nombres cortos, en minuscula y sin tildes ni espacios, para TUS columnas.
# La clave es el nombre exacto que trae el archivo. El valor es como lo vas a usar tu.
RENOMBRES = {
    "Municipio": "categoria_1",
    "Estacion": "categoria_2",
    "Fecha": "fecha",
    "Diametro aerodinamico": "grupo",
    "Medicion": "valor",
}

# TODO: etiquetas que va a ver el usuario en los filtros.
TITULO_APP = "Calidad del aire en Risaralda"
ETIQUETA_CATEGORIA_1 = "Municipio"
ETIQUETA_GRUPO = "Tipo de particula"
UNIDAD_VALOR = "ug/m3"

# TODO: si tu columna numerica tiene valores imposibles, define aqui el tope.
# Si no aplica, pon None.
LIMITE_VALOR = 500


# ---------------------------------------------------------------------------
# 1. CARGA Y LIMPIEZA
# ---------------------------------------------------------------------------

st.set_page_config(page_title=TITULO_APP, layout="wide")


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    """Lee el CSV una sola vez y lo deja listo para filtrar.

    @st.cache_data guarda el resultado. Sin el, Streamlit releeria el archivo
    cada vez que el usuario mueve un filtro.
    """
    df = pd.read_csv(RUTA_DATOS)
    df = df.rename(columns=RENOMBRES)

    # TODO: si tu fecha viene en otro formato, cambia el patron.
    # Si tu dataset no tiene fecha, borra esta linea y usa un filtro numerico.
    df["fecha"] = pd.to_datetime(
        df["fecha"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    for columna in ["categoria_1", "categoria_2", "grupo"]:
        df[columna] = df[columna].astype(str).str.strip()

    df = df.dropna(subset=["fecha", "valor"])

    if LIMITE_VALOR is not None:
        df = df[(df["valor"] > 0) & (df["valor"] <= LIMITE_VALOR)]

    return df.sort_values("fecha").reset_index(drop=True)


df = cargar_datos()

st.title(TITULO_APP)
# TODO: una linea que diga de que trata el dataset y de donde salio.
st.write("Descripcion pendiente: que datos son, de que periodo y de que fuente.")


# ---------------------------------------------------------------------------
# 2. FILTROS (minimo 3: al menos uno categorico y uno de rango)
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("Filtros")

    opciones_categoria = sorted(df["categoria_1"].unique())
    opciones_grupo = sorted(df["grupo"].unique())

    categorias_elegidas = st.multiselect(
        ETIQUETA_CATEGORIA_1,
        options=opciones_categoria,
        default=opciones_categoria,
    )

    grupos_elegidos = st.multiselect(
        ETIQUETA_GRUPO,
        options=opciones_grupo,
        default=opciones_grupo,
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


# Guardas: sin esto la app revienta cuando el usuario deselecciona todo.
if not categorias_elegidas:
    st.warning(f"Selecciona al menos un valor en {ETIQUETA_CATEGORIA_1}.")
    st.stop()

if not grupos_elegidos:
    st.warning(f"Selecciona al menos un valor en {ETIQUETA_GRUPO}.")
    st.stop()


# ---------------------------------------------------------------------------
# 3. FILTRADO DEL DATAFRAME
# ---------------------------------------------------------------------------

df_filtrado = df[
    df["categoria_1"].isin(categorias_elegidas)
    & df["grupo"].isin(grupos_elegidos)
    & df["fecha"].dt.date.between(rango_fechas[0], rango_fechas[1])
].copy()

if df_filtrado.empty:
    st.error("Ninguna fila cumple los filtros seleccionados.")
    st.stop()


# ---------------------------------------------------------------------------
# 4. KPIs (minimo 3, y los tres tienen que cambiar al mover los filtros)
# ---------------------------------------------------------------------------

col_1, col_2, col_3 = st.columns(3)

promedio = df_filtrado["valor"].mean()
maximo = df_filtrado["valor"].max()

with col_1:
    st.metric(f"Promedio ({UNIDAD_VALOR})", f"{promedio:,.1f}")

with col_2:
    st.metric(f"Maximo ({UNIDAD_VALOR})", f"{maximo:,.1f}")

with col_3:
    # TU CODIGO AQUI
    # Define el tercer KPI. Que numero cambiaria una decision?
    # Ideas: un conteo de filas, un porcentaje sobre un umbral, cuantas
    # categorias distintas hay en la vista, la diferencia entre dos grupos.
    # Reemplaza las dos lineas de abajo.
    tercer_kpi = 0
    st.metric("Tercer KPI (cambiar)", f"{tercer_kpi:,}")


# ---------------------------------------------------------------------------
# 5. GRAFICOS (minimo 3, y cada uno responde una pregunta distinta)
# ---------------------------------------------------------------------------

col_izq, col_der = st.columns(2)

with col_izq:
    # Grafico 1: evolucion en el tiempo.
    # Recuerda: px NO agrega por ti. El groupby va antes, siempre.
    serie = (
        df_filtrado.groupby(
            [pd.Grouper(key="fecha", freq="ME"), "grupo"], as_index=False
        )["valor"]
        .mean()
        .sort_values("fecha")
    )

    fig_linea = px.line(
        serie,
        x="fecha",
        y="valor",
        color="grupo",
        # TODO: cambia este titulo por el mensaje que quieres que el usuario concluya.
        title="Titulo descriptivo (cambialo por un mensaje)",
    )
    fig_linea.update_layout(
        xaxis_title="", yaxis_title=f"Promedio ({UNIDAD_VALOR})", legend_title=""
    )
    st.plotly_chart(fig_linea, use_container_width=True)

with col_der:
    # Grafico 2: comparacion entre categorias.
    resumen = (
        df_filtrado.groupby("categoria_1", as_index=False)["valor"]
        .mean()
        .sort_values("valor", ascending=False)
    )

    fig_barras = px.bar(
        resumen,
        x="categoria_1",
        y="valor",
        # TODO: cambia este titulo por un mensaje.
        title="Titulo descriptivo (cambialo por un mensaje)",
    )
    fig_barras.update_layout(
        xaxis_title="", yaxis_title=f"Promedio ({UNIDAD_VALOR})", showlegend=False
    )
    st.plotly_chart(fig_barras, use_container_width=True)


# TU CODIGO AQUI
# Grafico 3. Sugerencia: px.box para mostrar la variabilidad que el promedio esconde.
# Necesitas: crear la figura, ajustar el layout y renderizarla con
# st.plotly_chart(fig, use_container_width=True).


# ---------------------------------------------------------------------------
# 6. EL INSIGHT ESCRITO
# ---------------------------------------------------------------------------

# TU CODIGO AQUI
# Una frase, con cifra, calculada a partir de df_filtrado, que siga siendo cierta
# sin importar como el usuario mueva los filtros. Usa st.info(...).
# Este es el puente con la clase 9: el dashboard no termina en el grafico,
# termina en una conclusion.


if mostrar_tabla:
    st.subheader("Datos filtrados")
    st.dataframe(df_filtrado, use_container_width=True)
