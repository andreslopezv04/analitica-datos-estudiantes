# Clase 5 · Reto — Análisis bivariado de 25.000 resultados del Saber Pro

## De qué se trata

En el demo trabajamos con el consumo de agua de Caldas: siete columnas numéricas y una relación que
todo el mundo esperaba. Aquí hay 25.362 estudiantes, 48 columnas y una pregunta con consecuencias
públicas: ¿los colegios privados producen mejores resultados, o eso es un espejismo de composición?

Su trabajo: aplicar el **marco bivariado de 5 pasos** sobre datos que no vio, y ejecutar un **chequeo
de paradoja de Simpson** que puede tumbar la conclusión obvia.

| Campo | Valor |
|-------|-------|
| Archivo de trabajo | `reto.ipynb` |
| Dataset | `../datos/saber_pro.csv` |
| Tiempo en el salón | 50 minutos |
| Se termina | En casa (parte D y el repaso de interpretaciones) |
| Entrega | El notebook completado, corriendo de arriba a abajo sin errores |

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las once tareas trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que va a usar, escritas de forma genérica |
| **Lo que decide usted** | Qué columna, qué lista, qué orden. Ahí no hay respuesta escrita |
| **La celda de código** | Los pasos numerados en comentarios; las líneas las escribe usted |
| **La comprobación** | `comprobar('TN', ...)` dice si el resultado es el correcto, sin mostrarlo |

**Por qué esto sigue siendo un reto.** Le damos el camino, pero el camino lo recorre usted sobre un
dataset que no vio en el demo: elige la columna entre 48, decide qué gráfico corresponde a cada par
de tipos, y **dice qué significa el número que sale**. La técnica se guía; el criterio no, y el
criterio es lo que se evalúa. Las celdas `comprobar(...)` comparan una huella digital de su resultado
con la esperada: nunca revelan la respuesta, y escribir cualquier cosa hasta que pasen es engañarse
en el propio entregable.

**Las tareas de gráfico se comprueban distinto.** No hay una única respuesta correcta para un
gráfico, así que `comprobar_grafico(...)` revisa que esté dibujado, titulado y con los dos ejes
etiquetados, y en el heatmap además que la escala de color vaya de -1 a 1. Es exactamente lo que pide
la rúbrica.

---

## El dataset

**Origen:** resultados de las pruebas Saber Pro, el examen de Estado que presentan los estudiantes
universitarios colombianos al final de su carrera. ICFES, vía datos.gov.co.

**Tamaño:** 25.362 filas x 48 columnas. Una fila = un estudiante, entre 2018 y 2022.

### Los seis puntajes

| Columna | Qué mide |
|---------|----------|
| `puntaje_global` | Puntaje total. **Es un compuesto de los otros cinco.** Ver la advertencia 2 |
| `punt_comp_ciud` | Competencias ciudadanas |
| `punt_comu_escr` | Comunicación escrita |
| `punt_ingles` | Inglés |
| `punt_lect_crit` | Lectura crítica |
| `punt_razo_cuant` | Razonamiento cuantitativo |

### Las variables categóricas

| Columna | Valores |
|---------|---------|
| `estrato` | `Estrato 1` a `Estrato 6`, más `ND/NE` |
| `tipo_col` | `Oficial`, `Privado`, `Otros`, `Sin datos` |
| `sexo` | `Hombres`, `Mujeres` |
| `areac_snies` | Área de conocimiento del programa (7 categorías) |
| `year` | 2018 a 2022 |

### Tres advertencias antes de escribir la primera línea

**1. Los faltantes están disfrazados de dato.** Las columnas de puntaje usan **-89** como código de
dato faltante. No es un puntaje negativo: es un centinela.

| Columna | Registros con -89 |
|---------|-------------------|
| `punt_comu_escr` | 427 |
| `punt_ingles` | 29 |
| `punt_comp_ciud` | 19 |
| `punt_lect_crit` | 8 |
| `punt_razo_cuant` | 5 |

