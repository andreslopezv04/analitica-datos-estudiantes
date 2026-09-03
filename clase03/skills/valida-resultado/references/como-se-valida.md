# Como se valida, y como cada oficio arma sus propias preguntas

Referencia de apoyo del skill. No se pega en el chat: se consulta cuando una validacion cuesta.

El skill valida contra el criterio de aceptacion del encargo, condicion por condicion. Eso es el
**procedimiento**, y es igual en cualquier trabajo. Lo que cambia de un oficio a otro es **que hay
que mirar**, y eso el skill no lo puede traer escrito: lo pone quien conoce el oficio.

---

## De un criterio a una lista de condiciones

Un criterio de aceptacion util se parte solo. Uno malo no se puede partir, y descubrirlo aqui ya es
un hallazgo.

| Criterio del encargo | Condiciones que salen |
|----------------------|-----------------------|
| "El promedio mensual por hogar residencial queda entre 10 y 40 metros cubicos, en una tabla de tres filas" | 1. El resultado tiene tres filas. 2. La unidad es metros cubicos al mes. 3. Ninguna cifra sale del rango 10 a 40. 4. Solo entraron hogares residenciales |
| "El informe cabe en dos paginas y cada recomendacion cita la seccion que la sostiene" | 1. Son dos paginas o menos. 2. Cada recomendacion trae una cita. 3. Cada cita apunta a una seccion que existe |
| "Que quede bien" | Ninguna. El encargo quedo corto: vuelva a especificar |

**La regla practica:** si no puede escribir como se comprobaria una condicion sin discutir con
nadie, esa condicion todavia no esta escrita.

---

## Las tres respuestas, y por que son tres

- **Si**: se comprobo y cumple. Con la evidencia al lado, no de memoria.
- **No**: se comprobo y no cumple. Va con el tramo del bucle al que hay que volver.
- **No se puede saber**: falta el dato para contestar. Es una respuesta legitima y **obligatoria**
  cuando corresponde.

El tercer caso es el que la gente se salta, y es el mas valioso: dice que el encargo no dejo forma
de comprobar algo que si importaba. Un "si" prudente en su lugar es peor que el hueco, porque el
hueco al menos se ve.

---

## Lo que el criterio nunca cubre

Ningun criterio de aceptacion lo previo todo. Por eso el skill pide una seccion aparte para lo que
extrana aunque ninguna condicion lo prohiba. Ahi entran:

- El resultado que cumple todo y aun asi no se puede defender delante de nadie
- Lo que se produjo de mas, sin que nadie lo pidiera
- La lectura equivocada que alguien podria hacer, y a quien perjudicaria

No cambia el veredicto. Es la materia prima de la siguiente vuelta del encargo.

---

## Un ejemplo trabajado: las cuatro preguntas del analista

Cada oficio termina destilando su criterio en un puñado de preguntas rapidas, las que su gente se
hace siempre antes de dar algo por bueno. Un corrector tiene las suyas, un contador tiene las
suyas. **Este es el juego de un analista de datos**, y esta aqui como ejemplo de la forma que tiene
un juego de esos, no como regla del skill.

| # | Pregunta | Que caza |
|---|----------|----------|
| 1 | El numero tiene sentido | El resultado bien calculado sobre los datos equivocados |
| 2 | La forma cuadra | El filtro que se llevo la mitad de las filas sin avisar |
| 3 | Responde lo que se pregunto | El analisis impecable de otra pregunta |
| 4 | Cambio algo | La operacion que no hizo nada, o que hizo demasiado |

### 1. El numero tiene sentido

El consumo promedio mensual del estrato 3 dio **411,2 metros cubicos**. El codigo corrio, no hubo
error, salieron tres filas, una por estrato, que es exactamente la forma que pedia el criterio. Y el
resultado no sirve: un hogar gasta entre 10 y 40 metros cubicos al mes. Habia suscriptores
industriales mezclados con los residenciales.

Es la unica de las cuatro que ninguna herramienta hace sola, porque la respuesta no esta en los
datos: esta en lo que usted sabe del mundo.

### 2. La forma cuadra

Se esperaban 27 filas, una por departamento. Salieron 34, porque la columna traia `ANTIOQUIA`,
`Antioquia` y `antioquia` como categorias distintas.

### 3. Responde lo que se pregunto

El encargo pedia el consumo **por hogar**. El resultado trae el consumo **total por municipio**. Los
dos son correctos; solo uno responde. Es el error mas caro porque no se nota.

### 4. Cambio algo

Un `dropna()` que dejo el mismo numero de filas: o no habia nulos, o se aplico a la columna
equivocada. Y un `dropna()` que dejo 12 filas de 9.000: tecnicamente hizo su trabajo, y se llevo el
dataset.

### Como se arma un juego propio

Mire las tres o cuatro formas en que su oficio se equivoca de verdad, no las que suenan graves.
Cada pregunta del juego caza una de ellas, se contesta en menos de un minuto, y se puede hacer sin
volver a producir nada. Si una pregunta necesita rehacer el trabajo para contestarse, no es una
pregunta rapida: es otro paso del plan.

---

## La regla del retorno

Cuando la validacion falla, se vuelve a **especificar**. No se parcha el resultado.

Un resultado que responde otra cosa casi siempre viene de un encargo que pedia otra cosa. Arreglar
la salida esconde el problema y lo devuelve la proxima vez, cuando ya nadie se acuerde de por que
estaba ese filtro raro en la linea 40.

En el ejemplo del estrato 3: la tentacion es escribir "descartar los mayores a 100" y seguir. El
numero queda bonito de una vez. Lo correcto es volver al encargo, agregar la columna `USO` a los
insumos que hace falta mirar, y declarar que el encargo cubre solo suscriptores residenciales. La
segunda vuelta da 26,8, y esta vez el resultado se puede defender.

**Que se pierde exactamente si se parcha:** el umbral de 100 queda sin razon escrita, nadie sabe de
donde salio, y el dia que aparezca un hogar con piscina de 120 metros cubicos, el filtro se lo lleva
sin avisar.
