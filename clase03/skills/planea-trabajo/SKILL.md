---
name: Planea el trabajo
description: Convierte un encargo escrito en un plan de pasos ejecutables, cada uno con su comprobacion, para ver el camino completo antes de tener resultado que revisar. Usela cuando ya exista el encargo y antes de empezar a producir nada
version: 3.0.0
---

# Planea el trabajo

Recibe el encargo de un trabajo y devuelve el plan para ejecutarlo: los pasos, en orden, cada uno
con lo que produce y con lo que se mira al terminarlo.

Es el segundo tramo del bucle de trabajo. Existe por una razon concreta: revisar un plan de ocho
lineas cuesta un minuto y revisar el resultado que sale de un plan malo cuesta la tarde. El plan es
donde todavia es barato cambiar de idea.

Este skill guia la ejecucion, pero no la reemplaza. Puede proponer el detalle de un paso cuando el
usuario lo pida, y en ese caso el detalle va dentro del paso y nunca sustituye al plan.

## Antes de escribir: lea y piense

1. **Lea el encargo completo.** Si no hay encargo, digalo y proponga escribirlo primero. Un plan
   sin encargo es una lista de tareas sin destino.
2. **Mire de lejos con que se cuenta.** Que insumos hay, en que estado estan, que falta. Nada mas.
3. **Disene el camino mas corto** que cumple el encargo. Despues pregunte de cada paso: hace falta
   de verdad, o esta ahi porque siempre se hace.
4. **Ordene por costo de equivocarse.** Lo que puede invalidar todo lo demas va primero.
5. **Busque el paso mas riesgoso** y digalo en voz alta dentro del plan.

Si al descomponer descubre que no entendio algo, vuelva a preguntar. Planear es iterativo.

**Salida de emergencia.** Si el trabajo es de veinte minutos y el camino es obvio, digalo y
proponga hacerlo en lugar de planearlo. No todo necesita un plan.

## Formato

### Supuestos que este plan da por ciertos
- [Cada supuesto que, de ser falso, invalidaria el plan completo]

### Pasos
| # | Paso | Que produce | Que se mira al terminarlo |
|---|------|-------------|---------------------------|
| 1 | [accion concreta, un verbo] | [el artefacto o la cifra] | [la comprobacion, con el valor esperado] |

### El paso mas riesgoso
[Cual es, por que, y que se hace si sale mal]

### Donde se puede caer
| Paso | Que puede salir mal | Como se nota |
|------|---------------------|--------------|
| [#]  | [la falla concreta] | [la senal que la delata en el resultado] |

### Que se entrega al final
- [El artefacto final, descrito como se veria: de que partes consta, que forma y que extension tiene]

## Reglas

- Regla 1. Ningun paso queda sin su comprobacion. Un paso que no se puede comprobar no es un paso
  del plan: es una esperanza.
- Regla 2. Maximo siete pasos. Si hacen falta mas, el encargo son dos trabajos y hay que decirlo en
  lugar de alargar la tabla.
- Regla 3. El primer paso es siempre mirar lo que ya hay: que insumos existen, en que estado, que
  falta. Nunca empiece por el paso que produce el resultado final.
- Regla 4. No estime ninguna cifra. Donde haga falta un numero que sale del trabajo, el plan indica
  el paso que lo obtiene, no el valor.
- Regla 5. Si el encargo que recibio no trae criterio de aceptacion, no invente uno: digalo en los
  supuestos y siga.
- Regla 6. Los pasos son verbos concretos con un objeto al lado. "Manejar el material" no es un
  paso; "quitar del listado las entradas sin fecha" si lo es.
- Regla 7. El ultimo paso siempre comprueba el criterio de aceptacion del encargo. Un plan que no
  vuelve al encargo no cierra el bucle.
