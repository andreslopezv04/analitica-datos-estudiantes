# Clase 3 · Reto — Limpiar indicadores de salud materno-infantil

## De qué se trata

En el demo limpiamos estadísticas de educación. Aquí hay otro dataset del gobierno colombiano, con
otras columnas, otras unidades y los mismos 5 problemas. **El workflow se copia; la lista de
columnas no.**

Su trabajo: aplicar el workflow de 5 pasos de punta a punta sobre 532 registros de salud
materno-infantil, y **justificar por escrito cada decisión**. Un cuaderno con el código perfecto y
sin justificaciones deja Saber en el suelo.

| Campo | Valor |
|-------|-------|
| Archivo de trabajo | `reto_starter.ipynb` |
| Dataset | `../datos/indicadores_salud.csv` |
| Tareas | 11, comprobadas con `comprobar('TN', ...)` |
| Tiempo en el salón | 60 minutos |
| Se termina | En casa (parte 7 y reflexión) |
| Entrega | El cuaderno completado, corriendo de arriba a abajo sin errores |

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las once tareas trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que va a usar, escritas de forma genérica |
| **Lo que decide usted** | Qué columna, qué umbral, qué orden. Ahí no hay respuesta escrita |
| **La celda de código** | Los pasos numerados en comentarios; las líneas las escribe usted |
| **La comprobación** | `comprobar('TN', ...)` dice si el resultado es correcto, sin mostrarlo |

**Por qué esto sigue siendo un reto.** Le damos el camino, pero el camino lo recorre usted sobre un
dataset que no vio en el demo: decide **cuáles** columnas entran en cada lista (aquí no existe
`desercion`), qué hacer con lo que falta, cuál columna es un porcentaje y cuál una tasa por mil, y
**escribe por qué**. La técnica se guía; el criterio no, y el criterio es lo que se evalúa.

Las celdas `comprobar(...)` comparan una huella digital de su resultado con la esperada, calculada
contra el CSV real. Nunca revelan la respuesta: si no coincide, dan una pista dirigida al error más
probable. Escribir cualquier cosa hasta que pasen es engañarse en el propio entregable.

**El cuaderno se ejecuta en orden y una sola vez.** Las tareas modifican el DataFrame una encima de
la otra, así que repetir una celda cambia los números. Si se enreda: Kernel → Restart and Run All.

---

## El dataset

**Origen:** Ministerio de Salud y Protección Social, publicado en datos.gov.co. Indicadores de
mortalidad y morbilidad por municipio y año.

**Tamaño:** 532 filas x 15 columnas. Una fila = un municipio en un año, entre 2005 y 2020.

| Columna | Qué es | Unidad |
|---------|--------|--------|
| `cod_departamento` | Código DANE del departamento | entero |
| `departamento` | Nombre del departamento | texto |
| `cod_municipio` | Código DANE del municipio | texto (debería ser entero) |
| `municipio` | Nombre del municipio | texto |
| `ano` | Año del registro | decimal (debería ser entero) |
| `bajo_peso_nacer` | Nacidos con bajo peso | **porcentaje (0-100)** |
| `controles_prenatales` | Promedio de controles prenatales por gestante | número de controles |
| `fecundidad_adolescente` | Fecundidad en adolescentes | tasa por mil |
| `mortalidad_fetal` | Mortalidad fetal | tasa por mil |
| `mortalidad_general` | Mortalidad general | tasa por mil |
| `mortalidad_infantil` | Mortalidad en menores de 1 año | tasa por mil |
| `mortalidad_materna` | Mortalidad materna | tasa por cien mil |
| `mortalidad_neonatal` | Mortalidad neonatal | tasa por mil |
| `partos_cesarea` | Partos por cesárea | **porcentaje (0-100)** |
| `partos_institucionales` | Partos atendidos en institución de salud | **porcentaje (0-100)** |

**Tres cosas que hay que saber antes de escribir la primera línea:**

1. **La ruta sube un solo nivel** (`../datos/indicadores_salud.csv`), no dos como en el demo. El
   dataset del demo es compartido por varias clases y vive en la raíz; este es propio de la clase.
