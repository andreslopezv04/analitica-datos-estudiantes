# Clase 4 · Reto — El campo colombiano en tres variables

## De qué se trata

En el demo aplicó el marco univariado de 5 pasos a una variable de consumo de agua, con el profesor
al lado. Aquí hay 20.000 registros de producción agrícola de todo el país, y el marco se aplica tres
veces: la primera a mano, paso por paso; las otras dos con una función que ya está escrita.

Su trabajo: resolver **diez tareas**, y escribir qué significa cada número que sale.

| Campo | Valor |
|-------|-------|
| Bloque | 3 (es el entregable de la clase) |
| Archivo de trabajo | `reto_starter.ipynb` |
| Dataset | `../datos/evaluaciones_agropecuarias.csv` |
| Tamaño | 20.000 filas x 17 columnas |
| Fuente | Evaluaciones Agropecuarias Municipales (EVA), Ministerio de Agricultura, vía datos.gov.co |
| Tiempo en el salón | 60 minutos |
| Se termina | En casa (partes 5 y 6, la tabla resumen y la reflexión) |
| Trabajo | Individual o en pareja |
| Entrega | El cuaderno completado, corriendo de arriba a abajo sin errores |

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las diez tareas trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que va a usar, escritas de forma genérica |
| **Lo que decide usted** | Qué columna, qué operación, qué criterio. Ahí no hay respuesta escrita |
| **La celda de código** | Los pasos numerados en comentarios; las líneas las escribe usted |
| **La comprobación** | `comprobar('TN', ...)` dice si el resultado es el correcto, sin mostrarlo |

**Por qué esto sigue siendo un reto.** Le damos el camino, pero el camino lo recorre usted sobre un
dataset que no vio en el demo: elige la columna, elige la operación, **clasifica la forma de la
distribución** y **decide qué hacer con los outliers**. Las dos últimas no las resuelve ninguna
función. La técnica se guía; el criterio no, y el criterio es lo que se evalúa. Las celdas
`comprobar(...)` comparan una huella digital de su resultado con la esperada: nunca revelan la
respuesta, y escribir cualquier cosa hasta que pasen es engañarse en el propio entregable.

---

## El dataset

Las Evaluaciones Agropecuarias Municipales son el censo anual de producción agrícola de Colombia.

**Granularidad:** una fila = **un cultivo, en un municipio, en un año** (2017 o 2018). 32
departamentos, 13 grupos de cultivo.

Las tres variables del reto:

| Columna | Qué es | Unidad |
|---------|--------|--------|
| `producci_n_t` | Producción cosechada | toneladas |
| `rea_sembrada_ha` | Área sembrada | hectáreas |
| `rendimiento_t_ha` | Rendimiento: producción dividida por área | toneladas por hectárea |

Las que se usan para agrupar:

| Columna | Qué es |
|---------|--------|
| `departamento` | Uno de 32 departamentos |
| `municipio` | Municipio |
| `grupo_de_cultivo` | 13 grupos: FRUTALES, CEREALES, OLEAGINOSAS, TUBERCULOS Y PLATANOS, ... |
| `ciclo_de_cultivo` | TRANSITORIO, PERMANENTE o ANUAL |
| `cultivo` | Nombre del cultivo |
| `a_o` | Año: 2017 o 2018 |

**Tres cosas que hay que saber antes de escribir la primera línea:**

1. **Los nombres de columna están mal escritos, y son los reales.** `rea_sembrada_ha` perdió la "á"
   de "área" y `producci_n_t` perdió la "ó" de "producción" al exportarse desde datos.gov.co.
   Cópielos de `df.columns.tolist()`; no los teclee.
2. **Todo el texto está en MAYÚSCULAS y sin tildes.** Filtrar por `'Antioquia'` devuelve cero filas.
3. **Una de las tres variables tiene valores faltantes.** Cuál es, y por qué, es la tarea 1.

Este dataset **no** se limpia hoy: viene sin el problema de separadores de miles que tenía el de
Empocaldas.

---

## Las tareas

### Paso 0 · Cargar y reconocer (5 min)

Las celdas ya están escritas. Ejecútelas y **deje la salida a la vista**: de ahí va a copiar los
nombres exactos de columnas, grupos y ciclos.

### Parte 1 · Paso 1 del marco: identificar (5 min)

Objetivo: mirar la variable antes de calcular nada sobre ella.

1. **Los faltantes.** ¿Cuál de las tres variables tiene valores faltantes y cuántos? Y una frase: por
   qué esa y no las otras dos.

### Parte 2 · Pasos 2 y 3 sobre `producci_n_t` (15 min)

Objetivo: centro y dispersión, calculados a mano una vez.

2. **El centro.** Media, mediana y moda de la producción, y la razón media/mediana.
3. **La dispersión.** Q1, Q3, desviación estándar y el IQR.

### Parte 3 · Pasos 4 y 5 sobre `producci_n_t` (15 min)

Objetivo: las dos partes del marco donde ninguna función responde por usted.

Antes de las tareas hay una celda de acción sin comprobación: el histograma y el boxplot de la
variable, con título y los dos ejes etiquetados.

