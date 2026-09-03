---
name: Especifica el encargo
description: Convierte una peticion suelta, escrita como la diria una persona, en un encargo con objetivo, alcance, insumos y criterio de aceptacion, antes de que exista una sola linea de resultado. Usela al empezar cualquier trabajo, sea un analisis, un informe, una presentacion o un programa
version: 3.0.0
---

# Especifica el encargo

Recibe una peticion escrita como la diria una persona y devuelve el encargo que la responderia.
Este skill no hace el trabajo y no produce el resultado: escribe lo que hay que hacer, para quien,
y como se sabra que quedo bien.

Es el primer tramo del bucle de trabajo: especificar, planear, ejecutar, validar. Si el encargo
queda ambiguo, todo lo que venga despues responde otra cosa, y lo hace con muy buena redaccion.

Sirve para cualquier tipo de trabajo. La peticion puede ser un analisis, un informe, una
presentacion, un trabajo de otra materia o un proyecto personal: lo que cambia es el contenido de
las secciones, nunca cuales son.

## Antes de escribir: entreviste

No empiece a redactar con lo primero que le dieron. Haga las preguntas minimas que hagan falta para
especificar con confianza, y ni una mas. Si algo se puede deducir de lo que el usuario ya escribio,
no lo pregunte.

Lo que hay que entender antes de redactar:

| Que averiguar | Como se pregunta |
|---------------|------------------|
| El objetivo real | Que decision o que accion depende de este resultado |
| Quien lo recibe | Quien lo va a leer, usar o calificar, y con que lo compara |
| El contexto | Por que ahora, que lo disparo |
| Las restricciones | Con que se cuenta, hasta cuando, que no se puede cambiar |
| Lo ya intentado | Que se probo y se descarto, y por que |
| La preocupacion | Que es lo que mas duda le da del resultado |

Cuando algo no se pueda deducir y tampoco se haya preguntado, escribalo como pregunta pendiente en
la seccion correspondiente. No lo suponga y no lo rellene con un valor plausible.

**Discuta el encargo si el encargo esta mal.** Si la peticion se resuelve en cinco minutos mirando
algo que ya existe, y no hace falta ningun trabajo, digalo. Es mas barato discutirlo aqui que
despues de tres horas.

## Formato

### Encargo en una frase
[La peticion, reescrita de forma que se pueda cumplir y comprobar. Una sola frase.]

### Contexto
[Por que se hace esto, quien recibe el resultado y que decision depende de el. Dos o tres frases.]

### Lo que hay que responder o producir
1. [Punto concreto, con su unidad de medida o su forma explicita]
2. [Segundo punto]
3. [Tercer punto, si hace falta]

### Insumos que hace falta tener
| Insumo | Para que se usa | Si no existe |
|--------|-----------------|--------------|
| [nombre exacto: un archivo, una fuente, un dato, un permiso, un contacto] | [uso concreto] | [que se hace en su lugar] |

### Criterio de aceptacion
- Forma esperada del resultado: [que es, de que partes consta, en que unidad o extension]
- Limites razonables: [que valores, plazos o tamanos no encenderian ninguna alarma]
- Como se sabra que responde: [comprobacion concreta que alguien mas podria correr]

### Lo que queda fuera
- [Algo que alguien podria esperar de este trabajo y que este encargo no cubre]

### Riesgos del resultado
- [Que lectura o uso equivocado podria salir de esto, y para quien]

### Preguntas pendientes
- [Lo que hizo falta preguntarle al usuario para cerrar el encargo, o "ninguna"]

### Decisiones tomadas
| Duda que aparecio | Que se decidio | Por que |
|-------------------|----------------|---------|
| [la duda]         | [la decision]  | [la razon, no solo la eleccion] |

## Reglas

- Regla 1. No proponga la solucion. Ni codigo, ni estructura del informe, ni herramientas. Este
  skill especifica; hacer el trabajo es de otro tramo del bucle.
- Regla 2. Cada punto de lo que hay que responder o producir dice su unidad o su forma. "El gasto
  por municipio en pesos al mes" es un punto; "el gasto" no lo es. "Tres diapositivas de cierre con
  una recomendacion cada una" es un punto; "cerrar bien" no lo es.
- Regla 3. El criterio de aceptacion es obligatorio y va antes de que exista ningun resultado. Si
  no se puede escribir un limite razonable, digalo en las preguntas pendientes en lugar de
  inventarlo.
- Regla 4. No suponga nombres de insumos. Use unicamente los que el usuario haya escrito, y lo que
  falte va a preguntas pendientes.
- Regla 5. La seccion de lo que queda fuera nunca va vacia: un encargo sin bordes se desborda.
- Regla 6. Una decision sin razon no entra en el registro de decisiones. La eleccion sola no le
  sirve a quien lea esto en tres semanas.
- Regla 7. No rellene una seccion para que se vea completa. Una seccion vacia es peor que una
  seccion omitida, y una seccion inventada es peor que las dos.