Es peor que una celda vacía: `NaN` avisa, el -89 no. Entra en la media, arrastra todas las
correlaciones hacia abajo y aparece como outlier fantasma en todos los boxplots. El cuaderno trae la
celda de limpieza escrita, pero **usted tiene que entender por qué está ahí**: es exactamente el tipo
de sorpresa que la clase 3 enseñó a buscar.

**2. `puntaje_global` no cuenta como hallazgo.** Se calcula a partir de los otros cinco puntajes, así
que correlaciona alto con todos **por construcción, no por descubrimiento**. Reportar "descubrí que
el puntaje global correlaciona 0,75 con lectura crítica" no es descubrir nada: es descubrir cómo se
calcula el puntaje global. Cuando le pidan las correlaciones más fuertes, va excluido, y el cuaderno
le deja la lista lista para eso.

**3. Numérico no es lo mismo que cantidad.** `cod_dep_nac`, `snies_progra` y `lat_ciu_nac` son
números y son, respectivamente, un código, un identificador y una coordenada. Correlacionarlos no
significa nada, y ninguna herramienta se lo va a impedir.

---

## Las tareas

### Paso 0 · Cargar, limpiar y reconocer (5 min)

Cuatro celdas ya escritas: preparación, carga, las listas de columnas y la limpieza de los -89.
Ejecútelas, léalas, y **deje a la vista la salida de reconocimiento**: de ahí salen los nombres
exactos de las categorías.

### Parte A · Correlaciones entre puntajes (aprox. 18 min)

Objetivo: los pasos 2 y 3 del marco sobre pares de variables numéricas.

1. **La matriz de los seis puntajes.** Todos los r contra todos.
2. **El heatmap de esa matriz**, con `center=0`. Sin eso el color miente y el gráfico no sirve.
3. **Las tres correlaciones más fuertes**, excluyendo la diagonal y excluyendo `puntaje_global`, cada
   una explicada: qué mide cada variable, si la relación tiene sentido, qué confusora podría haber
   detrás.
4. **El scatter del par más fuerte.** Mirar la nube después del número, y decir si el número escondía
   una curva, outliers o grupos.

Hay además dos preguntas de lectura: qué fila del heatmap se ve pálida y por qué, y por qué
`punt_comu_escr` se comporta distinto de todos los demás módulos.

### Parte B · Categórica contra numérica (aprox. 12 min)

Objetivo: el otro caso de la tabla de elección de gráfico.

5. **Boxplot de `puntaje_global` por `estrato`**, con el orden lógico forzado.
6. **Boxplot de `puntaje_global` por `tipo_col`.** Aquí no hay orden natural, y saber por qué es la
   mitad de la tarea.
7. **Las medias por estrato, con su conteo.** Una media sin su conteo no se interpreta.

Y tres preguntas de interpretación, que son las que se leen en Saber: qué patrón hay, qué **no** se
puede concluir de él —con dos confusoras nombradas— y qué grupo es demasiado pequeño para confiar.

### Parte C · Chequeo de paradoja de Simpson (aprox. 17 min)

**Es la parte que más pesa, y la única donde se le listan los comandos pero no el orden.**

El punto de partida: los colegios privados tienen media más alta que los oficiales. La pregunta:
**¿esa ventaja sobrevive al partir por estrato, o era solo un efecto de composición?**

8. **El resultado global**: media y conteo de `puntaje_global` por tipo de colegio.
9. **El resultado partido**: la tabla cruzada de estrato contra tipo de colegio.
10. **Los tamaños de cada celda del cruce.** Sin esto, la tabla anterior es interpretable a medias.
11. **La comparación**: los dos tipos que se comparan, los seis estratos, y la diferencia.