4. **La forma.** Clasificar la distribución: normal, sesgada a la derecha, sesgada a la izquierda o
   bimodal. Una sola palabra, y tiene que ser coherente con la razón de la tarea 2.
5. **Los outliers.** Los dos límites de la regla 1.5xIQR y el conteo de registros marcados. Después,
   con la tabla de los diez mayores a la vista, la decisión argumentada: ¿se conservan?

### Parte 4 · Las otras dos variables, con la función ya escrita (10 min)

Objetivo: reconocer que es el mismo procedimiento, y compararlas.

6. **`rea_sembrada_ha`**, el área sembrada.
7. **`rendimiento_t_ha`**, el rendimiento. Es un **cociente**, y ahí está el punto de la parte: la
   razón media/mediana cae muchísimo respecto a las otras dos. Hay que explicar por qué, y mirar los
   seis rendimientos más altos antes de decidir si se conservan.

### Parte 5 · GroupBy (10 min en clase, se termina en casa)

Objetivo: pasar de un número único a la comparación entre grupos. Las tres decisiones de los M&Ms.

8. **Producción media por grupo de cultivo.** Cuál encabeza, y por qué FLORES Y FOLLAJES queda a
   mitad de tabla pese a ser un renglón exportador clave.
9. **Rendimiento mediano por ciclo de cultivo.** Mediana y no media, y hay que saber decir por qué.

### Parte 6 · Una pregunta que usted arma sola (en casa)

Objetivo: el ensamblaje. El cuaderno lista todos los comandos que entran en juego, pero **no el
orden**. Es deliberado: en los momentos evaluativos nadie le va a dar la secuencia.

10. **Los grandes productores, ¿son los más eficientes?** Entre los 5 departamentos con mayor
    producción total, cuál tiene el rendimiento mediano más alto.

### Cierre (en casa)

- **La tabla resumen:** las tres variables en una sola vista, más una frase por variable **sin ningún
  número**.
- **Tres preguntas de reflexión**, una de ellas sobre el dataset del proyecto de su equipo.

### Opcional · Solo si terminó todo

No se comprueba ni entra en la retroalimentación: histograma en escala logarítmica, los tres boxplots
lado a lado, y producción total por departamento en barras horizontales.

---

## Cómo se entrega

1. Complete `reto_starter.ipynb`.
2. Antes de entregar: **Kernel → Restart and Run All**. Si algo revienta, arréglelo. Un cuaderno que
   no corre de arriba a abajo le pone techo a Hacer.
3. Súbalo al aula virtual con el nombre `clase04_reto_APELLIDO.ipynb`.
4. Fecha límite: antes del inicio de la clase 5.

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegue familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | Las frases de interpretación: qué significa cada número. La razón media/mediana traducida a una frase sobre el campo colombiano, la comparación de las tres razones en la tarea 7, y la tabla resumen con sus tres frases sin números |
| **Ser** | La decisión sobre los outliers **argumentada** en lugar de aplicada por defecto, sobre todo el contraste entre la tarea 5 (caña azucarera: se conservan) y la 7 (rendimientos de tomate: se marcan y se consultan), y las tres preguntas de reflexión |
| **Hacer** | Las diez tareas con el resultado correcto (el punto de control final las cuenta), la parte 6 armada por usted, los gráficos con título y ejes etiquetados, y el cuaderno corriendo completo con Restart & Run All |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Respuestas correctas sin ninguna frase de interpretación: **Saber** no pasa de Insuficiente. El
  número no es el análisis; la frase que lo explica sí.
- El cuaderno no corre con Restart & Run All: **Hacer** no pasa de Aceptable.
- Gráficos sin título o sin etiquetas de eje: **Hacer** no pasa de Bueno.

## Si se atasca

| Síntoma | Qué revisar |
|---------|-------------|
| `FileNotFoundError` | La ruta es `../datos/evaluaciones_agropecuarias.csv`, relativa al cuaderno. Verifique con `import os; print(os.getcwd())` |
| `KeyError` con el nombre de una columna | Los nombres reales están mutilados. `df.columns.tolist()` y copie y pegue |
| El histograma de `producci_n_t` sale como una sola barra | Es el resultado correcto: el sesgo es tan fuerte que todo se apila contra el cero. Es un hallazgo, no un fallo |
| `.quantile(25)` da un número absurdo y no da error | Recibe una fracción entre 0 y 1: `0.25`, no `25` |
| `TypeError` al combinar dos condiciones | Faltan paréntesis. Cada condición entre paréntesis, sin excepción |
| La tarea 6 o la 7 dicen "sigue valiendo None" | Llamó la función pero no guardó lo que devuelve en una variable |

## Enlaces

- El `demo/demo.ipynb` de esta misma clase tiene el marco de 5 pasos completo sobre otro dataset, con
  los recuadros que explican qué es una media, qué mide la desviación estándar y qué es un objeto
  agrupado. Úselo de referencia.
- Guía de entrega del Momento 1 y qué hace que un dataset sirva:
  `evaluaciones/momento1/guia_entrega.md`, sección 3. Fuente única: los criterios no se duplican aquí.
- Fuente del dataset: https://www.datos.gov.co/resource/2pnw-mmge
- Documentación de pandas sobre GroupBy:
  https://pandas.pydata.org/docs/user_guide/groupby.html