2. **La trampa de dominio.** Solo **tres** columnas son porcentajes de verdad y por lo tanto están
   acotadas entre 0 y 100: `bajo_peso_nacer`, `partos_cesarea` y `partos_institucionales`. Las
   columnas de mortalidad son **tasas por mil o por cien mil**: una `mortalidad_materna` de 422
   significa 422 muertes por cada cien mil nacidos vivos, y es un dato válido. Si valida mortalidad
   contra el rango 0-100 va a "corregir" datos que estaban perfectos, y el destrozo no deja rastro.
   Esta distinción no la puede hacer pandas: la hace usted, leyendo qué mide cada columna. Ese es
   exactamente el problema 5.
3. **`municipio` no se limpia.** Compruébelo usted mismo en la parte 5: ya está consistente.
   Estandarizar por reflejo una columna que no lo necesita es tan mal criterio como no estandarizar
   la que sí.

---

## Las tareas

### Parte 1 · Inspección (10 min)

El ritual completo **antes de tocar nada**. La forma, las columnas, los tipos y las primeras filas
ya están escritos; el resto es suyo.

1. **Cuantificar lo que falta.** Cuántas columnas están afectadas y cuál es el **porcentaje** de la
   peor. El conteo absoluto no sirve para decidir; el porcentaje sí.

Después, el **diagnóstico escrito**: los 5 problemas, dónde está cada uno y con qué comando lo
detectó. Esto es lo que se califica, no los comandos. Las casillas que todavía no puede llenar se
dejan en "por confirmar".

### Parte 2 · Valores nulos (12 min)

Escriba sus decisiones **antes** de programarlas, aplicando el marco:

| Nulos | Acción |
|-------|--------|
| > 50% | Considere eliminar la columna |
| < 5% | Elimine las filas |
| 5-50% | Rellene, con criterio de dominio |

Pista honesta: en este dataset **ninguna columna pasa del 50%**. Si concluye que hay que eliminar
una columna entera, revise la cuenta.

2. **Las filas sin departamento.** `dropna(subset=[...])`, y de paso vea cuánto se habría llevado un
   `dropna()` sin `subset`.
3. **Rellenar las tasas con la mediana**, cada columna con la suya. La lista de columnas sale de la
   tarea 1, no del demo.

### Parte 3 · Tipos de datos (12 min)

4. **`ano`**, de decimal a entero, con la secuencia segura: `to_numeric(errors='coerce')`, rellenar,
   `astype(int)`. La regla de orden es **rellenar primero, convertir después**.
5. **`cod_municipio`**, de texto a entero. Trae comas de miles (`44,001`) y el literal `sin dato`.
   Cuente cuántos valores no se pueden convertir, y justifique qué hace con ellos: un código DANE 0
   no existe.

### Parte 4 · Duplicados (8 min)

6. **Contar, ver y eliminar.** `duplicated(keep=False)` marca todas las copias, que es lo que sirve
   para verlas. Y responda: si una fila es un municipio en un año, ¿un duplicado aquí es siempre un
   error?

### Parte 5 · Inconsistencias de texto (10 min)

7. **Estandarizar `departamento`**: espacios, mayúsculas, tildes y puntuación. Cuente los valores
   únicos antes y después, e imprima la lista final para saber cuántos **deberían** ser. Verifique
   también `municipio`, y no lo toque.
8. **Los duplicados que acaba de crear.** Van a aparecer nuevos. Cuéntelos, elimínelos y explique
   por qué aparecieron.

### Parte 6 · Valores inválidos de dominio (12 min)

9. **Detectar.** Cuántos valores están fuera del rango 0-100 en las **tres** columnas de porcentaje.
   Elegir bien esas tres columnas es toda la tarea.
10. **Decidir y corregir**, sin perder filas. Dos caminos defendibles: convertir a `NaN` y rellenar
    con la mediana, o recortar al rango con `.clip(0, 100)`. Elija uno y **justifíquelo antes de
    programarlo**; la comprobación acepta los dos. Y no toque las columnas de mortalidad: explique
    en markdown por qué no.

### Parte 7 · Verificación final (en casa)

Aquí no hay comandos nuevos y el cuaderno se los lista todos, pero **no el orden**: el ensamblaje es
suyo. Es deliberado: en los momentos evaluativos nadie le va a dar la secuencia.

