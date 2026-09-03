---
name: Valida el resultado
description: Somete un resultado al criterio de aceptacion que el encargo escribio antes de empezar, condicion por condicion, y emite un veredicto con la correccion concreta y el tramo del bucle al que hay que volver, sin tocar lo que lo produjo
version: 3.0.0
---

# Valida el resultado

Recibe tres cosas: el encargo, el resultado obtenido y como se produjo. Devuelve un veredicto sobre
el resultado.

Es el cuarto tramo del bucle de trabajo, y el unico que no se delega del todo: la maquina puede
recorrer las condiciones, pero quien conoce el oficio es el usuario. Este skill escribe una vez el
procedimiento para que no haya que acordarse de aplicarlo cada vez.

**Contra que se valida.** Contra el criterio de aceptacion del encargo, y contra nada mas. No
contra lo que el resultado se ve, ni contra lo que ahora parece razonable: contra las condiciones
que se escribieron cuando el resultado todavia no existia. Esa es toda la razon de que el criterio
se escriba antes.

## Recorrido

### 1) Sacar las condiciones

Lea el criterio de aceptacion del encargo y conviertalo en una lista de condiciones comprobables,
una por linea. Si el encargo no trae criterio de aceptacion, no invente uno: digalo, marque el
veredicto como no emitible y mande a volver a especificar.

### 2) Contestar cada condicion

Cada condicion se contesta con **si**, **no** o **no se puede saber**, y con la evidencia al lado.
Ninguna se omite, aunque se vea obvia: omitir una es la forma mas comun de no hacerla.

"No se puede saber" es una respuesta valida y necesaria cuando falta el dato para contestar. No es
un fracaso del validador: es un hallazgo sobre el encargo, que quedo corto.

### 3) Mirar lo que el criterio no cubrio

Un criterio de aceptacion nunca lo cubre todo. Antes de cerrar, pregunte:

- Que del resultado le extrana, aunque ninguna condicion lo prohiba
- Que se produjo de mas, o de menos, sin que nadie lo pidiera
- Quien podria leer esto mal, y que dano haria

Lo que salga de aqui no cambia el veredicto: se declara aparte, y casi siempre es material para la
siguiente vuelta del encargo.

### 4) Decir a donde se vuelve

Un veredicto que no dice que hacer no sirve. Nombre el tramo del bucle y el cambio concreto.

**Cada oficio tiene ademas su propio juego de preguntas rapidas**, las que su gente aprendio a
hacerse antes de dar algo por bueno. No las trae este skill, porque son de la disciplina y no del
metodo. Como se arma ese juego, con un ejemplo trabajado, esta en
`references/como-se-valida.md`.

## Formato

### Veredicto
[Sirve / Sirve con reservas / No sirve / No se puede emitir] - [la razon, en una frase]

### Condicion por condicion
| Condicion del criterio de aceptacion | Cumple | En que me baso |
|--------------------------------------|--------|----------------|
| [la condicion, tal como la escribio el encargo] | [si / no / no se puede saber] | [la evidencia concreta] |

### Lo que el criterio no cubrio
- [Lo que extrana del resultado, aunque ninguna condicion lo prohiba, o "nada"]

### Que se corrige, y donde
- Tramo del bucle al que hay que volver: [especificar / planear / ejecutar]
- Cambio concreto: [que frase se agrega o se cambia, y en que documento o en que paso]

### Lo que este veredicto no puede juzgar
- [Lo que haria falta saber, o mirar, para cerrar una condicion que quedo en "no se puede saber"]

## Reglas

- Regla 1. No corrija el resultado ni entregue una version arreglada. Este skill emite un veredicto
  y senala el tramo al que hay que volver.
- Regla 2. Cuando una condicion falla, la correccion se busca primero en el encargo. Un resultado
  que responde otra cosa casi siempre viene de un encargo que pedia otra cosa; parchear la salida
  esconde el problema y lo devuelve la proxima vez, cuando ya nadie se acuerde.
- Regla 3. No estime ninguna cifra para comparar. Si un numero no salio del trabajo hecho, no es un
  numero: es una suposicion, y asi hay que reportarlo.
- Regla 4. Un veredicto sin razon no es un veredicto. "No sirve" a secas esta prohibido.
- Regla 5. Todas las condiciones aparecen, aunque casi todas salgan limpias. Una lista recortada a
  lo que fallo no deja ver lo que nunca se miro.
- Regla 6. "No se puede saber" nunca se reemplaza por un "si" prudente. Un "si" sin base es peor
  que un hueco declarado.
- Regla 7. No agregue condiciones que el encargo no escribio. Lo que le extrane va en la seccion de
  lo que el criterio no cubrio, no en la tabla.
