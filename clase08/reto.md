# Clase 8 · Bloque 3 — Reto

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

## Usa lo de la clase 7

Los skills que escribiste la semana pasada sirven hoy.

Y aprovecha para escribir uno nuevo: **un verificador de la checklist de diez puntos.** Le
pasas el código de una figura y te dice qué puntos incumple.

Es el skill más rentable del Momento 2 y hoy es el día en que sabes qué debe decir. Lo vas a
usar en las clases 9, 10 y 12.

> Y recuerda por qué esta clase importa aunque uses IA: si le pides "un gráfico bonito", te da
> algo genérico. Si le pides "barras horizontales ordenadas, top 10, todas en gris salvo la
> primera, con etiquetas directas, eje desde cero y sin bordes", te da exactamente eso.
> **La diferencia entre las dos peticiones es lo que aprendiste hoy.**

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
reto_clase08_APELLIDO.ipynb
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

**Fecha de entrega:** antes de la clase 9.

---

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegues familiarizado a las clases
6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen peso**:
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
  e importarlo en las clases 9 y 10. Vas a producir muchos gráficos más.