- **Antes y después.** Compare `df_original` con `df` en seis dimensiones: filas, celdas vacías,
  duplicados, departamentos únicos y los tipos de `ano` y `cod_municipio`. La salida **es** la
  evidencia de que la limpieza sirvió.
11. **Una pregunta de verdad.** Los 5 municipios con mayor `mortalidad_infantil`. Y la pregunta
    incómoda: ¿cuánto confía en ese ranking, sabiendo que usted rellenó cerca del 11% de esa columna?

### Reflexión (en casa)

Tres preguntas en el cuaderno, dos o tres frases cada una: cuál problema fue el más difícil de
detectar, cuál de sus decisiones podría cambiar una conclusión posterior, y qué problemas espera
encontrar en el dataset de su equipo.

### Opcional · Solo si terminó todo

- Exportar el dataset limpio a CSV.
- Escribir una función `diagnostico(datos)` que imprima el resumen de los 5 problemas de cualquier
  DataFrame. Es la parte automatizable del oficio, y la va a agradecer en el Momento 1.
- Repetir la tarea 10 con el **otro** camino y ver si cambia el ranking de la tarea 11.
- Detección de outliers con el rango intercuartílico. Se ve formalmente en la clase 4.

---

## Cómo se entrega

1. Complete `reto_starter.ipynb`.
2. Antes de entregar: **Kernel → Restart and Run All**. Si algo revienta, arréglelo. Un cuaderno que
   no corre de arriba a abajo le pone techo a Hacer.
3. Ejecute el punto de control y deje la salida a la vista.
4. Súbalo al aula virtual con el nombre `clase03_reto_APELLIDO.ipynb`.
5. Fecha límite: antes del inicio de la clase 4.

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegue familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | El diagnóstico de la parte 1 y la **justificación escrita de cada decisión**, incluida la de por qué no tocó las columnas de mortalidad |
| **Ser** | La reflexión final: reconocer qué decisión propia podría cambiar una conclusión posterior, y anticipar qué problemas espera en el dataset de su equipo |
| **Hacer** | Las once tareas correctas (el punto de control final las cuenta), la parte 7 armada por usted, y el cuaderno corriendo completo con Restart & Run All |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Código correcto sin justificaciones escritas: **Saber** no pasa de Insuficiente. En limpieza de
  datos la justificación pesa más que el código: el código lo escribe cualquiera, la decisión la
  defiende usted.
- "Corregir" las columnas de mortalidad contra el rango 0-100: **Saber** no pasa de Insuficiente. Es
  el error de dominio que este reto existe para provocar.
- El cuaderno no corre con Restart & Run All: **Hacer** no pasa de Aceptable.

## Si se atasca

| Síntoma | Qué revisar |
|---------|-------------|
| `FileNotFoundError` | La ruta es `../datos/indicadores_salud.csv`, **un** nivel de subida (el demo usaba dos) |
| `IntCastingNaNError` | Está convirtiendo a entero con nulos presentes. Rellene primero |
| `ValueError: invalid literal for int()` | `astype(int)` sobre texto sucio. Use `pd.to_numeric(..., errors='coerce')` |
| `KeyError: 'desercion'` | Copió la lista de columnas del demo. Este dataset no tiene esa columna |
| `AttributeError: Can only use .str accessor...` | Está aplicando `.str` a una columna numérica. Revise `dtypes` |
| El DataFrame quedó casi vacío | Usó `dropna()` sin `subset` |
| Una comprobación deja de coincidir sin motivo | Ejecutó dos veces una celda que modifica `df`. Restart and Run All |
| Siguen apareciendo duplicados | Estandarizó el texto después de borrarlos. Vuelva a correr `duplicated()` |
| "Corrigió" mortalidad y ahora los números se ven raros | Mortalidad no es un porcentaje. Vuelva a la tabla de unidades de arriba |

## Enlaces

- Guía de entrega del Momento 1: `evaluaciones/momento1/guia_entrega.md`.
- Documentación de pandas sobre datos faltantes:
  https://pandas.pydata.org/docs/user_guide/missing_data.html
