# Clase 7 · Bloque 3 — Reto

## Tu ecosistema de 3 skills

**Modalidad:** en equipo (1-2 personas, el mismo equipo del proyecto del semestre)
**Entregable:** `reto_starter.ipynb` completo, más los archivos `SKILL.md` que escribas
**Requisito previo:** haber recorrido el Bloque 2
**Cómo se comprueba:** el cuaderno trae **7 puntos de verificación** (`R1` a `R7`) repartidos entre
las seis tareas. Cada uno da una pista dirigida **sin revelar la respuesta**, y el punto de control
del final dice cuántos van en verde. La solución no se publica: el reto se resuelve en voz alta en
el cierre de la sesión, y si te trabas, preguntas ahí mismo.

---

## Antes de nada: qué NO hace falta

**Este reto no necesita Node.js, ni una cuenta, ni internet.** Solo Python y el entorno del curso,
igual que todos los demás retos.

Instalar un CLI de IA en tu máquina es una **recomendación** de este curso. No es un requisito y
no lo va a ser:

- No hace falta para este reto.
- No hace falta para el Momento 2 ni para el Momento 3.
- **No se evalúa.** No aparece en ninguna rúbrica del curso, ni aquí ni más adelante.

Si tu equipo tiene un CLI instalado, hay una sección opcional al final del notebook que cierra el
ciclo ejecutando lo que escribiste. Si no lo tienes, haces el reto completo igual que todo el
mundo, y no te falta nada evaluable.

---

## La consigna

Diseña y construye el ecosistema de **3 skills** que tu proyecto del semestre va a necesitar.

No skills genéricas. Skills para **tu** dataset y **tus** preguntas de investigación.

La diferencia entre un ecosistema y una colección de archivos sueltos es que el ecosistema cubre
fases distintas del trabajo. Tres skills que hacen casi lo mismo no son un ecosistema: son un
skill mal partido en tres.

---

## Por qué esto importa ahora y no en la clase 12

Faltan cinco clases para el entregable del Momento 2: dashboard más narrativa.

Los skills que escribas hoy los vas a usar en las clases 8, 9, 10 y 11. Si los escribes bien, cada
uno te ahorra trabajo cuatro veces. Si los escribes el día antes de la sustentación, no te ahorran
nada.

Esto no es un ejercicio de calentamiento. Es infraestructura.

---

## Tareas

### Tarea 0 — Punto de partida

Escribe qué sabes de tu proyecto: dataset, preguntas de investigación y, sobre todo, **los nombres
exactos de las columnas que más usas**, tal como aparecen en tu CSV.

Esos nombres no son decorativos. El verificador los va a buscar dentro de tu primer skill, porque
son la diferencia mecánica entre un skill tuyo y un skill genérico.

### Tarea 1 — Plan de ecosistema

Antes de escribir un solo archivo, decide **cuáles** tres skills necesitas.

| Fase | Qué produces | Ejemplos de skill útil |
|------|--------------|------------------------|
| `preparacion` | Datos limpios y documentados | Reporte de calidad, generador de script de limpieza, diccionario de datos |
| `analisis` | Hallazgos y gráficos | Resumen de EDA, recomendador de tipo de gráfico, reportador de outliers |
| `comunicacion` | Dashboard, narrativa, README | Esquema de narrativa, redactor de resumen ejecutivo, generador de README |

Para cada skill: nombre en formato de carpeta (minúsculas, con guiones), fase y **una frase que
diga qué sale de él**.

> **Criterio de corte:** si no puedes describir en una frase qué sale del skill, el skill todavía
> no existe. Vuelve a pensarlo antes de abrir un archivo.

**Regla del ecosistema:** los tres skills deben cubrir **al menos dos fases distintas**. Si los
tres son de preparación, fusiona dos y busca el tercero en otra fase.

### Tarea 2 — Construir los tres skills

Escribe los tres `SKILL.md`, en la carpeta que corresponde a tu herramienta:

```
<carpeta-de-la-herramienta>/skills/<nombre-del-skill>/SKILL.md
```

