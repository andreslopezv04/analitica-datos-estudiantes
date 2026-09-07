# Clase 9 · Reto — Tu dashboard, con tu dataset

## Qué vas a entregar

Una app Streamlit que **corre**, sobre el dataset de tu equipo, con:

- **3 filtros** (al menos uno categórico y uno de rango)
- **3 KPIs** (que cambian cuando mueves los filtros)
- **3 gráficos** (que responden preguntas distintas)

Esto no es un ejercicio parecido al entregable del Momento 2. **Es el entregable del Momento 2.**
Lo que empieces hoy es lo que sustentas en la clase 11.

---

## "Pero en la clase 3 ya hice un tablero de Streamlit"

Sí, y salió corriendo sin que supieras Plotly ni Streamlit. Ese era el punto: **en la clase 3
aprendiste el método** —especificar, planear, ejecutar, validar— y lo probaste sobre algo que no
sabías construir.

Lo que no tenías entonces es lo de hoy: **el criterio.** Qué gráfico responde qué pregunta, qué
filtro vale la pena y cuál sobra, qué número cambia una decisión y cuál es decoración.

| Clase 3 | Clase 9 |
|---------|---------|
| Cómo se dirige el trabajo | Qué se le pide al trabajo |
| El bucle, sobre cualquier objeto | Las decisiones propias de un tablero |
| Salió una app | Sabes si esa app sirve |

**Una IA te entrega un tablero en dos minutos. Saber si sirve es otra cosa**, y es lo único que no
puedes pedir prestado. El método sin criterio produce doce filtros bien programados que no responden
ninguna pregunta.

---

## Archivos

| Archivo | Para qué |
|---------|----------|
| `reto.ipynb` | Diseñas el dashboard y preparas tu dataset. **Empieza aquí**. Trae **10 puntos de verificación** (`T1` a `T10`) con pista dirigida |
| `streamlit_app_starter.py` | La plantilla de la app. La adaptas a tus columnas. No es un cuaderno: no tiene celdas y no se ejecuta con el botón de play |

La solución no se publica. Si te trabas, pregunta en clase: el reto se resuelve en voz alta en el
cierre de la sesión.

---

## El orden importa

No abras el `.py` primero. Ese es el error que más tiempo cuesta.

Es el bucle de la clase 3, aplicado a un tablero. Si vas a usar las skills que instalaste entonces,
van en este orden: `especifica-encargo`, `planea-trabajo`, `ejecuta-plan`, `valida-resultado`. Y si
prefieres hacerlo a mano, los pasos son los mismos: **el bucle es el andamio, no la herramienta.**

### Paso 1 — Especificar: diseño en papel (en `reto.ipynb`)

Antes de tocar código, escribe:

1. **La pregunta.** ¿Qué quiere saber quién usaría esto? Nombra a la persona.
2. **Los 3 filtros.** ¿Qué cortes de esa pregunta importan de verdad?
3. **Los 3 KPIs.** ¿Qué tres números resumen la respuesta?
4. **Los 3 gráficos.** ¿Qué muestran que los números no alcanzan a decir?

Si no puedes escribir la pregunta, todavía no tienes un dashboard: tienes un dataset.

### Paso 2 — Planear y preparar tu dataset (en `reto.ipynb`)

- Cargar el CSV y verificar `shape` y `dtypes`.
- Renombrar columnas a minúsculas, sin tildes ni espacios. Una sola vez, en la carga.
- Convertir fechas con `pd.to_datetime` y el `format` correcto.
- Revisar valores imposibles. Un outlier extremo aplasta todos tus gráficos.
- Prototipar los 3 gráficos con Plotly **en el notebook**, antes de meterlos en la app.

### Paso 3 — Ejecutar: adaptar la app (en `streamlit_app_starter.py`)

1. Cambiar el bloque `CONFIGURACION` del principio: ruta, `RENOMBRES`, etiquetas.
2. Completar los tres `# TU CODIGO AQUI`: el tercer KPI, el tercer gráfico y el `st.info`.
3. Cambiar los títulos de los gráficos por mensajes, no etiquetas.

Ejecutar desde una terminal parada en la carpeta donde está `streamlit_app_starter.py`:

```
streamlit run streamlit_app_starter.py
```

### Paso 4 — Validar: las cuatro preguntas, con la app abierta

Este es el paso que se salta todo el mundo, y es el único que descubre que el tablero contesta otra
cosa. Se hace **moviendo controles**, no releyendo el archivo.

| La pregunta | Qué haces con la app abierta |
|-------------|------------------------------|
| **¿El número tiene sentido?** | Mira cada KPI contra el rango que conoces de tu dominio. Un promedio fuera de ese rango no es un error de sintaxis: es un dato que no era un dato |
| **¿La forma cuadra?** | Filtra por un solo valor y mira el conteo. Si sigue apareciendo el total, el filtro no filtró. Si aparece cero, filtró de más |
| **¿Responde lo que pregunté?** | Vuelve a la pregunta que escribiste en el paso 1. ¿La responde, o responde la que fue fácil de graficar? |
| **¿Cambió algo?** | Mueve cada control uno por uno. Un indicador que no se mueve nunca está desconectado: es el criterio que ya está en los requisitos |

