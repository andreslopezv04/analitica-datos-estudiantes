# Clase 7 · Bloque 3 — Reto

## Cinco figuras publication-ready sobre ejecución presupuestal

**Modalidad:** en equipo (1-2 personas)
**Duración:** 60 minutos asistidos en clase + cierre en casa
**Dataset:** `../datos/EJECUCION_PRESUPUESTAL.csv`
**Entregable:** `reto.ipynb` completo + carpeta `figuras/` con los cinco PNG exportados

---

## Cómo está armado el cuaderno

Este reto se recorre solo, leyendo. Nadie dicta los pasos desde el tablero: el profesor circula por
el salón resolviendo dudas. Cada una de las **diez tareas** trae, en este orden:

| Parte | Qué contiene |
|-------|--------------|
| **La pregunta** | Lo que hay que responder, en español |
| **El concepto** | Qué técnica aplica y por qué esa y no otra |
| **Los comandos** | Las instrucciones exactas que va a usar, escritas de forma genérica |
| **Lo que decide usted** | Qué recorte, qué color, qué orden, qué título. Ahí no hay respuesta escrita |
| **La celda de código** | Los pasos numerados en comentarios; las líneas las escribe usted |
| **La comprobación** | `comprobar('TN', ...)` dice si el resultado es el correcto, sin mostrarlo |

Las diez tareas están repartidas en tres partes: **A** (T1 y T2, las dos tablas agregadas), **B**
(T3 a T8, las cinco figuras más la normalización de la figura 4) y **C** (T9 y T10, el ensamblaje y
la exportación). **La parte C es la que más pesa y es la única donde no se le da el orden de los
comandos.**

**Por qué esto sigue siendo un reto y no una copia.** Los comandos se dan; las decisiones no. Usted
elige el recorte, el color, el orden, la unidad del eje y sobre todo el título, que tiene que decir
una conclusión y **ser verdadero**. Eso es lo que se evalúa.

**Las tareas de gráfico se comprueban distinto.** No hay una única figura correcta, así que se revisa
lo verificable: dibujada, titulada, con los ejes etiquetados, con el eje en cero donde la regla lo
exige, con la línea de referencia donde hace falta y con la misma escala en todos los paneles. Los
puntos 1, 7 y 8 de la checklist —los cinco segundos, la escala de grises y que el título sea
verdadero— no los revisa ningún programa. Esos los juzga usted, y son los que más pesan.

> Que el verificador diga CORRECTO no quiere decir que la figura esté bien. Quiere decir que ya se
> puede juzgar.

---

## Sí, es el mismo dataset del demo. Es a propósito

En el resto del curso el reto usa datos que no viste en el demo. Esta clase es la excepción
declarada.

Razón: hoy lo que se evalúa no es tu capacidad de cargar y limpiar un dataset nuevo, es tu
**criterio visual**. Si tuvieras que entender datos nuevos, gastarías 20 de tus 60 minutos en
limpieza y llegarías a los gráficos con 40.

**Lo que cambia entre el demo y el reto no son los datos: son los gráficos.** Cuatro de las
cinco figuras son de tipos que no aparecieron en el demo.

Los mismos números, cinco preguntas distintas, cinco gráficos distintos. Si el gráfico correcto
dependiera de los datos, esto sería trivial. Depende de la pregunta.

---

## La consigna

Cinco figuras listas para publicar. Cada una responde una pregunta analítica concreta, usa la
paleta que definiste y pasa la checklist de diez puntos.

| # | La pregunta | El gráfico | ¿Estuvo en el demo? |
|---|-------------|-----------|---------------------|
| 1 | ¿Qué sectores concentran el presupuesto? | Barras horizontales, top 10 | Sí. Es el calentamiento |
| 2 | ¿Dónde es más grande la brecha entre lo autorizado y lo comprometido? | Barras agrupadas, top 8 | No |
| 3 | ¿Qué entidades tienen mucho presupuesto y poca ejecución? | Dispersión con línea de referencia | No |
| 4 | ¿Cómo cambia la composición del gasto entre sectores? | Barras apiladas al 100% | No |
| 5 | ¿Qué sectores están por debajo del promedio de ejecución? | Small multiples | No |

Aproximadamente **9 minutos por figura**. Si te demoras 20 en la primera, no vas a terminar.
La primera es la que ya sabes hacer: hazla rápido y sigue.

---

## La checklist de diez puntos

Es la misma del Bloque 1 y del Bloque 2. **Es con lo que se califica.**