Si no tienes ninguna herramienta instalada, usa `.gemini/` como carpeta de trabajo. **El archivo
de adentro es idéntico en las cuatro**: el día que instales una, cambias el nombre de la carpeta y
sigues. Eso es lo que quiere decir que el estándar sea abierto.

Cada archivo debe tener:

- **Frontmatter** completo: `name`, `description`, `version`, entre tres guiones arriba y abajo,
  y los de arriba en la línea 1.
- **Instrucciones** específicas. No "analiza los datos".
- **Formato** de salida definido explícitamente, con las secciones exactas.
- **Mínimo dos reglas**, y al menos una que diga algo que el skill **NO** debe hacer.

Y cada skill debe estar **anclado a tu proyecto**: tus columnas reales, tus umbrales reales, tus
preguntas de investigación reales. Un skill que funcionaría igual para cualquier dataset es un
skill genérico, y los genéricos ya existen: no aportas nada escribiéndolos otra vez.

### Tarea 3 — La salida que esperas

Escribe a mano la salida que esperas de tu skill 1: completa, con las secciones que tu propio
bloque `## Formato` promete, con cifras inventadas donde haga falta pero con **tus** columnas y
**tus** categorías.

Es la tarea incómoda del reto y es la que hace que un skill sirva.

Cuando ejecutas un skill y miras la salida, juzgas a posteriori: ya viste algo y decides si te
gusta. Es facilísimo conformarse. Cuando la escribes **antes**, tienes que decidir qué quieres, y
ahí se descubre que el bloque de formato no decía lo suficiente.

El verificador compara las dos cosas: lo que tu skill **promete** contra lo que tu salida esperada
**trae**. Si no coinciden, el que está mal casi siempre es el skill.

### Tarea 4 — Auditar lo que acabas de escribir

Pasa tus tres archivos por el mismo auditor de seguridad del Bloque 2, y escribe un veredicto
sobre el primero: si un compañero de otro equipo se lo encontrara, ¿lo instalaría?

Tus skills son "skills de terceros" para todo el que no seas tú.

### Tarea 5 — Reflexión

Cortas y honestas. Si crees que estas herramientas están sobrevaloradas, dilo y explica por qué:
es una respuesta perfectamente válida y vale igual que una entusiasta.

---

## Qué comprueba el verificador, y qué no

Vale la pena ser exacto, porque un chequeo mecánico mal entendido se vuelve una lista de casillas.

| Sí comprueba | No comprueba |
|--------------|--------------|
| Que el plan tenga forma de ecosistema y cubra dos fases | Que sean los tres skills que tu proyecto de verdad necesita |
| Que los tres archivos estén bien armados: frontmatter, instrucciones, formato, reglas | Que los skills sean buenos |
| Que el skill 1 nombre las columnas reales de tu CSV | Que las instrucciones sean las correctas para tu pregunta |
| Que la salida que esperas cumpla el contrato que tu propio skill declara | Que la salida real de un modelo se le parezca |
| Que ninguno de tus skills dispare una bandera roja de seguridad | Si el skill es útil |

**Ninguna tarea se comprueba contra una respuesta correcta**, porque tu proyecto es tuyo y el
cuaderno no lo conoce. Lo que se comprueba es la forma. No es poca cosa: la mayoría de los errores
de un skill viven en la forma del archivo, no en la salida del modelo.

---

## Checklist de calidad de un skill

Antes de dar por terminado cada uno:

- [ ] El frontmatter tiene `name`, `description` y `version`, y abre con tres guiones en la línea 1
- [ ] La `description` dice **cuándo** usar el skill, no solo qué hace
- [ ] Las instrucciones nombran columnas, métricas o umbrales de tu proyecto
- [ ] La sección de formato define las secciones exactas de la salida
- [ ] Hay al menos dos reglas que restringen al modelo
- [ ] Al menos una regla pone un límite de alcance ("no hagas X")
- [ ] La carpeta se llama como el skill y el archivo se llama `SKILL.md`

---

## Errores que ya sabemos que van a pasar

