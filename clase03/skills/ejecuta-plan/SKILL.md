---
name: Ejecuta el plan
description: Recorre un plan paso a paso, uno por vez, comprobando cada paso antes de seguir y dejando escrito lo que se aprendio. Usela cuando ya exista el plan y toque ejecutarlo de verdad
version: 3.0.0
---

# Ejecuta el plan

Recorre un plan **un paso a la vez**. No es un piloto automatico: se detiene, muestra lo que
produjo el paso, lo comprueba y espera antes de seguir.

Es el tercer tramo del bucle de trabajo, y es el unico que se delega casi entero: el que planeo ya
dijo que hay que hacer y con que se comprueba. Lo que este skill agrega es la disciplina de no
correr. Un trabajo que avanza cinco pasos sin mirar ninguno llega a un resultado que nadie puede
defender.

## Principios

1. **Un paso por vez.** Se completa un paso, se comprueba, se para. El siguiente empieza cuando el
   usuario lo diga.
2. **Las dudas van antes de producir.** Si el paso es ambiguo, se pregunta. El usuario esta ahi.
3. **La comprobacion no es opcional.** Cada paso trae la suya escrita en el plan y se ejecuta.
4. **Lo que se aprende se escribe.** Un hallazgo que no queda escrito se vuelve a descubrir la
   semana entrante.
5. **Cada paso terminado deja un resumen** de dos o tres lineas dentro del plan.

## Recorrido

### 1) Encontrar el paso

Lea el plan y ubique el primer paso sin marcar. Si no hay plan, digalo y proponga escribirlo antes
de empezar.

### 2) Entender antes de actuar

Antes de producir nada:

- Compruebe que el paso sigue teniendo sentido. Si los pasos anteriores cambiaron los supuestos,
  proponga el ajuste antes de seguir.
- Mire de verdad los insumos que el paso menciona, en lugar de dar por hecho lo que traen.
- Diga en una frase que va a significar "terminado" para este paso.

**Si el paso es demasiado grande, partalo en el plan antes de empezarlo.** Un paso es demasiado
grande si toca dos cosas sin relacion, o si su comprobacion necesita dos comprobaciones.

Si algo queda ambiguo, pregunte con opciones concretas. Por ejemplo:

```text
Antes de empezar el paso 3, "quitar las entradas sin fecha":

1) Las entradas con la fecha vacia
   a) se descartan
   b) se conservan marcadas como "sin fecha"

2) Al terminar reporto
   a) cuantas quedaron y que porcentaje se fue (por defecto)
   b) solo el total

Responda: 1a 2a
```

No siga hasta tener respuesta o hasta que el usuario diga que use los valores por defecto.

### 3) Ejecutar

Haga solo ese paso. Nada de adelantar el siguiente porque "ya que estamos".

Al terminar, **antes de decir que quedo listo**, corra la comprobacion que el plan pide y muestre:

- El antes y el despues, si el paso quito o transformo material
- La cifra o el artefacto que el paso produce, obtenido de verdad, nunca estimado
- Si el resultado cae dentro de los limites que el criterio de aceptacion declaro

Si la comprobacion falla, **no siga al paso siguiente**. Reporte que fallo y proponga a que tramo
del bucle hay que volver.

### 4) Dejar escrito lo aprendido

Antes de cerrar el paso, preguntese que aprendio que sirva mas adelante.

| Que aprendio | Donde se escribe |
|--------------|------------------|
| Algo de este paso ("este archivo trae la fecha en dos formatos") | Una nota debajo del paso, en el plan |
| Algo del trabajo entero ("la fuente publica el dato con dos meses de retraso") | El archivo de notas del proyecto |
| Algo que cambia el encargo | El encargo, y se avisa |

### 5) Cerrar el paso

Marque el paso y escriba el resumen debajo:

```markdown
- [x] 3. Quitar las entradas sin fecha
  > 9.000 entradas antes, 8.412 despues: se fueron 588 (6,5%). Todas de 2019.
  > OJO: la fecha viene en dos formatos distintos, ver nota del paso 4.
```

### 6) Reportar y parar

Diga que se hizo, que se aprendio y cual es el paso siguiente. **Y pare.** El usuario decide cuando
seguir: puede que quiera mirar el resultado antes.

## Cuando el plan ya no cuadra

El plan es un documento vivo. Se actualiza cuando la realidad no coincide:

- **Un paso resulto ser dos**: se parte en el plan antes de ejecutarlo
- **Aparecio trabajo que nadie previo**: se agrega como paso nuevo, con la nota de donde salio
- **Un paso quedo bloqueado**: se marca como bloqueado, con lo que hace falta para desbloquearlo

## Formato

### Paso que se ejecuto
[Numero y titulo, tal como aparece en el plan]

### Que se hizo
[Dos o tres lineas. Que se hizo, no como]

### Comprobacion
| Que se miro | Valor obtenido | Valor esperado | Cuadra |
|-------------|----------------|----------------|--------|
| [la comprobacion del plan] | [obtenido de verdad] | [del plan] | [si / no] |

### Antes y despues
[Lo que habia y lo que quedo, con cifras, si el paso quito o transformo material. Si no aplica,
digalo]

### Lo que se aprendio
- [Hallazgo que sirve mas adelante, y donde quedo escrito]

### Paso siguiente
[Cual es. Sin empezarlo]

## Reglas

- Regla 1. Un paso por vez. No encadene dos pasos aunque el segundo sea trivial.
- Regla 2. No estime ninguna cifra. Si un numero no salio del trabajo hecho, no es un numero: es
  una suposicion, y asi hay que reportarlo.
- Regla 3. No siga adelante con una comprobacion fallida. Un paso roto contamina todo lo que viene
  despues y se descubre tres pasos mas tarde.
- Regla 4. No cambie el encargo por su cuenta. Si el paso no se puede hacer como esta escrito, se
  dice y se propone; no se hace otra cosa parecida en silencio.
- Regla 5. Reporte siempre el antes y el despues de toda operacion que quite o transforme material.
  Es la comprobacion mas barata que existe y caza la mitad de los errores.
- Regla 6. Un resumen de paso nunca dice solamente "listo". Dice que quedo, con cifras.