- [ ] ¿Pasa la prueba de los 5 segundos con alguien ajeno al equipo?
- [ ] ¿El tipo de gráfico corresponde a la pregunta?
- [ ] ¿Las categorías están ordenadas por valor, no alfabéticamente?
- [ ] ¿El eje empieza en cero, o hay una razón declarada para que no?
- [ ] ¿Borré todo lo que se podía borrar sin perder información?
- [ ] ¿Hay un solo elemento resaltado y el resto en gris?
- [ ] ¿Funciona en escala de grises?
- [ ] ¿El título dice la conclusión y es verdadero?
- [ ] ¿Los ejes tienen unidades?
- [ ] ¿Está la fuente del dato?

---

## Requisitos no negociables

1. **Una paleta, definida en una celda al inicio, usada en las cinco figuras.**
   Es lo primero que se mira al calificar. Es lo que separa cinco figuras de un informe.
2. **Ejes en billones de pesos**, no en notación científica. Si tu eje dice `1e13`, la figura
   está incompleta.
3. **Título que enuncia la conclusión, y que es verdadero.** Si el título afirma algo que los
   datos no sostienen, no es storytelling: es un dato falso en el renglón más grande.
4. **Fuente citada** en las cinco.
5. **Exportación a PNG con `dpi=300`**, `bbox_inches='tight'` y `facecolor='white'`.

### Nombres de archivo

```
figuras/fig1_apropiacion_por_sector.png
figuras/fig2_brecha_apropiacion_compromisos.png
figuras/fig3_entidades_presupuesto_vs_ejecucion.png
figuras/fig4_composicion_gasto_por_sector.png
figuras/fig5_ejecucion_small_multiples.png
```

---

## Dónde te vas a atascar

En orden de frecuencia real, del semestre pasado:

| Atasco | Tarea | Síntoma | Salida |
|--------|-------|---------|--------|
| Las magnitudes | T1 | El eje dice `1e13` | Divide entre 1e12 y pon "billones de pesos" en la etiqueta |
| Los nombres de las columnas derivadas | T1, T2 | La tabla se ve bien y `comprobar` dice que no coincide | Se llaman `'% Ejecución'` y `'Apropiación (billones)'`, con tilde y mayúscula |
| La normalización por fila | T6 | Las filas suman 300, o salen números gigantes | Invertiste los `axis`: `.div(tabla.sum(axis=1), axis=0) * 100` |
| Los small multiples | T8 | El verificador rechaza por escalas distintas | `sharex=True`. Sin eso la comparación visual es falsa, y la figura se ve bien igual |
| Los títulos | todas | Cinco títulos que describen los ejes | "Eso me dice qué graficaste, no qué encontraste" |
| La paleta | T5 en adelante | Las figuras 1 y 2 con paleta, las demás con los colores por defecto | Revisa a mitad de camino |
| El tiempo | T3 | 25 minutos en la figura 1 | A los 15 minutos deberías ir en la figura 2 |
| El mensaje del verificador | cualquiera | "No sé qué le falta a mi gráfico" | El mensaje lo dice, línea por línea. Léelo |

---

## El bucle de la clase 3, sobre una figura

Las cuatro skills que instalaste en la clase 3 —`especifica-encargo`, `planea-trabajo`,
`ejecuta-plan` y `valida-resultado`— se usan hoy. No se vuelven a explicar: hoy son la
herramienta, no el tema.

**Cada figura es una vuelta completa del bucle, no una sola vuelta para las cinco.**

| Tramo | Qué escribes, y cuándo |
|-------|------------------------|
| **Especificar** | La pregunta que la figura responde, quién la mira, y **el título que esperas poder escribir al final**. Antes de dibujar |
| **Planear** | El tipo de gráfico y por qué ese y no el vecino, el recorte, la unidad del eje, qué se resalta |
| **Ejecutar** | La figura. Es el único tramo que se delega entero |
| **Validar** | El título contra la tabla, condición por condición |

**Por qué esto importa hoy más que en otras clases.** Un gráfico bonito que no responde nada
casi siempre salió de un encargo que no preguntaba nada. Si el título lo escribes **después**
de ver la figura, va a describir la figura. Si lo escribes **antes**, la figura tiene que
ganárselo. Ese cambio de orden es todo el tramo de especificar.

Y la mitad que se olvida: si al validar el título resulta falso, **no parches el título**.
Vuelve a especificar, porque el problema estaba en la pregunta.

### Validar: las cuatro preguntas, traducidas a una figura

La checklist dice **qué** revisar. Las cuatro preguntas del analista dicen **en qué orden**, y
son las mismas de la clase 3: allá el resultado era un número, aquí es un gráfico. No son diez
criterios más: son la forma de recorrer los diez que ya tienes.

