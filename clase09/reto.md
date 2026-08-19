# Clase 9 · Reto — La historia de tu proyecto en 4 slides

## De qué se trata

En el demo se contó la brecha del presupuesto nacional: 92 billones comprometidos, 25 pagados, y una
cifra de 28,85 que aparecía sola cuando se cambiaba el recorte. Aquí haces lo mismo **con el dataset
de tu equipo**, el que vienes usando desde el Momento 1.

Tu trabajo: calcular las tres cifras que sostienen tu historia, escribir los cuatro títulos que la
cuentan, y presentarla en 5 minutos.

| Campo | Valor |
|-------|-------|
| Archivo de trabajo | `reto.ipynb` |
| Dataset | **El de tu equipo.** No hay CSV asignado |
| Tiempo en el salón | 60 minutos (25 de construcción, 25 de pitches, 10 de instrucción y cierre) |
| Se termina | En casa: aplicar el feedback y ensayar con cronómetro |
| Entrega | El notebook completado, corriendo de arriba a abajo sin errores, más el mini-deck |

Este es el ensayo directo de la sustentación del **Momento 2 (clase 12)**.

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las nueve tareas trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que vas a usar, escritas de forma genérica |
| **Lo que decides tú** | Qué columna, qué recorte, qué frase. Ahí no hay respuesta escrita |
| **La celda** | Los pasos numerados en comentarios; las líneas las escribes tú |
| **La comprobación** | `comprobar_cifra`, `revisar_titulo` o `comprobar_coherencia`, según el caso |

Las nueve tareas están repartidas en tres partes:

| Parte | Tareas | Qué se hace |
|-------|--------|-------------|
| **A · Las cifras** | T1 a T3 | La cifra principal, el recorte que le da nombre propio, la segunda evidencia |
| **B · Las cuatro slides** | T4 a T7 | Contexto, hallazgo, implicación y acción |
| **C · La prueba** | T8 y T9 | Los cuatro títulos leídos seguidos, y la cifra del hallazgo recalculada desde cero |

**La parte C es la que más pesa**, y es la única donde no se te da el orden de los comandos.

## Cómo se verifica un reto que no tiene respuesta correcta

Esto es distinto a los retos de las clases 2 a 5, y conviene decirlo claro para que nadie crea que
el cuaderno le está calificando la historia.

En los retos anteriores había **una** respuesta correcta, y el verificador comparaba una huella
digital de tu resultado contra la suya. Aquí no se puede: el dataset es tuyo (nadie más sabe cuánto
debe dar) y el entregable es una narrativa (no existe "el título correcto" de una slide de
implicación). Fingir una comprobación automática ahí sería mentirte.

Así que la verificación está partida en tres, y cada parte declara hasta dónde llega:

| Qué comprueba | Cómo | Qué NO garantiza |
|---------------|------|------------------|
| `comprobar_cifra` | Que produjiste un número finito y legible, no un `None` ni una tabla | No sabe si el número es el correcto |
| `revisar_titulo` · `revisar_historia` | Forma: que afirmen algo, que quepan en una línea, que el hallazgo lleve cifra, que la implicación no repita el hallazgo, que la acción concluya | No juzga si el título es **bueno** |
| `comprobar_coherencia` | Que el número escrito en tu título sea el mismo que sale de recalcularlo desde el CSV | Nada. Esta sí es automática, y es la más importante del cuaderno |

**Un título en verde no es un título bueno. Es un título con forma de título.** El juicio lo cierras
tú, en la autoevaluación guiada del final del cuaderno, con criterios explícitos.

**La solución no se publica**, ni antes ni después de la clase. El reto se resuelve en voz alta en el
cierre de la sesión, y si te trabas, preguntas ahí mismo.

---

## La estructura, sin negociación

Cuatro slides. Ni tres ni seis.

| # | Slide | La pregunta que responde | Cómo saber que está mal |
|---|-------|--------------------------|-------------------------|
| 1 | Contexto | ¿De qué estamos hablando y por qué ahora? | Si es la agenda de tu presentación, está mal |
| 2 | Hallazgo | ¿Qué encontramos? En una frase, con cifra | Si tiene tres hallazgos, está mal |
| 3 | Implicación | ¿Y eso qué significa para quien decide? | Si repite el hallazgo con otras palabras, está mal |
| 4 | Acción | ¿Qué hay que hacer, quién y cuándo? | Si dice "se recomienda seguir investigando", está mal |

## Requisitos del mini-deck

- [ ] Exactamente 4 slides.
- [ ] Los 4 títulos son **afirmaciones con contenido**, no etiquetas.
      Mal: "Análisis de consumo". Bien: "El 12% de los usuarios consume la mitad del agua".