| Error | Cómo se ve | Cómo se arregla |
|-------|-----------|-----------------|
| Skill genérico | "Mejora mis gráficos" | Describe la salida sección por sección. Si no puedes, el skill no existe todavía |
| Tres skills que son uno | Los tres tocan la fase de preparación | Fusiona dos, busca el tercero en análisis o comunicación |
| Sin sección de formato | No puedes escribir la salida que esperas | Escribe las secciones exactas que quieres, con `### ` |
| Frontmatter sin los guiones de arriba | El archivo se ve perfecto y la herramienta lo ignora | Los tres guiones van en la **línea 1**, sin nada antes |
| Todo el tiempo en el plan | Siguen discutiendo nombres y no han abierto un archivo | El plan es corto a propósito. Escribe el primero y arréglalo después |
| Editar la celda y no volver a ejecutarla | El verificador sigue reportando lo mismo | Lee el archivo del disco, no la celda. Vuelve a ejecutar el `%%writefile` |

---

## Entrega

Sube una carpeta comprimida con:

```
reto07_<apellidos>/
    reto_completo.ipynb          # el starter, completo
    skills/
        <skill-1>/SKILL.md
        <skill-2>/SKILL.md
        <skill-3>/SKILL.md
```

**Fecha de entrega:** antes de la clase 8.

---

## Cómo se valora

**Este reto no produce nota ni cumplido / no cumplido.** Es práctica. La retroalimentación usa el
mismo instrumento de los momentos evaluativos —**Saber, Ser y Hacer, una banda por dimensión**:
Excelente, Bueno, Aceptable, Insuficiente, No aceptable— para que llegues familiarizado a las
clases 6, 12 y 15. **Las tres dimensiones pesan lo mismo** y los elementos de cada fila **no tienen
peso**: no se suman ni se promedian, alimentan una sola banda por dimensión.

| Dimensión | Qué se mira en este reto |
|-----------|--------------------------|
| **Saber** | El plan de ecosistema es coherente y cubre al menos dos fases: se entiende por qué cada skill existe y qué fase del trabajo cubre |
| **Ser** | La reflexión muestra criterio propio, y el veredicto de la auditoría es una decisión con razón, no una casilla. Reconocer dónde tu propio skill queda corto es parte de lo que se valora, no algo que se esconde |
| **Hacer** | Los tres skills están bien estructurados (frontmatter, instrucciones, formato, reglas), anclados al proyecto propio y no genéricos, y la salida esperada del skill 1 cumple el contrato que ese skill declara |

**Topes por omisión** (techo a la banda, nunca resta, y no se acumulan):

- Tres skills genéricos, que servirían para cualquier proyecto: **Hacer** no pasa de Aceptable. El
  anclaje al dataset propio es el punto del reto.
- Sin la salida esperada del skill 1, o escrita sin las secciones que el propio skill promete:
  **Hacer** no pasa de Aceptable.
- Reflexión que solo repite lo que dijo el profesor: **Ser** no pasa de Aceptable.

**Nada de lo opcional se evalúa.** Tener o no tener un CLI instalado, y haber ejecutado o no los
skills, **no entra en ninguna de las tres dimensiones**. Este curso no exige lo que no enseña.

---

## Opcional, para cerrar en casa

Marcado como opcional: no se valora, pero se nota en las siguientes cinco clases.

- **Instalar un CLI de IA y ejecutar tus skills de verdad.** Las instrucciones están en
  [`INSTALACION.md`](../INSTALACION.md), sección 12. Cuando tengas la salida real, compárala con la
  que escribiste en la Tarea 3: la distancia entre las dos es la medida exacta de qué tan
  específico era tu bloque de formato.
- Escribir un archivo `PROYECTO.md` en la raíz de tu proyecto con el dataset, sus columnas, tus
  preguntas de investigación y las decisiones tomadas hasta hoy. Es la "memoria en archivos" de la
  que hablamos en el Bloque 1: a partir de que exista, no vuelves a explicarle tu proyecto a nadie
  desde cero, ni a una persona ni a una herramienta.
- Guardar tus skills en un repositorio propio. Son texto plano y siguen un estándar abierto: te van
  a servir en otras materias y después de graduarte.