| La pregunta | Sobre la figura | Puntos de la checklist |
|-------------|-----------------|------------------------|
| **¿El número tiene sentido?** | Lee un valor en el eje y búscalo en la tabla de la que salió. Un eje que dice `1e13` no te está mostrando un número: te está mostrando una notación | 9 y 10 |
| **¿La forma cuadra?** | Aquí la forma es la **escala**: barras desde cero, paneles con el mismo rango, ninguna línea sobre categorías. Una escala mal puesta se ve perfectamente bien | 3 y 4 |
| **¿Responde lo que pregunté?** | Cinco segundos con alguien de otro equipo, sin explicarle nada. Lo que te devuelva tiene que ser la pregunta que escribiste al especificar, no otra parecida | 1, 2 y 8 |
| **¿Cambió algo?** | Compara con el gráfico por defecto, el que sale sin tocar nada. Si el lector entiende lo mismo, no rediseñaste: maquillaste | 5, 6 y 7 |

La tercera es la peligrosa, igual que en la clase 3: una figura puede pasar los otros nueve
puntos y responder una pregunta que nadie hizo.

**Y algo que vale la pena escribir esta semana:** un skill que verifique los diez puntos de la
checklist. Le pasas el código de una figura y te dice qué puntos incumple. Hoy es el día en que
sabes exactamente qué debe revisar, y lo vas a usar en las clases 8, 9 y 11.

> Por qué esta clase importa aunque le pidas la figura a una IA: a "un gráfico bonito" te
> responde algo genérico; a "barras horizontales ordenadas, top 10, todas en gris salvo la
> primera, con etiquetas directas, eje desde cero y sin bordes" te responde exactamente eso.
> **La diferencia entre las dos peticiones es el tramo de especificar, y es lo que aprendiste
> hoy.**

---

## Análisis crítico

Al final del notebook, cinco preguntas. Cortas, con criterio:

1. ¿Cuál de las cinco figuras comunica mejor el hallazgo más importante del dataset? ¿Por qué?
2. ¿Qué te perderías si solo mostraras los sectores con más presupuesto?
3. Si solo pudieras mostrar una figura a un tomador de decisiones, ¿cuál y qué pregunta
   responde mejor?
4. ¿Qué dato adicional (una columna que no está en este archivo) haría estas figuras mucho
   más útiles?
5. ¿Cuál de estos cinco tipos de gráfico vas a usar en el dashboard del Momento 2, y para qué
   pregunta?

---

## Entrega

```
reto_clase07_APELLIDO.ipynb
figuras/
    fig1_apropiacion_por_sector.png
    fig2_brecha_apropiacion_compromisos.png
    fig3_entidades_presupuesto_vs_ejecucion.png
    fig4_composicion_gasto_por_sector.png
    fig5_ejecucion_small_multiples.png
```

Antes de subirlo: **Kernel → Restart and Run All**, y el punto de control final tiene que decir
**10 de 10 correctas**. Un cuaderno que no corre de arriba a abajo le pone techo a la dimensión
Hacer.

Y antes de eso, **valida**: las cuatro preguntas sobre las cinco figuras, en orden. La tercera
—¿responde lo que pregunté?— es la que más figuras tumba, y la única que necesita a otra persona.

**Fecha de entrega:** antes de la clase 8.

---

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegues familiarizado a las
sustentaciones de los tres momentos. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | El tipo de gráfico es el correcto para cada pregunta, y se puede explicar por qué ese y no otro |
| **Ser** | Los títulos enuncian una conclusión **y son verdaderos**, y el análisis crítico muestra criterio propio |
| **Hacer** | Paleta consistente aplicada en las cinco figuras, data-ink ratio (figuras limpias, sin basura visual), ejes con unidades legibles y fuente citada, exportación a 300 DPI con los nombres pedidos |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Un título que afirma algo que los datos no sostienen: **Ser** no pasa de Insuficiente. Es un error
  de análisis, no de diseño, y es el más grave que se puede cometer hoy.
- Un eje de barras truncado sin razón declarada: **Hacer** no pasa de Aceptable.
- Un gráfico de líneas sobre categorías: **Saber** no pasa de Aceptable. Este dataset no tiene tiempo.

---

## Opcional, para cerrar en casa

Marcado como opcional: no se califica.

- Exportar también en SVG (`format='svg'`), que es vectorial y escala sin pixelarse. Útil para
  el dashboard del Momento 2.
- Verificar las cinco figuras en un simulador de daltonismo y anotar si alguna falla.
- Convertir tu paleta y tu función de limpieza de ejes en un archivo `estilo.py` reutilizable,
  e importarlo en las clases 8 y 9. Vas a producir muchos gráficos más.