Después, cuatro preguntas de conclusión. **El entregable es el chequeo, no la paradoja.** Si la
relación se sostiene, ese es un resultado completo y correcto: que resista la partición la hace más
creíble, no menos. Forzar los datos hasta sacar un titular es lo contrario de lo que esta clase
enseña.

### Parte D · Reflexión (en casa)

Tres preguntas: reescribir un titular causal para que sea defendible, cómo protegerse de reportar una
correlación espuria con 48 columnas encima, y qué análisis bivariado va a llevar al Momento 1 con el
dataset de su equipo.

### Opcional · Solo si terminó todo

No se comprueba y no entra en la retroalimentación: un segundo chequeo de Simpson por `sexo` partido
por área de conocimiento, un pair plot de los cinco módulos, y las correlaciones contra `edad` y
`pbm`.

---

## Cómo se entrega

1. Complete `reto.ipynb`.
2. Antes de entregar: **Kernel → Restart and Run All**. Si algo revienta, arréglelo. Un notebook que
   no corre de arriba a abajo le pone techo a Hacer.
3. Ejecute el punto de control y verifique que las once tareas están correctas.
4. Guárdelo como `reto_clase05_APELLIDO.ipynb` y súbalo antes del inicio de la clase 6.

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegue familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | La explicación de las 3 correlaciones más fuertes sin `puntaje_global`, la lectura de la comparación por categorías incluyendo qué **no** se puede concluir, y entender qué produce una paradoja de Simpson |
| **Ser** | La conclusión honesta del chequeo —incluida la de que no aparece paradoja, si no aparece—, el reconocimiento de los grupos demasiado pequeños, y las 3 preguntas de reflexión respondidas con criterio |
| **Hacer** | Las once tareas correctas según el punto de control, la parte C armada por usted, y el notebook corriendo completo con Restart & Run All |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Afirmar causalidad —"el estrato determina el puntaje", "estudiar en colegio privado mejora el
  resultado"— aunque todo el código esté bien: **Saber** no pasa de Insuficiente. La forma correcta
  es "se observa una asociación entre X e Y", y después nombrar las confusoras plausibles.
- Reportar `puntaje_global` como hallazgo: **Saber** no pasa de Aceptable.
- El notebook no corre con Restart & Run All: **Hacer** no pasa de Aceptable.
- Heatmap sin `center=0`: **Hacer** no pasa de Bueno.

## Si se atasca

| Síntoma | Qué revisar |
|---------|-------------|
| `FileNotFoundError` | La ruta es `../datos/saber_pro.csv`, relativa al cuaderno. `import os; print(os.getcwd())` |
| El heatmap sale ilegible | Metió más columnas de la cuenta. Solo van los seis puntajes: use `columnas_puntaje` |
| Su correlación más fuerte incluye `puntaje_global` | Usó la lista equivocada. Es `columnas_modulo` |
| `comprobar_grafico` dice que el eje está en `None` | No guardó lo que devuelve seaborn: `eje = sns.boxplot(...)` |
| `comprobar_grafico` dice que falta título o etiqueta | `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`. Se califican |
| La tabla cruzada sale con `NaN` en una celda | No es un error: es que no hay ningún estudiante en esa combinación. Mírelo en la tabla de tamaños |
| `MatplotlibDeprecationWarning` al dibujar un boxplot | Viene de dentro de seaborn, no de su código. No afecta nada. Ignórelo |

## Enlaces

- El `demo/demo.ipynb` de esta misma clase tiene el marco bivariado aplicado paso por paso, incluido
  el chequeo de Simpson y las cuatro cosas que el coeficiente r no ve. Úselo de referencia.
- Guía de entrega del Momento 1 y qué hace que un dataset sirva:
  `evaluaciones/momento1/guia_entrega.md`, sección 3. Fuente única: los criterios no se duplican aquí.
- Fuente del dataset: https://www.datos.gov.co/resource/g6ci-7e9g
- Correlaciones espurias: https://tylervigen.com/spurious-correlations
