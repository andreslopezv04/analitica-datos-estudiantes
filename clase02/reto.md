# Clase 2 · Reto — Filtrar 20.000 accidentes de tránsito

## De qué se trata

En el demo trabajamos con 318 filas de estados financieros. Aquí hay 20.000 filas de vehículos
involucrados en accidentes de tránsito en Colombia. La técnica es exactamente la misma; lo único
que cambia es que ahora sí importa saber filtrar, porque mirar 20.000 filas a ojo no es una opción.

Su trabajo: traducir 10 preguntas escritas en español a filtros de pandas, y escribir la respuesta
en una frase.

| Campo | Valor |
|-------|-------|
| Archivo de trabajo | `reto_starter.ipynb` |
| Dataset | `../datos/vehiculos_accidentes.csv` |
| Tiempo en el salón | 60 minutos |
| Se termina | En casa (partes 4 y 5) |
| Entrega | El notebook completado, corriendo de arriba a abajo sin errores |

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las diez tareas trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que va a usar, escritas de forma genérica |
| **Lo que decide usted** | Qué columna, qué valor, qué operador. Ahí no hay respuesta escrita |
| **La celda de código** | Los pasos numerados en comentarios; las líneas las escribe usted |
| **La comprobación** | `comprobar('TN', ...)` dice si el número es el correcto, sin mostrarlo |

**Por qué esto sigue siendo un reto.** Le damos el camino, pero el camino lo recorre usted sobre un
dataset que no vio en el demo: elige la columna, escribe el valor exacto tal como está en el dato,
decide el operador y **dice qué significa el número que sale**. La técnica se guía; el criterio no,
y el criterio es lo que se evalúa. Las celdas `comprobar(...)` comparan una huella digital de su
resultado con la esperada: nunca revelan la respuesta, y escribir cualquier cosa hasta que pasen es
engañarse en el propio entregable.

---

## El dataset

**Origen:** Ministerio de Transporte, publicado en datos.gov.co. Vehículos involucrados en
accidentes de tránsito registrados en Colombia entre diciembre de 2022 y diciembre de 2025.

**Tamaño:** 20.000 filas x 9 columnas. Una fila = un vehículo involucrado en un accidente.

| Columna | Qué es | Tipo | Ejemplos |
|---------|--------|------|----------|
| `marca_vehiculo` | Marca del vehículo | texto | AKT, YAMAHA, RENAULT, CHEVROLET |
| `modelo_vehiculo` | Año del modelo | entero | 2026, 2015, 1998 |
| `tipo_vehiculo` | Tipo de vehículo | texto | MOTOCICLETA, AUTOMOVIL, CAMIONETA, BUS |
| `edad_vehiculo` | Antigüedad en años al momento del accidente | decimal | 1.0, 10.0, 25.0 |
| `fecha_accidente` | Mes y año del accidente | texto | 12/2025, 12/2024 |
| `gravedad_accidente` | Gravedad | texto | CON HERIDOS, CON MUERTOS |
| `departamento_accidente` | Departamento | texto | ANTIOQUIA, VALLE DEL CAUCA |
| `municipio_accidente` | Municipio | texto | MEDELLIN, CALI, BARRANQUILLA |
| `autoridad_de_transito` | Autoridad que registró el caso | texto | STRIA DTAL TTO BARRANQUILLA |

**Tres cosas que hay que saber antes de escribir la primera línea:**

1. **Todo el texto está en MAYÚSCULAS y sin tildes.** Filtrar por `'Motocicleta'` devuelve cero
   filas. Filtrar por `'MOTOCICLETA'` funciona.
2. **`fecha_accidente` es texto**, no una fecha de verdad. Tiene el formato `12/2025`. Si necesita
   el año, `modelo_vehiculo` no sirve para eso (es el año del modelo, no del accidente). Hay una
   pista en la tarea correspondiente.
3. **`marca_vehiculo` tiene 4 valores vacíos** y `edad_vehiculo` tiene 1. No hay que arreglarlos
   hoy; solo hay que saber que están ahí, porque pueden hacer que algo se comporte raro.

Este dataset **no** se limpia hoy. La limpieza es la clase 3.

---

## Las tareas

### Paso 0 · Cargar y reconocer (5 min)

Las dos celdas ya están escritas. Ejecútelas y **deje la salida a la vista**: de ahí va a copiar y
pegar los valores exactos (`MOTOCICLETA`, `CON MUERTOS`, los departamentos) de casi todas las
tareas. Escribirlos de memoria es la causa número uno de "mi filtro devuelve 0 filas".

### Parte 1 · Una sola condición (12 min)

Objetivo: soltar la mano con el patrón `df[df['columna'] operador valor]`.

1. **Motocicletas.** ¿Cuántos de los 20.000 vehículos son motocicletas?
2. **Vehículos nuevos.** ¿Cuántos tienen un modelo de 2020 o posterior?
3. **Accidentes fatales.** ¿Cuántos registros corresponden a accidentes con muertos?

Cada respuesta es un número. Debajo, una frase suya interpretándolo.

### Parte 2 · Condiciones combinadas (15 min)

