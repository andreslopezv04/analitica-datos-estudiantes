# Clase 3 · Construir con IA: agentes, skills y ecosistema

Cómo trabajar con un asistente de IA sin quedar a merced de lo que devuelva: el bucle
**especificar → planear → ejecutar → validar**, y cómo se empaqueta ese bucle en skills reutilizables.

**Esta clase es distinta a las demás:** el demo y el reto no son cuadernos, son documentos HTML que
se recorren paso a paso. Se abren con doble clic y se dejan en una ventana al lado del editor.

## Qué hay aquí

| Archivo | Para qué |
|---------|----------|
| `slides.html` | Diapositivas de la clase |
| `demo.html` | El demo guiado, paso a paso: se escribe un `SKILL.md` a mano, se instala el catálogo y se repite el trabajo con ayuda de IA |
| `reto.html` | El reto, paso a paso: recorrer el bucle completo, una skill por tramo, para construir un dashboard. Trae campos para escribir dentro del documento y un botón para exportar las respuestas |
| `skills/README.md` | Explicación del catálogo: qué hace cada skill y cuándo se usa |
| `skills/especifica-encargo/` · `skills/planea-trabajo/` · `skills/ejecuta-plan/` · `skills/valida-resultado/` | Las cuatro skills del curso, una por tramo del bucle. Cada una con su `SKILL.md` y su carpeta `references/` |
| `skills/zips/` | Las mismas cuatro skills empaquetadas en `.zip`, para quien prefiera instalarlas descomprimiendo |

## El catálogo de skills

Cuatro skills generales, que sirven para cualquier trabajo y no solo para datos:

| Skill | Tramo | Qué hace |
|-------|-------|----------|
| `especifica-encargo` | Especificar | Convierte una petición dicha en voz alta en un encargo con objetivo, alcance, insumos y criterio de aceptación |
| `planea-trabajo` | Planear | Convierte ese encargo en pasos, cada uno con su comprobación |
| `ejecuta-plan` | Ejecutar | Ejecuta un paso por vez, con su comprobación y su resumen |
| `valida-resultado` | Validar | Contrasta el resultado con el criterio de aceptación, condición por condición |

Se instalan copiando las carpetas (o descomprimiendo los ZIP) en la carpeta de skills de su
herramienta. Si no tiene ninguna, use `.gemini/skills/` igual. El procedimiento exacto, con su
verificador, está en `demo.html`.

## Datos

| Archivo | Dónde se usa |
|---------|--------------|
| [`../datos/saber_pro.csv`](../datos/saber_pro.csv) | Reto. Es el mismo para todos los equipos |

## Cómo se usa

- **El demo se recorre en clase**, siguiendo el documento: se lee, se ejecuta lo que indica y se
  comprueba con los verificadores que trae en línea.
- **El reto se hace después**, solo, con el profesor circulando. Al final se exportan las respuestas
  desde el propio documento.

## Antes de empezar

- El entorno del curso montado ([`../INSTALACION.md`](../INSTALACION.md)).
- **Nada más.** No hace falta instalar ningún CLI de IA, ni tener cuenta en nada: el demo y el
  reto se recorren con un editor de texto y, para el último tramo, cualquier chatbot en el
  navegador.
- El demo recorrido antes de abrir el reto. El reto asume que el catálogo ya está copiado.
