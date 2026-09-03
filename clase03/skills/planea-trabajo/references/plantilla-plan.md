# Plantilla de plan

Estructura para escribir el plan. Extremadamente concisa: sacrifique la gramatica antes que la
brevedad.

```markdown
# Plan: <titulo del trabajo>

<Una a tres frases: que se va a hacer>

## Alcance

| Entra | No entra |
|-------|----------|
|       |          |

## Criterio de exito

- <Medible. Sale del criterio de aceptacion del encargo>

## Supuestos

- <Cada supuesto que, de ser falso, invalida el plan>

## Pasos

- [ ] 1. <Verbo + objeto concreto>
      Produce: <artefacto o cifra>
      Se comprueba: <la comprobacion, con el valor esperado>
- [ ] 2. ...
- [ ] 3. ...

## El paso mas riesgoso

<Cual, por que, y el plan B>

## Donde se puede caer

| Paso | Que puede salir mal | Como se nota |
|------|---------------------|--------------|
|      |                     |              |

## Que se entrega

- <El artefacto final: de que partes consta, que forma y que extension tiene>
```

## Como se escribe un buen paso

**Sirven:**

- Atomicos y ordenados: mirar lo que hay, preparar, producir, comprobar
- Empiezan por verbo: "Cargar...", "Descartar...", "Agrupar...", "Redactar...", "Comprobar..."
- Nombran el objeto exacto: el archivo, la seccion, la columna, la fuente
- Traen una comprobacion concreta: "quedan 8.412 de 9.000", no "verificar que este bien"
- El ultimo vuelve al criterio de aceptacion

**No sirven:**

- Pasos vagos: "manejar el material", "hacer la revision"
- Micro-pasos: "abrir el editor", "crear la carpeta"
- La solucion completa dentro del paso, salvo que el usuario la haya pedido

**Siempre hay:**

- Al menos un paso que comprueba
- Un paso o una fila de riesgo cuando el trabajo toca material sucio, fechas o dinero

## Fases

Si el trabajo es grande, partalo en fases:

- La **fase 1** es la unica que se detalla paso por paso
- Las siguientes van como una lista corta de titulos al final, sin detalle

Cuando la fase 1 termina, se reemplaza la lista de pasos por la de la fase 2. El contexto largo vive
en el encargo, no en el plan.

## Barra de calidad

Antes de dar el plan por terminado:

- [ ] Se pregunto hasta entender el encargo
- [ ] Se discutio el encargo si estaba mal planteado
- [ ] Cada paso es atomico y comprobable
- [ ] Esta identificado el paso mas riesgoso
- [ ] El criterio de exito es medible
- [ ] El plan es ejecutable por otra persona sin usted al lado