- [ ] Al menos 2 evidencias sacadas de tu propio EDA: dos cifras, o una cifra y un gráfico.
- [ ] Toda cifra que pongas la puedes reproducir en tu notebook. **La tarea T9 lo comprueba.**
- [ ] La slide de acción nombra **qué** hacer y **quién** lo hace.
- [ ] Declaras cuál es tu audiencia principal: ejecutivo, gerente de área o técnico. Una sola.

### Formato del entregable

**Libre.** Se acepta HTML, PDF, Google Slides, o las cuatro celdas markdown del notebook
renderizadas. **No hay plantilla obligatoria del curso.** Lo que se evalúa es la estructura
narrativa, no la estética. El tiempo que gastes eligiendo colores es tiempo que no gastaste
puliendo tus títulos.

---

## Requisitos del pitch

5 minutos. Reparto sugerido:

| Tramo | Tiempo |
|-------|--------|
| Contexto | 45 seg |
| Hallazgo | 90 seg |
| Implicación | 90 seg |
| Acción | 45 seg |
| Colchón | 30 seg |

Reglas:

- No leas las slides. Si las lees, la audiencia lee más rápido que tú y se aburre.
- Explica cada gráfico en una sola frase, señalando el punto exacto del que hablas.
- No abras pidiendo disculpas por tus datos.
- No cierres con "eso es todo, ¿preguntas?". Cierra con tu recomendación.

En la clase 12 el corte es duro y queda escrito en el acta. Hoy es el ensayo.

---

## Feedback: I like, I wish, What if

Después de cada pitch, cada persona que escuchó entrega tres frases, en este orden:

- **I like...** qué funcionó. Concreto, no "estuvo bien".
- **I wish...** qué faltó. Sobre el trabajo, nunca sobre la persona.
- **What if...** una propuesta, no una queja.

Ejemplo:

- "I like que arrancaste con la cifra de la brecha, entendí el problema en 10 segundos."
- "I wish el título de la tercera slide dijera qué concluir; me tocó deducirlo."
- "What if muestras el gráfico por municipio antes del total? Creo que el contraste pega más fuerte."

**El que presenta no defiende.** Escucha y anota. Discutir el feedback consume el tiempo
del siguiente equipo.

Hay una plantilla del formulario al final de `reto.ipynb`.

---

## Cómo se ve un buen trabajo

La retroalimentación de este reto usa el mismo instrumento de los momentos evaluativos: **Saber, Ser
y Hacer, una banda por dimensión** (Excelente, Bueno, Aceptable, Insuficiente, No aceptable). Los
elementos de cada fila **no tienen peso**: no se suman ni se promedian, alimentan una sola banda.

| Dimensión | Qué se mira hoy | Se cumple cuando |
|-----------|-----------------|------------------|
| **Saber** | Evidencia | Las cifras son reproducibles desde el notebook y sostienen lo que el título afirma |
| **Ser** | Títulos · Acción | Leer solo los 4 títulos seguidos ya cuenta la historia, y alguien podría hacer algo distinto el lunes por haber escuchado esto |
| **Hacer** | Estructura · Foco · Tiempo | Las 4 slides están en orden, hay una idea por slide y un hallazgo principal, y cupo en el pitch sin correr al final |

La autoevaluación del final del cuaderno está organizada con esos mismos tres bloques. Contéstala
antes de presentar: en un ensayo, el resultado útil es saber qué no está listo.

---

## Qué hacer en casa

En clase alcanzas a construir la estructura y a ensayar una vez. El cierre es en casa:

- [ ] Aplicar el feedback que recibiste. Al menos dos de los tres "I wish".
- [ ] Ensayar con cronómetro, en voz alta. El ensayo mental no revela ni el tiempo ni las frases torpes.
- [ ] Pulir el gráfico de la slide de hallazgo con lo que viste en la clase 8.

**Opcional (no se evalúa hoy):** versión alterna del mismo deck para otra audiencia. Es el mejor
ejercicio de los tres, pero no cabe en 60 minutos.

---

## Este reto no tiene nota

Y no la tiene por partida doble. **Los retos semanales no producen nota ni cumplido / no cumplido:**
son práctica, y su retroalimentación usa el lenguaje de bandas para que llegues familiarizado a los
momentos evaluativos.

Este es el ensayo directo de la sustentación del **Momento 2 (clase 12)**, que **tampoco produce
nota**: produce retroalimentación por dimensión y un **cumplido / no cumplido** que **habilita el
Momento 3**, la única evaluación calificada del semestre. Sustentar mal cuesta bandas; no sustentar
cuesta el acceso al M3. La clase 11 es el laboratorio donde se ensaya completo.