Objetivo: `&`, `|`, `~`, con paréntesis en cada condición.

4. **Motos fatales.** ¿Cuántas motocicletas estuvieron en accidentes con muertos?
5. **Dos departamentos.** ¿Cuántos registros son de ANTIOQUIA o de VALLE DEL CAUCA?
6. **Todo menos motos.** ¿Cuántos vehículos **no** son motocicletas? Hágalo de dos formas
   distintas (con `!=` y con `~`) y verifique que dan el mismo número.

### Parte 3 · Métodos de conveniencia (13 min)

Objetivo: escribir filtros que se puedan leer.

7. **Transporte pesado y de pasajeros.** Cuente los vehículos cuyo tipo esté en la lista
   `['BUS', 'BUSETA', 'MICROBUS', 'CAMION']`. Primero escríbalo con tres `|`, después reescríbalo
   con `.isin()`. Compare las dos líneas y diga cuál preferiría leer dentro de seis meses.
8. **Vehículos casi nuevos.** ¿Cuántos vehículos tenían entre 0 y 3 años de antigüedad (ambos
   incluidos)? Use `.between()`.

### Parte 4 · Preguntas analíticas (15 min en clase, se termina en casa)

Objetivo: traducir una pregunta de negocio a un filtro. Aquí no hay ningún comando nuevo, y el
cuaderno se los lista todos; lo que no se le da es **el orden en que se arman**. Esa es la única
parte del reto donde el ensamblaje corre por su cuenta, y es deliberado: en los momentos
evaluativos nadie le va a dar la secuencia.

9. **Motos nuevas y fatales en el Eje Cafetero.** ¿Cuántas motocicletas de 3 años o menos
   estuvieron en accidentes con muertos en CALDAS, RISARALDA o QUINDIO? Muestre las columnas
   relevantes del resultado, no solo el conteo.
10. **¿Qué es más letal, una moto o un carro?** Calcule qué porcentaje de los accidentes de
    motocicleta fueron con muertos, y qué porcentaje de los accidentes de automóvil fueron con
    muertos. Compare los dos porcentajes y escriba una conclusión de dos frases.

    Pista de método: es un filtro dentro de otro filtro. Cuente cuántas motos hay en total, cuente
    cuántas motos con muertos hay, y divida.

### Parte 5 · Reflexión (en casa)

Responda en el notebook, en español, dos o tres frases por pregunta:

- ¿Cuál de las 10 tareas le costó más y por qué?
- Piense en el dataset que su equipo eligió para el proyecto. Escriba **una** pregunta que se
  respondería con un filtro, y el filtro que la respondería (no tiene que ejecutarlo).

### Opcional · Solo si terminó todo

- `.str.contains()`: ¿cuántos accidentes ocurrieron en 2024? La columna `fecha_accidente` es texto
  con formato `12/2024`. Investigue `.str.contains('2024')`. Advertencia: si la columna tiene
  nulos, va a necesitar el parámetro `na=False`. Esto se ve formalmente en la clase 3.
- ¿Cuáles son las 5 marcas con más accidentes? Investigue `.value_counts()`.

---

## Cómo se entrega

1. Complete `reto_starter.ipynb`.
2. Antes de entregar: **Kernel → Restart and Run All**. Si algo revienta, arréglelo. Un notebook
   que no corre de arriba a abajo le pone techo a Hacer.
3. Súbalo al aula virtual con el nombre `clase02_reto_APELLIDO.ipynb`.
4. Fecha límite: antes del inicio de la clase 3.

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegue familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | Las frases de interpretación: qué significa cada número que obtuvo. En la tarea 10, la comparación de los dos porcentajes y la conclusión |
| **Ser** | La reflexión de la parte 5: reconocer qué le costó, y llevar el filtro al dataset propio del proyecto |
| **Hacer** | Las tareas 1 a 8 con el filtro correcto (el punto de control final las cuenta), la parte 4 armada por usted, y el notebook corriendo completo con Restart & Run All |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Respuestas correctas sin ninguna frase de interpretación: **Saber** no pasa de Insuficiente. El
  número no es el análisis; la frase que lo explica sí.
- El notebook no corre con Restart & Run All: **Hacer** no pasa de Aceptable.

## Si se atasca

| Síntoma | Qué revisar |
|---------|-------------|
| `FileNotFoundError` | La ruta es `../datos/vehiculos_accidentes.csv`, relativa al notebook |
| El filtro devuelve 0 filas | Ejecute `df['columna'].unique()`. Casi siempre es un tema de mayúsculas |
| `ValueError: truth value ... is ambiguous` | Usó `and` u `or`. Van `&` y `\|` |
| `TypeError` con `&` | Faltan paréntesis. Cada condición entre paréntesis, sin excepción |
| `KeyError` | Nombre de columna mal escrito. `df.columns.tolist()` y copie y pegue |

## Enlaces

- Guía de entrega del Momento 1 y qué hace que un dataset sirva:
  `evaluaciones/momento1/guia_entrega.md`, sección 3. Fuente única: los criterios no se duplican aquí.
- Documentación de pandas sobre boolean indexing:
  https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing
