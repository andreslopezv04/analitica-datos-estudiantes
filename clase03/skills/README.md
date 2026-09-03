# Catálogo de skills del curso

Cuatro skills, una por tramo del bucle de trabajo del Bloque 1:

**Especificar → Planear → Ejecutar → Validar**

| Carpeta | Tramo | Qué recibe | Qué devuelve |
|---------|-------|------------|--------------|
| `especifica-encargo/` | Especificar | Una petición como la diría una persona | El encargo con objetivo, alcance, insumos y criterio de aceptación |
| `planea-trabajo/` | Planear | Ese encargo | Los pasos, cada uno con su comprobación |
| `ejecuta-plan/` | Ejecutar | Ese plan | Un paso ejecutado por vez, con su comprobación y su resumen |
| `valida-resultado/` | Validar | El encargo, el resultado y cómo se produjo | Un veredicto contra el criterio de aceptación, condición por condición |

## Son generales, y eso es a propósito

Ninguna de las cuatro sabe qué es un dataset, una columna o un dashboard. Sirven para **cualquier
trabajo**: un análisis, un informe, una presentación, un trabajo de otra materia, un proyecto
personal. Lo que cambia entre un caso y otro es el contenido de las secciones; nunca cuáles son.

Esa decisión no es estética. Una herramienta que solo sirve para lo que estamos haciendo hoy se
queda en el semestre. El bucle es un método de trabajo, y usted lo va a necesitar la próxima vez que
tenga que entregarle algo a alguien, sea o no de datos.

**Lo específico lo pone usted.** Un analista, al validar, no se queda en "cumple el criterio": se
hace además las cuatro preguntas de su oficio (¿el número tiene sentido? ¿la forma cuadra?
¿responde lo que pregunté? ¿cambió algo?). Esas cuatro son de la disciplina, no del método, y por
eso no viven dentro de `valida-resultado`: se enseñan en la clase, y el archivo
`valida-resultado/references/como-se-valida.md` las trae como **ejemplo trabajado** de la forma que
tiene un juego de preguntas de un oficio, con la guía para armarse el propio.

En una frase: **el skill da el procedimiento, la disciplina da las preguntas concretas.**

## Dónde se usan hoy

| Momento de la clase | Qué se hace con el catálogo |
|---------------------|-----------------------------|
| Bloque 2 · demo, Tramo B | Se instala, se pasa por el verificador y se audita. Después se usa una vez: `valida-resultado` sobre el `SKILL.md` que usted mismo escribió a mano |
| Bloque 2 · demo, Tramo C | Se recorre el bucle completo con las cuatro para construir un segundo `SKILL.md`, ahora con ayuda de IA |
| Bloque 3 · reto | Se recorre el bucle completo, una skill por tramo, para construir **un dashboard** sobre el dataset que da el curso. La consigna está en `reto.html` |
| Clases 4 a 14 | Es la herramienta con la que su equipo trabaja el proyecto del semestre |

Fíjese en lo que el demo demuestra sin decirlo: en el Tramo B las cuatro skills se aplican a un
archivo de texto, y en el reto se aplican a un dashboard. Es el mismo método sobre dos objetos que
no se parecen en nada. Si hubiera que reescribirlas para cambiar de objeto, no serían un método.

**No hay que escribir skills nuevas para el reto**: el trabajo es usar éstas de verdad, que es
distinto de haberlas visto instalar.

## De dónde salieron

No se inventaron para la clase. Son una adaptación de las cuatro skills que el profesor usa todos
los días para trabajar, con una sola cosa quitada: **lo que era de su empresa y de su flujo de
ingeniería** (números de ticket, el gestor de proyectos que usan, las rutas de sus repositorios, los
agentes internos a los que delega, las órdenes de commit y de pull request).

Lo demás se conservó tal cual, porque el original ya era general: no era un skill de software, era
un skill de trabajar.

**Lo que se conservó es el método:** especificar antes de planear, planear antes de ejecutar,
escribir el criterio de aceptación antes de que exista el resultado, ejecutar un paso por vez
comprobando cada uno, y validar contra lo que se escribió al principio.

## Por qué ejecutar sí tiene skill propio

Es el tramo que más se delega, y por eso es el que más fácil se va de las manos. Un modelo al que se
le entrega un plan de seis pasos los hace los seis de un tirón, no comprueba ninguno, y devuelve un
resultado que se ve terminado. `ejecuta-plan` existe para imponer lo contrario: **un paso, su
comprobación, y parar**.

## Cada carpeta trae `references/`

Un skill puede apoyarse en archivos auxiliares que viven junto a él. No se pegan en el chat: se
consultan cuando hacen falta.

| Skill | Archivo de apoyo | Para qué |
|-------|------------------|----------|
| `especifica-encargo/` | `references/plantilla-encargo.md` | La estructura completa de un encargo |
| `planea-trabajo/` | `references/plantilla-plan.md` | La estructura de un plan y cómo se escribe un buen paso |
| `ejecuta-plan/` | `references/ejemplos-resumen.md` | Resúmenes de paso que sirven y que no sirven |
| `valida-resultado/` | `references/como-se-valida.md` | Cómo se pasa de un criterio a una lista de condiciones, y las cuatro preguntas del analista como ejemplo |

---

## Instalarlas es copiar carpetas

No hace falta Node.js, ni una cuenta, ni internet. Un skill es un archivo de texto plano:
instalarlo es ponerlo donde tu herramienta lo busca.

Copia las cuatro carpetas dentro de la carpeta de skills de tu herramienta:

| Herramienta | Dónde van |
|-------------|-----------|
| Gemini CLI | `.gemini/skills/` |
| OpenCode | `.opencode/skills/` |
| Claude Code | `.claude/skills/` |
| Codex CLI | `.codex/skills/` |

**Si no tienes ninguna instalada, usa `.gemini/` igual.** Es una carpeta normal con texto adentro,
y el día que instales una herramienta cambias el nombre de la carpeta y sigues. Eso es lo que
significa que `SKILL.md` sea un estándar abierto: eliges una herramienta, no una religión.

### O descomprimir el ZIP

Cada skill viene además empaquetado en `zips/<nombre>.zip`. Al descomprimirlo queda la carpeta
completa con su `SKILL.md` y su `references/` adentro:

```
especifica-encargo/
    SKILL.md
    references/
        plantilla-encargo.md
```

Descomprime dentro de la carpeta de skills de tu herramienta y ya está instalado. Es la misma
instalación, en un solo archivo, para cuando toque mandarla por correo o subirla a un formulario.

---

## Usarlas sin instalar nada

El bucle funciona igual a mano, y así es como lo recorre esta clase:

1. Abre el `SKILL.md` del tramo en el que estás.
2. Pega su contenido en el chatbot que uses, y debajo escribe tu encargo.
3. Lee lo que vuelve **contra el bloque `## Formato` de ese mismo archivo**: si el skill prometía
   cinco secciones y volvieron tres, el que está mal es el skill, no el modelo.
4. Pasa al tramo siguiente con lo que produjo el anterior.

Un CLI automatiza el paso 2 y nada más. El trabajo del analista está en los pasos 1, 3 y 4, y
ninguno depende de una instalación.

---

## Si la validación falla

Se vuelve a **especificar**. No se parcha el resultado.

Un resultado que responde otra cosa casi siempre viene de un encargo que pedía otra cosa. Arreglar
la salida esconde el problema y lo devuelve la próxima vez, cuando ya nadie se acuerde.