**Y la regla que viene con el bucle: si la validación falla, se vuelve a especificar.** No se parcha
el gráfico. Un tablero que responde otra cosa casi siempre viene de una pregunta mal escrita en el
paso 1, y arreglar la salida esconde el problema hasta la sustentación.

---

## Requisitos, uno por uno

- [ ] La app **levanta**. Una app que no corre no cuenta.
- [ ] 3 filtros **distintos entre sí**. Dos filtros sobre columnas redundantes
      (como municipio y estación en el dataset del aire) cuentan como uno solo.
- [ ] 3 KPIs que reaccionan a los filtros. Un número que no cambia es decoración.
- [ ] 3 gráficos que responden preguntas distintas. Tres versiones de lo mismo cuentan como uno.
- [ ] La app **no revienta** si el usuario deselecciona todo (`st.warning` + `st.stop()`).
- [ ] Un `st.info` con el insight principal, calculado a partir del DataFrame filtrado.
- [ ] Los títulos de los gráficos son mensajes.
      Mal: "Consumo por municipio". Bien: "Tres municipios concentran la mitad del consumo".

**Techo:** más de 5 filtros o más de 5 gráficos se penaliza. La habilidad que se evalúa es elegir.

---

## Casos especiales

| Tu situación | Qué hacer |
|--------------|-----------|
| Mi dataset no tiene fecha | El filtro de rango puede ser numérico. `st.slider` sobre cualquier columna continua |
| No tengo columna numérica para KPIs | `len(df_filtrado)` es un KPI válido. También `nunique()` de una categórica |
| Mis columnas tienen tildes y espacios | Renómbralas en `RENOMBRES`, en la carga, una sola vez |
| Mi dataset tiene millones de filas | Agrega antes de graficar. Nunca le pases millones de puntos a Plotly |
| Tengo una sola columna categórica | Deriva otra: año, mes, rango de valores con `pd.cut` |

---

## Cuando algo falla

| Error | Solución |
|-------|----------|
| `command not found: streamlit` | `pip install streamlit`, o `python -m streamlit run app.py` |
| `ModuleNotFoundError: No module named 'streamlit'` | Está instalado en otro entorno. Compara `which python` y `which streamlit` |
| `Port 8501 is already in use` | `streamlit run app.py --server.port 8502` |
| La app no cambia cuando edito | Guarda el archivo y usa el botón "Rerun" arriba a la derecha |
| `KeyError: 'algo'` | Renombraste la columna y seguiste usando el nombre viejo |
| El gráfico de barras muestra valores gigantes | Falta el `groupby`. `px` no agrega por ti |
| La app va lentísima | Falta `@st.cache_data` en la función de carga |
| No pasa nada al ejecutar el `.py` con el botón de play | Streamlit solo corre con `streamlit run archivo.py` desde la terminal |

Para detener la app: `Ctrl+C` en la terminal. Cerrar la pestaña del navegador no la apaga.

---

## Qué hacer en casa

En el bloque asistido alcanzas a tener la app corriendo con lo mínimo. El cierre es en casa:

- [ ] Revisar que los 3 KPIs sean los que importan, no los que fueron fáciles de calcular.
- [ ] Reescribir los 3 títulos como mensajes.
- [ ] Recorrer las cuatro preguntas del paso 4 con la app abierta, y probarla además con filtros
      extremos: todo seleccionado, nada seleccionado, un solo valor.

**Opcional, no se evalúa hoy:** `st.tabs` para organizar secciones, `st.download_button` para
exportar el filtrado, temas y colores personalizados, mapas con `px.scatter_map`, despliegue en
Streamlit Community Cloud. Nada de esto suma nota si lo básico no corre.

---

## Cómo se conecta con la evaluación

| Hoy | Clase 11 |
|-----|----------|
| App con 3/3/3 corriendo | La misma app, pulida |
| Un `st.info` con el insight | La narrativa de la clase 8 sobre esta app |
| Práctica, sin banda registrada | Turno de 10 min (7 de exposición con corte duro + 2 de preguntas + 1 de transición), con banda de Saber, Ser y Hacer en el acta |

**El Momento 2 no produce nota.** Produce retroalimentación por dimensión y un **cumplido / no
cumplido** que **habilita el Momento 3**, que es la única evaluación calificada del semestre. Que no
dé nota no lo hace opcional: sin cumplir el M2 no hay M3, y sin M3 no hay nota del curso.

Los retos semanales, este incluido, **no producen nota ni cumplido / no cumplido**: son práctica, y
su retroalimentación usa el mismo lenguaje de bandas para que llegues familiarizado al momento.

La clase 10 es el laboratorio de ensayo. Llega con la app funcionando.
